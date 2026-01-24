#!/usr/bin/env python3
"""
Replay expansion verification v3 for all persisted decisions after forward growth.

AUTHORIZATION: REPLAY_VERIFICATION_ONLY (LIMITED)
HANDOFF: 0925-king-replay_authorization_expansion_v3

This script is read-only. It does NOT:
- Execute any engines
- Write to any database
- Modify any artifacts
- Access any network resources

It DOES:
- Verify replay determinism for all persisted decisions
- Recompute decision identities from raw output
- Compare computed values against persisted manifests
- Report PASS or FAIL with evidence for each decision
"""

import json
import hashlib
import sys
from pathlib import Path
from datetime import datetime, timezone

# Authorization constants
AUTHORIZED_POLICY_ID = "pol_d8da3e00e9584eb1"

# Expected equivalence policy spec (frozen)
EQUIVALENCE_POLICY_SPEC = {
    "policy_type": "exact",
    "policy_version": "1.0.0",
    "level": "exact",
    "description": "Bit-for-bit identity. Decision identity is sha256 of canonical route payload.",
    "hash_source": "route.nodes",
    "canonicalization": "json_sorted_keys_utf8",
    "match_rule": "sha256_equality",
}

# All decision sources (3 decisions across 3 experiments)
DECISION_SOURCES = [
    {
        "decision_id": "dec_e28092c4dc33b8f1",
        "experiment_id": "exp_20260124T102432Z",
        "manifest_path": "outputs/engine/exp_20260124T102432Z/decision_manifest.json",
        "raw_output_path": "outputs/engine/exp_20260124T102432Z/engine_output.json",
        "database_path": "outputs/engine/exp_20260124T102432Z/decisiondb.sqlite",
    },
    {
        "decision_id": "dec_c2dda068734c9107",
        "experiment_id": "exp_probe_promotion_20260124",
        "manifest_path": "outputs/probe_promotion/decision_manifest_expansion.json",
        "raw_output_path": "outputs/probe_20260124_052401/raw_output.json",
        "database_path": "outputs/probe_promotion/decisiondb.sqlite",
    },
    {
        "decision_id": "dec_bd75e5723d8af952",
        "experiment_id": "exp_20260124T142041Z",
        "manifest_path": "outputs/engine/exp_20260124T142041Z/decision_manifest.json",
        "raw_output_path": "outputs/engine/exp_20260124T142041Z/engine_output.json",
        "database_path": "outputs/engine/exp_20260124T142041Z/decisiondb.sqlite",
    },
]


