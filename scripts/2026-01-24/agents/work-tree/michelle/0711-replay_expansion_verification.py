#!/usr/bin/env python3
"""
Replay expansion verification for all persisted decisions.

AUTHORIZATION: REPLAY_VERIFICATION_ONLY (LIMITED)
HANDOFF: 0711-king-replay_authorization_expansion

This script is read-only. It does NOT:
- Execute any engines
- Write to any database
- Modify any artifacts
- Access any network resources

It DOES:
- Enumerate all persisted decisions across all experiments
- Recompute decision identities from persisted raw output
- Compare computed values against persisted decision manifests
- Report PASS or FAIL with evidence for each decision
"""

import json
import hashlib
import sys
from pathlib import Path
from datetime import datetime, timezone

# Authorization constants
AUTHORIZED_POLICY_ID = "pol_d8da3e00e9584eb1"

# Expected equivalence policy spec (from v1 authorization)
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


def find_all_experiments(outputs_dir: Path) -> list:
    """Find all experiment directories with persisted decisions."""
    experiments = []
    
    engine_dir = outputs_dir / "engine"
    if engine_dir.exists():
        for exp_dir in engine_dir.iterdir():
            if exp_dir.is_dir() and exp_dir.name.startswith("exp_"):
                manifest_path = exp_dir / "decision_manifest.json"
                engine_output_path = exp_dir / "engine_output.json"
                if manifest_path.exists() and engine_output_path.exists():
                    experiments.append({
                        "experiment_id": exp_dir.name,
                        "path": exp_dir,
                        "manifest_path": manifest_path,
                        "engine_output_path": engine_output_path,
                    })
    
    return experiments


def verify_decision(experiment: dict, policy_id: str) -> dict:
    """Verify a single decision from an experiment."""
    result = {
        "experiment_id": experiment["experiment_id"],
        "checks": [],
        "verdict": None,
    }
    
    # Load decision manifest
    with open(experiment["manifest_path"]) as f:
        manifest = json.load(f)
    
    # Load raw engine output
    with open(experiment["engine_output_path"]) as f:
        raw_output = json.load(f)
    
    persisted_decision = manifest.get("decision", {})
    persisted_policy = manifest.get("equivalence_policy", {})
    
    result["decision_id"] = persisted_decision.get("decision_id")
    
    # Check 1: Policy ID match
    persisted_policy_id = persisted_policy.get("policy_id")
    recomputed_policy_id = compute_policy_id(EQUIVALENCE_POLICY_SPEC)
    
    policy_match = (
        persisted_policy_id == recomputed_policy_id == policy_id
    )
    
    result["checks"].append({
        "check": "policy_id_deterministic",
        "status": "PASS" if policy_match else "FAIL",
        "recomputed": recomputed_policy_id,
        "persisted": persisted_policy_id,
        "expected": policy_id,
        "match": policy_match,
    })
    
    if not policy_match:
        result["verdict"] = "FAIL"
        return result
    
    # Check 2: Extract payload and verify
    payload = extract_decision_payload(raw_output)
    
    result["checks"].append({
        "check": "payload_extraction",
        "status": "PASS",
        "node_count": len(payload.get("nodes", [])),
        "path_found": payload.get("path_found"),
    })
    
    # Check 3: Payload hash match
    recomputed_payload_hash = canonical_hash(payload)[:16]
    persisted_payload_hash = persisted_decision.get("signature", {}).get("payload_hash")
    
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
    persisted_decision_id = persisted_decision.get("decision_id")
    
    decision_id_match = recomputed_decision_id == persisted_decision_id
    
    result["checks"].append({
        "check": "decision_id_deterministic",
        "status": "PASS" if decision_id_match else "FAIL",
        "recomputed": recomputed_decision_id,
        "persisted": persisted_decision_id,
        "match": decision_id_match,
    })
    
    if not decision_id_match:
        result["verdict"] = "FAIL"
        return result
    
    # Check 5: Signature consistency
    recomputed_signature = {
        "node_count": len(payload.get("nodes", [])),
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
    return result


def main():
    results = {
        "verification_type": "replay_expansion",
        "authorization": "REPLAY_VERIFICATION_ONLY",
        "handoff_id": "0711-king-replay_authorization_expansion",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "policy_id": AUTHORIZED_POLICY_ID,
        "experiments_scanned": 0,
        "decisions_verified": 0,
        "decisions_passed": 0,
        "decisions_failed": 0,
        "decision_results": [],
        "verdict": None,
    }
    
    # Find outputs directory relative to script location
    script_dir = Path(__file__).parent
    outputs_dir = script_dir.parent.parent.parent / "outputs"
    
    if not outputs_dir.exists():
        results["error"] = f"Outputs directory not found: {outputs_dir}"
        results["verdict"] = "BLOCKED"
        print(json.dumps(results, indent=2))
        return 1
    
    # Find all experiments with decisions
    experiments = find_all_experiments(outputs_dir)
    results["experiments_scanned"] = len(experiments)
    
    if len(experiments) == 0:
        results["error"] = "No experiments with persisted decisions found"
        results["verdict"] = "BLOCKED"
        print(json.dumps(results, indent=2))
        return 1
    
    # Verify each decision
    for experiment in experiments:
        decision_result = verify_decision(experiment, AUTHORIZED_POLICY_ID)
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
    elif results["decisions_verified"] == 1:
        results["verdict"] = "PASS_SINGLE"
        results["expansion_blocked"] = True
        results["expansion_reason"] = (
            "Only 1 decision exists. Expansion verification requires "
            "additional decisions to be materialized first."
        )
        exit_code = 0
    else:
        results["verdict"] = "PASS"
        exit_code = 0
    
    results["summary"] = {
        "total_experiments": results["experiments_scanned"],
        "total_decisions": results["decisions_verified"],
        "passed": results["decisions_passed"],
        "failed": results["decisions_failed"],
        "expansion_possible": results["decisions_verified"] > 1,
    }
    
    print(json.dumps(results, indent=2))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
