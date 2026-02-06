# Figure 4: Boundary and Fracture Localization

## Decision identity definition
Decision identity is the route node sequence produced by the engine. Two engine outputs share the same decision identity if and only if their canonicalized route node arrays produce the same SHA-256 hash.

## Representation axes
Derived from the sweep in Figure 2:
- `neighbor_weight` axis: values 0.5 and 1.0 (no boundary observed)
- `second_order_weight` axis: values 0.25 and 0.5 (boundary observed between these values)

## Equivalence rule
Policy `pol_d8da3e00e9584eb1` (version 1.0.0). Type: exact. Hash source: `route.nodes`. Canonicalization: `json_sorted_keys_utf8`. Match rule: `sha256_equality`.

## Stability criterion
A boundary is identified where decision identity changes between adjacent representation parameter values. In the second_order_weight sweep, route_changed = true and edge_order_changed = true between values 0.25 and 0.5, indicating a boundary. In the neighbor_weight sweep, route_changed = false, indicating no boundary.

## Sampling method
Derived from Figure 2 sweep results. Boundaries are located between adjacent sampled parameter values. No interpolation or curve fitting.

## Non-claims disclaimer
This figure makes no performance claims, optimization claims, or learning claims. It marks observed loci where decision identity changes under representation variation with fixed data and fixed engine.
