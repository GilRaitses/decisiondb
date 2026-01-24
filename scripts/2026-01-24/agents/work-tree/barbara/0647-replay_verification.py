#!/usr/bin/env python3
"""
Replay verification for decision dec_e28092c4dc33b8f1.

AUTHORIZATION: REPLAY_VERIFICATION_ONLY (LIMITED)
This script is read-only. It does NOT:
- Execute any engines
- Write to any database
- Modify any artifacts
- Access any network resources

It DOES:
- Recompute decision identity from persisted raw output
- Compare computed values against persisted decision manifest
- Report PASS or FAIL with evidence
"""

import json
import hashlib
import sys
from pathlib import Path
from datetime import datetime, timezone

# Constants from handoff authorization
AUTHORIZED_DECISION_ID = "dec_e28092c4dc33b8f1"
AUTHORIZED_POLICY_ID = "pol_d8da3e00e9584eb1"
AUTHORIZED_EXPERIMENT_ID = "exp_20260124T102432Z"

# Expected equivalence policy spec
EQUIVALENCE_POLICY_SPEC = {
    "policy_type": "exact",
    "policy_version": "1.0.0",
    "level": "exact",
    "description": "Bit-for-bit identity. Decision identity is sha256 of canonical route payload.",
    "hash_source": "route.nodes",
    "canonicalization": "json_sorted_keys_utf8",
    "match_rule": "sha256_equality",
}


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


def main():
    results = {
        "verification_type": "replay",
        "authorization": "REPLAY_VERIFICATION_ONLY",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "experiment_id": AUTHORIZED_EXPERIMENT_ID,
        "expected_decision_id": AUTHORIZED_DECISION_ID,
        "expected_policy_id": AUTHORIZED_POLICY_ID,
        "checks": [],
        "verdict": None,
    }
    
    experiment_dir = Path(__file__).parent.parent.parent.parent / "outputs/engine" / AUTHORIZED_EXPERIMENT_ID
    
    # Check 1: Verify experiment directory exists
    if not experiment_dir.exists():
        results["checks"].append({
            "check": "experiment_dir_exists",
            "status": "FAIL",
            "message": f"Experiment directory not found: {experiment_dir}",
        })
        results["verdict"] = "FAIL"
        print(json.dumps(results, indent=2))
        return 1
    
    results["checks"].append({
        "check": "experiment_dir_exists",
        "status": "PASS",
        "path": str(experiment_dir),
    })
    
    # Check 2: Load decision manifest
    manifest_path = experiment_dir / "decision_manifest.json"
    if not manifest_path.exists():
        results["checks"].append({
            "check": "decision_manifest_exists",
            "status": "FAIL",
            "message": f"Decision manifest not found: {manifest_path}",
        })
        results["verdict"] = "FAIL"
        print(json.dumps(results, indent=2))
        return 1
    
    with open(manifest_path) as f:
        manifest = json.load(f)
    
    results["checks"].append({
        "check": "decision_manifest_exists",
        "status": "PASS",
    })
    
    # Check 3: Load raw engine output
    engine_output_path = experiment_dir / "engine_output.json"
    if not engine_output_path.exists():
        results["checks"].append({
            "check": "engine_output_exists",
            "status": "FAIL",
            "message": f"Engine output not found: {engine_output_path}",
        })
        results["verdict"] = "FAIL"
        print(json.dumps(results, indent=2))
        return 1
    
    with open(engine_output_path) as f:
        raw_output = json.load(f)
    
    results["checks"].append({
        "check": "engine_output_exists",
        "status": "PASS",
    })
    
    # Check 4: Verify policy ID computation is deterministic
    recomputed_policy_id = compute_policy_id(EQUIVALENCE_POLICY_SPEC)
    persisted_policy_id = manifest["equivalence_policy"]["policy_id"]
    
    policy_match = recomputed_policy_id == persisted_policy_id == AUTHORIZED_POLICY_ID
    
    results["checks"].append({
        "check": "policy_id_deterministic",
        "status": "PASS" if policy_match else "FAIL",
        "recomputed": recomputed_policy_id,
        "persisted": persisted_policy_id,
        "authorized": AUTHORIZED_POLICY_ID,
        "match": policy_match,
    })
    
    if not policy_match:
        results["verdict"] = "FAIL"
        print(json.dumps(results, indent=2))
        return 1
    
    # Check 5: Extract decision payload and verify determinism
    payload = extract_decision_payload(raw_output)
    
    results["checks"].append({
        "check": "payload_extraction",
        "status": "PASS",
        "node_count": len(payload.get("nodes", [])),
        "path_found": payload.get("path_found"),
    })
    
    # Check 6: Compute payload hash and compare
    recomputed_payload_hash = canonical_hash(payload)[:16]
    persisted_payload_hash = manifest["decision"]["signature"]["payload_hash"]
    
    payload_hash_match = recomputed_payload_hash == persisted_payload_hash
    
    results["checks"].append({
        "check": "payload_hash_deterministic",
        "status": "PASS" if payload_hash_match else "FAIL",
        "recomputed": recomputed_payload_hash,
        "persisted": persisted_payload_hash,
        "match": payload_hash_match,
    })
    
    if not payload_hash_match:
        results["verdict"] = "FAIL"
        print(json.dumps(results, indent=2))
        return 1
    
    # Check 7: Compute decision ID and compare
    recomputed_decision_id = compute_decision_id_from_payload(payload, recomputed_policy_id)
    persisted_decision_id = manifest["decision"]["decision_id"]
    
    decision_id_match = recomputed_decision_id == persisted_decision_id == AUTHORIZED_DECISION_ID
    
    results["checks"].append({
        "check": "decision_id_deterministic",
        "status": "PASS" if decision_id_match else "FAIL",
        "recomputed": recomputed_decision_id,
        "persisted": persisted_decision_id,
        "authorized": AUTHORIZED_DECISION_ID,
        "match": decision_id_match,
    })
    
    if not decision_id_match:
        results["verdict"] = "FAIL"
        print(json.dumps(results, indent=2))
        return 1
    
    # Check 8: Verify signature consistency
    recomputed_signature = {
        "node_count": len(payload.get("nodes", [])),
        "path_found": payload.get("path_found", False),
        "payload_hash": recomputed_payload_hash,
    }
    persisted_signature = manifest["decision"]["signature"]
    
    signature_match = recomputed_signature == persisted_signature
    
    results["checks"].append({
        "check": "signature_consistent",
        "status": "PASS" if signature_match else "FAIL",
        "recomputed": recomputed_signature,
        "persisted": persisted_signature,
        "match": signature_match,
    })
    
    if not signature_match:
        results["verdict"] = "FAIL"
        print(json.dumps(results, indent=2))
        return 1
    
    # All checks passed
    results["verdict"] = "PASS"
    results["summary"] = {
        "decision_id": recomputed_decision_id,
        "policy_id": recomputed_policy_id,
        "payload_hash": recomputed_payload_hash,
        "all_checks_passed": True,
        "determinism_verified": True,
    }
    
    print(json.dumps(results, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
