# Phase 2 and Phase 3 Pre-Flight Blueprint

This document defines the pre-scope and structural constraints for Phase 2 and Phase 3.
Its purpose is to shape both phases so that Phase 4 becomes necessary rather than optional.

The guiding principle is that degradation under reuse is expected.
Neither phase should claim robustness, generality, or completeness.

---

## Shared Structural Requirement

Both phases treat erosion of meaning under reuse as a structural outcome.
Reuse is modeled as projection of an output into a new situation without reinstating the conditions that produced it.

Each phase must leave a principled unresolved tension.

---

## Phase 2 Pre-Scope: Theory Paper

### Purpose
Define what must remain conserved for an output to remain meaningful across contexts,
without committing to mechanisms, architectures, or metrics.

### Allowed Claims
- Outputs are situated compressions that stand in for specific situations.
- Each output reflects alignment among data, goals, and tolerances.
- Reuse introduces a projection into a new situation.
- Meaning erodes when original constraints are not reinstated.
- Certain invariants must hold for meaning to persist.

### Explicit Non-Claims
- No mechanisms are proposed.
- No architectures are described.
- No enforcement strategies are introduced.
- No empirical evaluation is performed.

### Required Tension at End
We can specify necessary conservation conditions,
but we do not yet know how they behave when instantiated in real systems.

This tension hands off directly to Phase 3.

---

## Phase 3 Pre-Scope: Benchmark / Instantiation Paper

### Purpose
Operationalize Phase 2 invariants in a narrow setting
to demonstrate controlled erosion under reuse.

### Allowed Claims
- Phase 2 invariants can be instantiated in specific systems.
- Outputs reused without reinstating constraints exhibit measurable erosion.
- Erosion manifests as loss of interpretability, trust, or evaluability.
- Different systems can fail in structurally similar ways.

### Explicit Non-Claims
- No fixes or repairs are proposed.
- No calibration is introduced.
- No optimization is performed.
- No system is claimed to be representative.

### Measurement Focus
- Track degradation of meaning rather than accuracy.
- Observe slow, structural failure rather than edge cases.
- Emphasize reproducible erosion patterns.

### Required Tension at End
We can observe erosion systematically,
but we lack a principled method for restoring coherence when assumptions shift.

This tension opens Phase 4.

---

## Phase Alignment Check

Phase 2 ends by showing that reuse without constraints must fail in principle.
Phase 3 ends by showing that reuse without constraints does fail in practice.

If both conditions are met, Phase 4 is structurally unavoidable.

---

## Phase 4 Dependency Note

Phase 4 is the first phase permitted to address:
- Calibration
- Mechanism
- Causal interpretation
- Restorative structure

These are explicitly out of scope for Phase 2 and Phase 3.

---

## Design Reminder

Do not retrofit inevitability.
Let inevitability emerge from unresolved structure.

---

## Phase 1 Revision Notes (Backward Alignment)

Phase 1 should be revised so that its conclusion and discussion explicitly surface the inevitability structure that Phases 2 and 3 rely on, without advancing any new formal claims.

The Phase 1 manuscript already establishes decision-valued maps as a diagnostic object. Revisions should emphasize that these maps do not merely reveal sensitivity to representational choice, but expose a structural condition: discrete outcome identities are only interpretable relative to the constraints under which they were produced.

The conclusion should frame representational sweeps as an early signal of a more general phenomenon: outputs persist as artifacts even when the situational assumptions that stabilized them are no longer present. Phase 1 should stop short of theorizing this phenomenon, but should name it as an open structural problem rather than a tooling limitation.

Language in the discussion may be adjusted to highlight that persistence, boundary formation, and fracture are not anomalies of specific systems, but expected consequences of reuse under shifted conditions. This sets up the Phase 2 move from diagnostic observation to invariant characterization.

Phase 1 should avoid introducing any notion of restoration, calibration, or repair. Instead, it should close by stating that while decision-valued maps make erosion observable, they do not explain what must be conserved for meaning to persist across contexts. That unanswered question is the handoff to Phase 2.