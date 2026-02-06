# Figure 3: Identity Persistence Regions

## Decision identity definition
Decision identity is the route node sequence produced by the engine. Two engine outputs share the same decision identity if and only if their canonicalized route node arrays produce the same SHA-256 hash.

## Representation axes
Derived from the sweep in Figure 2:
- `neighbor_weight` axis: values 0.5 and 1.0
- `second_order_weight` axis: values 0.25 and 0.5

## Equivalence rule
Policy `pol_d8da3e00e9584eb1` (version 1.0.0). Type: exact. Hash source: `route.nodes`. Canonicalization: `json_sorted_keys_utf8`. Match rule: `sha256_equality`.

## Stability criterion
A persistence region is a contiguous range of representation parameter values over which decision identity remains unchanged. The neighbor_weight sweep spans a single persistence region (Decision A at both 0.5 and 1.0). The second_order_weight sweep spans two regions (Decision A at 0.25, Decision B at 0.5).

## Sampling method
Derived from Figure 2 sweep results. No additional engine evaluations. No interpolation.

## Non-claims disclaimer
This figure makes no performance claims, optimization claims, or learning claims. It shows observed regions of identity persistence under representation variation with fixed data and fixed engine.
