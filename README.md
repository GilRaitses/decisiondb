# decisiondb system design

this repository is the decisiondb mirror and is intended to run from `/Users/gilraitses/decisiondb` as a standalone, auditable subsystem.

this page defines the minimal, reproducible system for logging and analyzing decision-valued maps of the form **f : R → D**, where **R** is a family of representations over a fixed snapshot and **D** is a discrete decision identity extracted from a fixed engine run.

this document is written so a pax-embedded agent can implement a first working slice without prior context.

---

## 1) core object

we study a decision-valued map:

**f : R → D**

- **snapshot**: a frozen slice of the world at some time window
- **representation (R)**: a deterministic encoding of that snapshot (kernels, thresholds, aggregation rules, graph weight policies)
- **engine**: a fixed solver or simulator that consumes the representation
- **decision (D)**: a discrete identity extracted from engine output, using a declared equivalence policy

the system exists to make the mapping **queryable**, **replayable**, and **auditable**.

---

## 2) invariants and design rules

### invariants
1. reproducibility: identical inputs must yield identical ids
2. auditability: every mapping links to versioned artifacts and policies
3. separation: representation parameters are distinct from tuning parameters
4. identity stability: decision identity is defined by policy, not raw output

### naming rule
- pax is always lowercase when referenced as the modeling system

---

## 3) identifiers and hashing

all identifiers are content-addressed hashes over canonical json.

### canonical json rules
- keys sorted
- no whitespace
- arrays preserve order
- floats serialized as strings
- version strings always included

hash function: `sha256(canonical_json_bytes)`

id format: `<prefix>_<sha256[:16]>`

prefixes:
- snap_
- repr_
- run_
- dec_
- exp_

---

## 4) data model

### snapshots
stores frozen inputs.

fields:
- snapshot_id (pk)
- created_at
- time_window_start
- time_window_end
- provenance_json
- artifact_manifest_json
- snapshot_version
- notes

### representations
stores deterministic encodings of snapshots.

fields:
- representation_id (pk)
- snapshot_id (fk)
- representation_spec_json
- representation_namespace
- factory_version
- artifact_uri
- artifact_sha256
- status
- error_text

### engine_runs
records fixed-engine executions.

fields:
- engine_run_id (pk)
- representation_id (fk)
- engine_name
- engine_version
- engine_config_json
- runtime_ms
- raw_output_uri
- raw_output_sha256
- status
- error_text

### decisions
stores discrete identities extracted from outputs.

fields:
- decision_id (pk)
- decision_type
- equivalence_policy_version
- decision_signature_json
- decision_payload_json

### f_map
materializes **f : R → D**.

fields:
- representation_id (fk)
- engine_run_id (fk)
- decision_id (fk)
- aux_metrics_json

---

## 5) directory layout

```
decisiondb/
  core/
    canonical_json.py
    ids.py
    schemas.py
  store/
    db.py
    migrate.py
  repr/
    factory.py
  engine/
    adapter.py
  decision/
    extract.py
    equivalence.py
  sweeps/
    plan.py
    run.py
  experiments/
    exp0001_pax_route_sweep/
      experiment.json
      run_experiment.py
  artifacts/
    snapshots/
    representations/
    runs/
    decisions/
```

---

## 6) minimal first experiment

**goal:** produce a nontrivial f_map with at least two distinct decision identities.

experiment name: `exp0001_pax_route_sweep`

### experiment.json (minimal)
```
{
  "experiment_version": "1",
  "name": "exp0001_pax_route_sweep",
  "snapshot": {
    "time_window_start": "2026-01-01T00:00:00Z",
    "time_window_end": "2026-01-01T00:10:00Z"
  },
  "representation_factory": {
    "family": "graph_weight_policy",
    "factory_version": "git:HEAD"
  },
  "sweep": {
    "grid": {
      "params": { "lambda": ["0.0", "1.0", "2.0"] }
    }
  },
  "engine": {
    "engine_name": "pax_router",
    "engine_version": "git:HEAD"
  },
  "decision": {
    "decision_type": "route",
    "equivalence_policy_version": "route_eq_v1"
  }
}
```

### success criteria
- at least two distinct decision_ids appear
- reruns produce identical ids and mappings

---

## 7) non-goals for v0

- no training
- no gradients
- no hyperparameter optimization
- no continuous ingestion

each update to the world becomes a new snapshot.

---

## 8) summary

decisiondb makes representation-induced decision changes visible.

it is not an optimizer.

it is an audit layer for discrete identity.

