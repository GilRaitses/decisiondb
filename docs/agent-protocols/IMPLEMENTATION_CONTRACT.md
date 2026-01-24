# DecisionDB Implementation Contract (Code Unlock Gate)

**Status:** REQUIRED before any coding agent runs sweeps or generates figures  
**Scope:** DecisionDB empirical sweeps, figure generation, and any code that populates the DecisionDB store

This contract defines the minimum implementation commitments that must exist before experimental execution is allowed. It prevents drift where empirical scripts silently redefine the manuscript object \( f : R \to D \).

---

## 0. Non-negotiable stance

DecisionDB is diagnostic infrastructure.

It does not train, optimize, adapt, improve outcomes, or introduce new decision procedures.

All empirical execution must preserve this stance.

---

## 1. Canonical object and locks

All experiments must instantiate the decision-valued map:

\[
f : R \to D
\]

- **snapshot:** a frozen slice of the world over a declared time window
- **representation (R):** a deterministic encoding of that snapshot defined by explicit structural choices
- **engine:** a fixed computational procedure consuming the representation
- **decision identity (D):** a discrete outcome extracted from engine output under a declared equivalence policy
- **equivalence policy:** the declared rule defining when two raw outputs correspond to the same decision identity

**Locks**
- snapshot is fixed during a sweep
- engine name, version, and config are fixed during a sweep
- equivalence policy ID is fixed during a sweep
- the representation family is the only locus of variation

---

## 2. Required repo artifacts (must exist before code execution)

### 2.1 Experiment registry file

A single registry enumerates all sweepable experiments.

**Required location**
- `decisiondb/experiments/experiment_registry.yaml`

**Required fields for each experiment**
- `exp_id`
- `purpose` (diagnostic only)
- `snapshot_ref` (points to a snapshot spec)
- `representation_family_ref` (points to a representation family spec)
- `engine_ref` (points to an engine lockfile)
- `equivalence_policy_ref` (points to a policy instantiation)
- `parameter_grid_ref` (points to a declared grid)
- `expected_artifacts` (list of tables and files produced)

No experiment may run unless it is present in the registry.

---

### 2.2 Snapshot specification

Each experiment references a snapshot spec, which must be immutable.

**Required location pattern**
- `decisiondb/snapshots/<SNAPSHOT_ID>/snapshot.yaml`

**Required fields**
- `snapshot_id`
- `time_window_start`
- `time_window_end`
- `provenance`
- `artifact_manifest`
- `snapshot_version`
- `notes` (optional)

**Rule**
- A changed snapshot is a new snapshot_id. No mutation in place.

---

### 2.3 Representation family specification

Each experiment references exactly one representation family.

**Required location pattern**
- `decisiondb/repr/families/<REP_FAMILY>/family.yaml`

**Required fields**
- `representation_family`
- `namespace`
- `factory_entrypoint` (module:function)
- `factory_version`
- `canonicalization_rules` (must match DecisionDB canonical JSON rules)
- `parameters` (declared parameter names with types)
- `grid_constraints` (allowed ranges, steps, enumerations)
- `artifact_emission` (what files are generated per representation and where)

**Determinism requirement**
- Given a snapshot and parameter tuple, the factory emits the same artifact bytes.

---

### 2.4 Engine lockfile

The engine must be pinned and replayable.

**Required location pattern**
- `decisiondb/engine/locks/<ENGINE_NAME>/<ENGINE_LOCK_ID>.yaml`

**Required fields**
- `engine_name`
- `engine_lock_id`
- `engine_version` (git SHA or immutable build ID)
- `engine_config_json` (canonical)
- `runtime_environment` (OS, interpreter, required binaries)
- `entrypoint`
- `notes` (optional)

**Rule**
- No sweep may run on `git:HEAD` for the engine. A pinned identifier is required.

---

### 2.5 Equivalence policy instantiation

The equivalence policy must be concrete, versioned, and referenced by ID.

**Required location pattern**
- `decisiondb/decision/equivalence_policies/<EQUIV_POLICY_ID>.yaml`

