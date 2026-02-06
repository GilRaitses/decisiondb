# Figure 5: Reproducibility Replay Verification

## Decision identity definition
Decision identity is the route node sequence produced by the engine. Two engine outputs share the same decision identity if and only if their canonicalized route node arrays produce the same SHA-256 hash. The verified decision is `dec_e28092c4dc33b8f1`.

## Representation axes
Not applicable. This figure verifies replay determinism for a single persisted decision record, not a sweep across representation parameters.

## Equivalence rule
Policy `pol_d8da3e00e9584eb1` (version 1.0.0). Type: exact. Hash source: `route.nodes`. Canonicalization: `json_sorted_keys_utf8`. Match rule: `sha256_equality`. The policy identifier is recomputed during replay and compared against the persisted value.

## Stability criterion
Replay passes if and only if all recomputed identifiers (policy ID, payload hash, decision ID) match the persisted values exactly, and no database rows are modified during verification.

## Sampling method
Single decision record verified via read-only replay. Raw engine output loaded from stored URI. Policy identifier, payload hash, and decision identifier recomputed independently and compared against persisted manifest.

## Non-claims disclaimer
This figure makes no performance claims, optimization claims, or learning claims. It reports a deterministic replay verification confirming that persisted decision identifiers are recoverable from stored artifacts under fixed policy.