def canonical_json(obj) -> str:
    """Serialize to canonical JSON (sorted keys, no whitespace)."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def canonical_hash(obj) -> str:
    """Compute SHA-256 of canonical JSON representation."""
    data = canonical_json(obj).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def make_id(entity_type: str, payload: dict) -> str:
    """Generate content-addressed identifier."""
    prefixes = {
        "snapshot": "snap_",
        "representation": "repr_",
        "engine_run": "run_",
        "decision": "dec_",
        "experiment": "exp_",
        "policy": "pol_",
    }
    prefix = prefixes.get(entity_type, f"{entity_type}_")
    full_hash = canonical_hash(payload)
    return f"{prefix}{full_hash[:16]}"


def compute_policy_id(spec: dict) -> str:
    """Compute content-addressed policy ID from spec."""
    return f"pol_{canonical_hash(spec)[:16]}"


def extract_decision_payload(raw_output: dict) -> dict:
    """Extract identity-bearing payload from raw engine output."""
    return {
        "nodes": raw_output.get("nodes", []),
        "path_found": raw_output.get("path_found", False),
    }


def compute_decision_id_from_payload(payload: dict, policy_id: str) -> str:
    """Compute decision ID from payload and policy."""
    combined = {
        "policy_id": policy_id,
        "payload": payload,
    }
    return make_id("decision", combined)


def verify_decision(source: dict, base_dir: Path, policy_id: str) -> dict:
    """Verify a single decision from its source artifacts."""
    result = {
        "decision_id": source["decision_id"],
        "experiment_id": source["experiment_id"],
        "database": source.get("database_path", "unknown"),
        "checks": [],
        "verdict": None,
    }
    
    # Load manifest
    manifest_path = base_dir / source["manifest_path"]
    if not manifest_path.exists():
        result["checks"].append({
            "check": "manifest_exists",
            "status": "FAIL",
            "message": f"Manifest not found: {manifest_path}",
        })
        result["verdict"] = "FAIL"
        return result
    
    with open(manifest_path) as f:
        manifest = json.load(f)
    
    result["checks"].append({
        "check": "manifest_exists",
        "status": "PASS",
    })
    
    # Load raw output
    raw_output_path = base_dir / source["raw_output_path"]
    if not raw_output_path.exists():
        result["checks"].append({
            "check": "raw_output_exists",
            "status": "FAIL",
            "message": f"Raw output not found: {raw_output_path}",
        })
        result["verdict"] = "FAIL"
        return result
    
    with open(raw_output_path) as f:
        raw_output = json.load(f)
    
    result["checks"].append({
        "check": "raw_output_exists",
        "status": "PASS",
    })
    
    # Get persisted values
    persisted_policy = manifest.get("equivalence_policy", {})
    persisted_decision = manifest.get("decision", {})
    persisted_policy_id = persisted_policy.get("policy_id")
    persisted_decision_id = persisted_decision.get("decision_id")
    persisted_payload_hash = persisted_decision.get("signature", {}).get("payload_hash")
    
    # Check 1: Policy ID match
    recomputed_policy_id = compute_policy_id(EQUIVALENCE_POLICY_SPEC)
    
    policy_match = (
        persisted_policy_id == recomputed_policy_id == policy_id
    )
    
    result["checks"].append({
        "check": "policy_id_deterministic",
        "status": "PASS" if policy_match else "FAIL",
        "recomputed": recomputed_policy_id,
        "persisted": persisted_policy_id,
        "match": policy_match,
    })
    
    if not policy_match:
        result["verdict"] = "FAIL"
        return result
    
    # Check 2: Extract payload
    payload = extract_decision_payload(raw_output)
    node_count = len(payload.get("nodes", []))
    
    result["checks"].append({
        "check": "payload_extraction",
        "status": "PASS",
        "node_count": node_count,
        "path_found": payload.get("path_found"),
    })
    
    # Check 3: Payload hash match
    recomputed_payload_hash = canonical_hash(payload)[:16]
    
    payload_hash_match = recomputed_payload_hash == persisted_payload_hash
    
    result["checks"].append({
        "check": "payload_hash_deterministic",
        "status": "PASS" if payload_hash_match else "FAIL",
        "recomputed": recomputed_payload_hash,
        "persisted": persisted_payload_hash,
        "match": payload_hash_match,
    })
    
    if not payload_hash_match:
        result["verdict"] = "FAIL"
        return result
    
    # Check 4: Decision ID match
    recomputed_decision_id = compute_decision_id_from_payload(
        payload, recomputed_policy_id
    )
    
    decision_id_match = recomputed_decision_id == persisted_decision_id == source["decision_id"]
    
    result["checks"].append({
        "check": "decision_id_deterministic",
        "status": "PASS" if decision_id_match else "FAIL",
        "recomputed": recomputed_decision_id,
        "persisted": persisted_decision_id,
        "authorized": source["decision_id"],
        "match": decision_id_match,
    })
    
    if not decision_id_match:
        result["verdict"] = "FAIL"
        return result
    
    # Check 5: Signature consistency
    recomputed_signature = {
        "node_count": node_count,
        "path_found": payload.get("path_found", False),
        "payload_hash": recomputed_payload_hash,
    }
    persisted_signature = persisted_decision.get("signature", {})
    
    signature_match = recomputed_signature == persisted_signature
    
    result["checks"].append({
        "check": "signature_consistent",
        "status": "PASS" if signature_match else "FAIL",
        "recomputed": recomputed_signature,
        "persisted": persisted_signature,
        "match": signature_match,
    })
    
    if not signature_match:
        result["verdict"] = "FAIL"
        return result
    
    result["verdict"] = "PASS"
    result["verified_hashes"] = {
        "decision_id": recomputed_decision_id,
        "policy_id": recomputed_policy_id,
        "payload_hash": recomputed_payload_hash,
        "node_count": node_count,
    }
    return result


def main():
    results = {
        "verification_type": "replay_expansion_v3",
        "authorization": "REPLAY_VERIFICATION_ONLY",
        "handoff_id": "0925-king-replay_authorization_expansion_v3",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "policy_id": AUTHORIZED_POLICY_ID,
        "decision_count": len(DECISION_SOURCES),
        "decisions_verified": 0,
        "decisions_passed": 0,
        "decisions_failed": 0,
        "decision_results": [],
        "databases_enumerated": [],
        "verdict": None,
    }
    
    # Determine base directory
    script_dir = Path(__file__).parent
    base_dir = script_dir.parent.parent.parent
    
    # Enumerate databases
    databases = []
    for source in DECISION_SOURCES:
        db_path = base_dir / source["database_path"]
        if db_path.exists():
            databases.append(source["database_path"])
    results["databases_enumerated"] = databases
    
    # Verify policy ID computation is stable
    recomputed_policy_id = compute_policy_id(EQUIVALENCE_POLICY_SPEC)
    if recomputed_policy_id != AUTHORIZED_POLICY_ID:
        results["error"] = f"Policy ID mismatch: computed {recomputed_policy_id}, expected {AUTHORIZED_POLICY_ID}"
        results["verdict"] = "FAIL"
        print(json.dumps(results, indent=2))
        return 1
    
    results["policy_verification"] = {
        "recomputed": recomputed_policy_id,
        "expected": AUTHORIZED_POLICY_ID,
        "match": True,
    }
    
    # Verify each decision
    for source in DECISION_SOURCES:
        decision_result = verify_decision(source, base_dir, AUTHORIZED_POLICY_ID)
        results["decision_results"].append(decision_result)
        results["decisions_verified"] += 1
        
        if decision_result["verdict"] == "PASS":
            results["decisions_passed"] += 1
        else:
            results["decisions_failed"] += 1
    
    # Determine overall verdict
    if results["decisions_failed"] > 0:
        results["verdict"] = "FAIL"
        exit_code = 1
    else:
        results["verdict"] = "PASS"
        exit_code = 0
    
    results["summary"] = {
        "total_decisions": len(DECISION_SOURCES),
        "verified_count": results["decisions_verified"],
        "passed_count": results["decisions_passed"],
        "failed_count": results["decisions_failed"],
        "all_passed": results["decisions_passed"] == len(DECISION_SOURCES),
        "replay_determinism_verified": results["decisions_failed"] == 0,
        "forward_growth_included": True,
        "databases_covered": len(databases),
    }
    
    print(json.dumps(results, indent=2))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
