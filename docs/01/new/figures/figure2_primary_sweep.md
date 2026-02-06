# Figure 2: Primary Representational Sweep

## Decision identity definition
Decision identity is the route node sequence produced by the engine. Two engine outputs share the same decision identity if and only if their canonicalized route node arrays produce the same SHA-256 hash.

## Representation axes
Two representation parameters are swept independently:
- `neighbor_weight`: tested at values 0.5 and 1.0 (second_order_weight fixed at 0.25)
- `second_order_weight`: tested at values 0.25 and 0.5 (neighbor_weight fixed at 0.5)

Each parameter value defines a point in the representation sweep.

## Equivalence rule
Policy `pol_d8da3e00e9584eb1` (version 1.0.0). Type: exact. Hash source: `route.nodes`. Canonicalization: `json_sorted_keys_utf8`. Match rule: `sha256_equality`.

## Stability criterion
Decision identity is considered stable (persistent) when two or more representation parameter values produce the same decision identity label under the fixed equivalence policy.

## Sampling method
Exhaustive evaluation at declared parameter values. Four total engine evaluations (two per sweep). No interpolation or extrapolation.

## Non-claims disclaimer
This figure makes no performance claims, optimization claims, or learning claims. It displays observed decision identities under representation variation with fixed data and fixed engine.
