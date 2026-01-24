#!/usr/bin/env python3
"""
Probe Promotion Script
======================
Handoff: 0804-king-probe_promotion_engine_runs_only

Purpose: Promote one successful probe output into a single engine_runs row
         WITHOUT executing any engine, writing decisions, or modifying policy.

Authorization: LIMITED_AUTHORIZATION
Scope: Insert exactly one engine_runs row; nothing else.
"""

import hashlib
import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

# ============================================================================
# CONFIGURATION (from handoff preconditions)
# ============================================================================

PROBE_ID = "probe_20260124_052401"
PROBE_DIR = Path("scripts/2026-01-24/outputs/probe_20260124_052401")
RAW_OUTPUT_PATH = PROBE_DIR / "raw_output.json"
EXPECTED_RAW_OUTPUT_HASH = "0c515e41e5f3e039d419779299585156c6180ba86513116c4a2146ecb2e5d7d2"

EXPERIMENT_ID = "exp_probe_promotion_20260124"
DB_PATH = Path("scripts/2026-01-24/outputs/probe_promotion/decisiondb.sqlite")
MANIFEST_PATH = Path("scripts/2026-01-24/outputs/probe_promotion/promotion_manifest.json")

# From probe manifest
ENGINE_NAME = "pax_pathfinder"
ENGINE_VERSION = "1.0.0"
ENGINE_CONFIG_HASH = "a5ecc09429ac27a29ac881f177b5b58a946fd79569dd851f90ac23a7dcdafd45"
REPRESENTATION_ID = "cb9f8c1d418c4678"
RUNTIME_MS = 1

# ============================================================================
# SCHEMA
# ============================================================================

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS snapshots (
    snapshot_id TEXT PRIMARY KEY,
    created_at TEXT NOT NULL,
    time_window_start TEXT NOT NULL,
    time_window_end TEXT NOT NULL,
    provenance_json TEXT NOT NULL,
    artifact_manifest_json TEXT NOT NULL,
    snapshot_version TEXT NOT NULL DEFAULT '1',
    notes TEXT,
    experiment_id TEXT
);

CREATE TABLE IF NOT EXISTS representations (
    representation_id TEXT PRIMARY KEY,
    snapshot_id TEXT NOT NULL,
    representation_spec_json TEXT NOT NULL,
    representation_namespace TEXT NOT NULL,
    factory_version TEXT NOT NULL,
    artifact_uri TEXT,
    artifact_sha256 TEXT,
    status TEXT NOT NULL DEFAULT 'pending',
    error_text TEXT,
    experiment_id TEXT,
    FOREIGN KEY (snapshot_id) REFERENCES snapshots(snapshot_id)
);

CREATE TABLE IF NOT EXISTS engine_runs (
    engine_run_id TEXT PRIMARY KEY,
    representation_id TEXT NOT NULL,
    engine_name TEXT NOT NULL,
    engine_version TEXT NOT NULL,
    engine_config_json TEXT NOT NULL,
    engine_config_hash TEXT NOT NULL,
    runtime_ms INTEGER,
    raw_output_uri TEXT,
    raw_output_sha256 TEXT,
    status TEXT NOT NULL DEFAULT 'pending',
    error_text TEXT,
    experiment_id TEXT,
    FOREIGN KEY (representation_id) REFERENCES representations(representation_id)
);

CREATE TABLE IF NOT EXISTS decisions (
    decision_id TEXT PRIMARY KEY,
    decision_type TEXT NOT NULL,
    equivalence_policy_version TEXT NOT NULL,
    decision_signature_json TEXT NOT NULL,
    decision_payload_json TEXT NOT NULL,
    experiment_id TEXT
);

CREATE TABLE IF NOT EXISTS f_map (
    representation_id TEXT NOT NULL,
    engine_run_id TEXT NOT NULL,
    decision_id TEXT NOT NULL,
    aux_metrics_json TEXT,
    experiment_id TEXT,
    PRIMARY KEY (representation_id, engine_run_id),
    FOREIGN KEY (representation_id) REFERENCES representations(representation_id),
    FOREIGN KEY (engine_run_id) REFERENCES engine_runs(engine_run_id),
    FOREIGN KEY (decision_id) REFERENCES decisions(decision_id)
);

