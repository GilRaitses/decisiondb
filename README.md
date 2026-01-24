# DecisionDB

DecisionDB is a diagnostic infrastructure for tracking how discrete outcome identities depend on representational choices within complex analytical pipelines. Many systems exhibit apparent stability across inputs while remaining sensitive to subtle changes in encoding, preprocessing, or structural description. DecisionDB makes these dependencies explicit by recording outcome identities across controlled representational variation, enabling empirical assessment of persistence, boundary formation, and fracture without introducing new models, performance targets, or theoretical claims.

---

## decisiondb system design

This document defines a minimal, reproducible system for logging and analyzing decision-valued maps of the form **f : R → D**, where **R** is a family of representations constructed over a fixed snapshot and **D** is a discrete decision identity extracted from a fixed engine run.

---

## 1) core object

DecisionDB studies a decision-valued map:

**f : R → D**

where:

- **snapshot** is a frozen slice of the world over a declared time window
- **representation (R)** is a deterministic encoding of that snapshot, such as kernels, thresholds, aggregation rules, or graph weight policies
- **engine** is a fixed solver or simulator that consumes the representation
- **decision (D)** is a discrete identity extracted from engine output using a declared equivalence policy

The system exists to make this mapping queryable, replayable, and auditable.

---

## 2) invariants and design rules

### invariants

1. reproducibility  
identical inputs must yield identical identifiers

2. auditability  
every mapping must link to versioned artifacts, policies, and configuration state

3. separation  
representation parameters are distinct from tuning or optimization parameters

4. identity stability  
decision identity is defined by equivalence policy rather than raw engine output

### naming rule

- pax is always lowercase when referenced as the modeling system

---

## 3) identifiers and hashing

All identifiers in DecisionDB are content-addressed hashes computed over canonical json.

### canonical json rules

- keys are sorted
- no whitespace is permitted
- arrays preserve order
- floating-point values are serialized as strings
- version strings are always included

Hash function:

```
sha256(canonical_json_bytes)
```

Identifier format:

```
<prefix>_<sha256[:16]>
```

Prefixes:

- snap_
- repr_
- run_
- dec_
- exp_

---

## 4) data model

### snapshots

Stores frozen inputs.

Fields:

- snapshot_id (pk)
- created_at
- time_window_start
- time_window_end
- provenance_json
- artifact_manifest_json
- snapshot_version
- notes

### representations

Stores deterministic encodings of snapshots.

Fields:

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

Records fixed-engine executions.

Fields:

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

Stores discrete identities extracted from engine outputs.

Fields:

- decision_id (pk)
- decision_type
- equivalence_policy_version
- decision_signature_json
- decision_payload_json

### f_map

Materializes the mapping **f : R → D**.

Fields:

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

**goal**  
Produce a nontrivial **f_map** with at least two distinct decision identities.

Experiment name:

```
exp0001_pax_route_sweep
```

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

- at least two distinct decision_id values appear
- repeated runs produce identical identifiers and mappings

---

## 7) non-goals for v0

DecisionDB explicitly does not include:

- training procedures
- gradient computation
- hyperparameter optimization
- continuous ingestion or streaming updates

Each update to the world is represented as a new snapshot.

---

## 8) summary

DecisionDB makes representation-induced changes in discrete outcomes visible.

It does not optimize outcomes.

It provides an audit layer for discrete identity under representational variation.
 