**Required fields**
- `equivalence_policy_id`
- `decision_type`
- `policy_level` (exact | corridor | semantic)
- `policy_definition` (explicit matching rule)
- `policy_version`
- `hash_inputs` (explicitly enumerated)
- `fallback_chain` (if any)
- `tests` (minimum test vectors)

**Rule**
- Decisions are defined by policy. The policy must exist before decisions are extracted.

---

### 2.6 Parameter grid declaration

The sweep grid must be declared and named.

**Required location pattern**
- `decisiondb/sweeps/grids/<GRID_ID>.yaml`

**Required fields**
- `grid_id`
- `parameters` (names matching the representation family)
- `grid_points` (explicit list) OR `grid_rules` (explicit generator rules)
- `adjacency_definition` (for boundary detection, if applicable)
- `sampling_method` (grid | random, but must be declared)

**Rule**
- “Reasonable choices” are not allowed at runtime. The grid is a declared object.

---

## 3. Required database readiness

The following tables must exist and match the documented schema:

- `snapshots`
- `representations`
- `engine_runs`
- `decisions`
- `f_map`

If derived tables are produced, they must be marked as derived and linked to source objects:

- `persistence_regions` (derived from `f_map`)
- `boundaries` / `fractures` (derived from `f_map`)
- `replay_verification` (derived from reruns)

---

## 4. Execution protocol constraints (hard)

All sweep execution must follow the protocol stages in the manuscript and README:

1. snapshot load
2. representation generation
3. engine run
4. decision extraction
5. map materialization

**Hard constraints**
- No adaptive loops
- No learning
- No hyperparameter tuning
- No selection of “best” outcomes
- No performance metrics in figures or tables intended for manuscript

---

## 5. Required outputs per experiment

For each `exp_id`, the run must produce:

### 5.1 Materialized map

- A populated `f_map` linking:
  - representation_id
  - engine_run_id
  - decision_id
  - aux_metrics_json (only diagnostics, no optimization metrics)

### 5.2 Reproducibility replay (if required by exp)

- A rerun with identical IDs
- A `replay_verification` artifact showing equality of:
  - representation hashes
  - run hashes
  - decision signatures

### 5.3 Figure-ready dataset export

Each figure must be produced from an explicit export artifact:

- `decisiondb/artifacts/exports/<EXP_ID>/<EXPORT_ID>.parquet` (or csv)
- plus a `export_manifest.yaml` containing:
  - exp_id
  - snapshot_id
  - representation_family
  - engine_lock_id
  - equivalence_policy_id
  - grid_id
  - date
  - git SHAs for decisiondb and any engine adapter

---

## 6. Unlock criteria (pass/fail checklist)

A coding agent is allowed to execute only when all items below are TRUE.

### 6.1 Artifacts exist
- [ ] experiment_registry.yaml exists and includes target exp_id
- [ ] snapshot spec exists for snapshot_ref
- [ ] representation family spec exists for representation_family_ref
- [ ] engine lockfile exists for engine_ref and is pinned (not HEAD)
- [ ] equivalence policy file exists for equivalence_policy_ref
- [ ] parameter grid file exists for parameter_grid_ref

### 6.2 Determinism and tests
- [ ] equivalence policy includes test vectors and tests pass locally
- [ ] representation factory determinism check exists and passes on 3 random grid points

### 6.3 Store readiness
- [ ] database migrations applied
- [ ] tables exist and match schema
- [ ] artifact storage paths are writable

### 6.4 Governance readiness
- [ ] pre-commit hook passes on the branch
- [ ] no forbidden claim phrases appear in staged manuscript or docs

If any item fails, code execution is not allowed.

---

## 7. Allowed and forbidden language in code and logs

**Allowed verbs**
- record, log, materialize, characterize, compare, replay, audit, extract, declare

**Forbidden verbs**
- optimize, learn, train, improve, outperform, enhance, decide, choose (as a normative act)

This language requirement applies to:
- CLI output
- log lines
- docstrings
- README updates
- figure captions

---

## 8. Sign-off

This contract is the gate that must be satisfied before empirical execution.

It exists to keep the implementation aligned with the manuscript’s diagnostic object \( f : R \to D \) and to prevent scope drift under deadline pressure.