CREATE TABLE IF NOT EXISTS _schema_meta (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);
"""


def compute_sha256(file_path: Path) -> str:
    """Compute SHA256 hash of file contents."""
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def derive_engine_run_id(representation_id: str, config_hash: str, raw_output_hash: str) -> str:
    """Derive deterministic engine_run_id from content."""
    content = f"{representation_id}:{config_hash}:{raw_output_hash}"
    hash_bytes = hashlib.sha256(content.encode()).hexdigest()[:16]
    return f"run_promoted_{hash_bytes}"


def get_table_counts(conn: sqlite3.Connection) -> dict:
    """Get row counts for all tables."""
    tables = ["snapshots", "representations", "engine_runs", "decisions", "f_map"]
    counts = {}
    for table in tables:
        cursor = conn.execute(f"SELECT COUNT(*) FROM {table}")
        counts[table] = cursor.fetchone()[0]
    return counts


def main():
    print("=" * 60)
    print("Probe Promotion: engine_runs insert only")
    print("=" * 60)
    
    # Verify preconditions
    if not RAW_OUTPUT_PATH.exists():
        print(f"ERROR: raw_output.json not found at {RAW_OUTPUT_PATH}")
        sys.exit(1)
    
    # Verify hash
    actual_hash = compute_sha256(RAW_OUTPUT_PATH)
    print(f"Raw output hash (computed): {actual_hash}")
    print(f"Raw output hash (expected): {EXPECTED_RAW_OUTPUT_HASH}")
    
    if actual_hash != EXPECTED_RAW_OUTPUT_HASH:
        print("ERROR: Hash mismatch! Aborting.")
        sys.exit(1)
    
    print("Hash verification: PASSED")
    
    # Load probe manifest for config
    probe_manifest_path = PROBE_DIR / "probe_manifest.json"
    with open(probe_manifest_path) as f:
        probe_manifest = json.load(f)
    
    # Reconstruct engine config from probe context
    # This is a placeholder; in production, config would be stored in probe manifest
    engine_config = {
        "promoted_from_probe": PROBE_ID,
        "original_config_hash": ENGINE_CONFIG_HASH,
        "note": "Config reconstructed from probe metadata"
    }
    engine_config_json = json.dumps(engine_config, sort_keys=True)
    
    # Derive engine_run_id
    engine_run_id = derive_engine_run_id(
        REPRESENTATION_ID, ENGINE_CONFIG_HASH, actual_hash
    )
    print(f"Derived engine_run_id: {engine_run_id}")
    
    # Create database and schema
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    # Check if DB already exists
    db_existed = DB_PATH.exists()
    if db_existed:
        print(f"WARNING: Database already exists at {DB_PATH}")
    
    conn = sqlite3.connect(DB_PATH)
    conn.executescript(SCHEMA_SQL)
    conn.execute(
        "INSERT OR REPLACE INTO _schema_meta (key, value) VALUES (?, ?)",
        ("schema_version", "1.0.0")
    )
    
    # Get before counts
    before_counts = get_table_counts(conn)
    print(f"Before counts: {before_counts}")
    
    # Check authorization limit
    if before_counts["engine_runs"] >= 1:
        print("ERROR: engine_runs already has rows. Authorization limit is 1 insert.")
        print("       This promotion requires an empty engine_runs table.")
        conn.close()
        sys.exit(1)
    
    # Insert engine_runs row
    raw_output_uri = str(RAW_OUTPUT_PATH.resolve())
    
    conn.execute(
        """
        INSERT INTO engine_runs (
            engine_run_id, representation_id, engine_name, engine_version,
            engine_config_json, engine_config_hash, runtime_ms,
            raw_output_uri, raw_output_sha256, status, experiment_id
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            engine_run_id,
            REPRESENTATION_ID,
            ENGINE_NAME,
            ENGINE_VERSION,
            engine_config_json,
            ENGINE_CONFIG_HASH,
            RUNTIME_MS,
            raw_output_uri,
            actual_hash,
            "complete",
            EXPERIMENT_ID,
        )
    )
    conn.commit()
    
    # Get after counts
    after_counts = get_table_counts(conn)
    print(f"After counts: {after_counts}")
    
    # Verify success criteria
    assert after_counts["engine_runs"] == 1, "Expected exactly 1 engine_runs row"
    assert after_counts["decisions"] == 0, "decisions table should be unchanged"
    assert after_counts["f_map"] == 0, "f_map table should be unchanged"
    assert after_counts["snapshots"] == before_counts["snapshots"], "snapshots should be unchanged"
    assert after_counts["representations"] == before_counts["representations"], "representations should be unchanged"
    
    # Read back the inserted row to verify
    cursor = conn.execute("SELECT * FROM engine_runs WHERE engine_run_id = ?", (engine_run_id,))
    row = cursor.fetchone()
    assert row is not None, "Inserted row not found"
    
    conn.close()
    
    # Generate promotion manifest
    manifest = {
        "manifest_version": "1.0.0",
        "authorization": "LIMITED_AUTHORIZATION",
        "authorization_type": "PROBE_PROMOTION",
        "handoff_id": "0804-king-probe_promotion_engine_runs_only",
        "experiment_id": EXPERIMENT_ID,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "probe": {
            "probe_id": PROBE_ID,
            "probe_dir": str(PROBE_DIR),
            "raw_output_path": str(RAW_OUTPUT_PATH),
            "raw_output_sha256": actual_hash,
        },
        "engine_run": {
            "engine_run_id": engine_run_id,
            "representation_id": REPRESENTATION_ID,
            "engine_name": ENGINE_NAME,
            "engine_version": ENGINE_VERSION,
            "engine_config_hash": ENGINE_CONFIG_HASH,
            "runtime_ms": RUNTIME_MS,
            "status": "complete",
        },
        "database": {
            "path": str(DB_PATH),
            "before_counts": before_counts,
            "after_counts": after_counts,
        },
        "verification": {
            "hash_verified": True,
            "insert_count": 1,
            "no_decisions_written": True,
            "no_fmap_written": True,
            "no_snapshots_modified": True,
            "no_representations_modified": True,
        },
        "notes": [
            "This is a one-time bridge operation.",
            "No engine execution was performed.",
            "The raw_output was sourced from an existing probe artifact.",
            "Decision extraction requires a separate authorization.",
        ]
    }
    
    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2)
    
    print()
    print("=" * 60)
    print("PROMOTION COMPLETE")
    print("=" * 60)
    print(f"Engine run inserted: {engine_run_id}")
    print(f"Database: {DB_PATH}")
    print(f"Manifest: {MANIFEST_PATH}")
    print()
    print("Success criteria verified:")
    print("  - Exactly 1 engine_runs row inserted")
    print("  - No decisions written")
    print("  - No f_map written")
    print("  - No snapshots modified")
    print("  - No representations modified")
    print("  - Hash verified against on-disk artifact")


if __name__ == "__main__":
    main()
