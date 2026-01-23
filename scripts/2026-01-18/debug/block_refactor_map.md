## Block aggregation refactor map

### Block abstraction (Phase 2)

Authoritative module:
- `src/pax/stress/block_stress.py`
  - `BlockStressModel.from_route` consumes an `IntersectionStressModel` and a route node list.
  - Aggregation rule is explicit (default `block_sum`) and recorded in diagnostics.

Inputs
- Intersection diagnostics and scalars from `IntersectionStressModel`.
- Route node sequence from a planner output.

Outputs
- Block diagnostics payload containing:
  - block_id
  - intersection_ids
  - aggregation_rule
  - intersection_scalars
  - block_scalar
  - pointer to intersection diagnostics

Integration points
- `scripts/2026-01-16/run_normalized_stress_activation.py`
  - writes `pearson_block_stress_diagnostics.json`
- `scripts/2026-01-16/run_neighbor_weight_activated.py`
  - writes `pearson_neighbor_weight_activated_block_diagnostics.json`
- `scripts/2026-01-16/run_second_order_weight_activated.py`
  - writes `pearson_second_order_weight_activated_block_diagnostics.json`

Non-goals
- Blocks do not reweight or normalize intersection scalars.
- Routing does not consume block scalars in Phase 2.
