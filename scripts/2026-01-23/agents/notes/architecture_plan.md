# Formal Architecture and Implementation Plan

The following minimal components must exist for a coding agent to run Figure 2 (primary representational sweep) tomorrow. Each component is expressed as a testable precondition.

| Component | Description | Precondition (testable) |
|-----------|-------------|-------------------------|
| Snapshot storage | Table `snapshots` | Row must contain `snapshot_id` computed from SHA-256 of canonical JSON of snapshot content; must be immutable. |
| Representation generator | Module `representation_mgr` | Must accept a factory version and a parameter grid, produce deterministic representation JSON, and return `rep_id` from SHA-256 of its canonical JSON. |
| Engine execution | Module `engine_runner` | Must take `rep_id`, execute the fixed engine (engine name, version, config) producing raw output, store `raw_output_hash` (SHA-256 of canonical JSON), and record `run_id`. |
| Decision extractor | Module `decision_extractor` | Must take `raw_output_hash` and an equivalence policy version, apply policy, return `decision_id` (SHA-256 of canonical JSON of decision identity). |
| Decision map | Table `decision_map` | Row must link `rep_id` to `decision_id` and store `map_id` computed from SHA-256 of a tuple (`snapshot_id`, `rep_id`, `engine_name`, `engine_version`, `eq_policy_id`). |
| Metadata tables | Tables `representations`, `engine_runs`, `decisions` | Must contain the fields described above, each row keyed by its respective ID. |
| Canonicalization rules | Specification of canonical JSON | Sorting keys, preserving array order, no whitespace, floats as strings, version field included; must be deterministic. |
| Hash prefixing | ID construction | ID = `<type prefix><first 16 hex chars of SHA-256>`. |
| Deterministic sweep orchestrator | Script `sweep_orchestrator` | Must iterate over all parameter tuples in the declared grid, call `representation_mgr`, `engine_runner`, `decision_extractor`, and insert rows into all tables. |
| Replay verifier | Script `replay_verifier` | Must re-run the same grid with identical parameters, check that all content hashes and decision IDs match the original run. |

All modules may be named generically; no novel computational or learning components are required.
