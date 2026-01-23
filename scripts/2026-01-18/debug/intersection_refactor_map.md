## Intersection stress refactor map

### Prior stress pathways (pre-refactor)

1. `src/pax/pathfinding/learned_heuristic.py:_map_intersections_to_stress`
   - Street-based assignment, with IDW fallback and nearest-camera fallback.
   - Output: `self.intersection_stress` dict of node_id -> scalar.

2. `src/pax/scripts/voronoi_stress_scoring.py:calculate_weighted_stress`
   - Zone-based aggregation with neighbor and second-order contributions.
   - Output: weighted stress dict per point (base/neighbor/second-order totals).

3. `src/pax/stress/composite_stress.py:compute_intersection_stress`
   - IDW interpolation from camera stress values.

4. Script-level aggregation
   - `scripts/2026-01-16/run_*_activated.py` and related scripts computed intersection stress directly with zone logic.

### Refactor dispositions (phase 1)

Authoritative intersection stress object:
- `src/pax/stress/intersection_stress.py:IntersectionStressModel`
  - Owns scalar per intersection and structured diagnostics.
  - Produces route diagnostics (intersections + edges) with stress_path_id and stress_source_key.

Consolidated usage:
- Zone-driven aggregation now flows through `IntersectionStressModel.from_voronoi_zones`.
- Precomputed intersection dictionaries are wrapped via `IntersectionStressModel.from_precomputed`.

Routing integration:
- `src/pax/pathfinding/learned_heuristic.py` now wraps its `intersection_stress` in `IntersectionStressModel`
  for diagnostics without changing the scalar behavior.

Diagnostics and sidecars:
- `scripts/2026-01-16/run_normalized_stress_activation.py` writes diagnostics sidecar.
- `scripts/2026-01-16/run_neighbor_weight_activated.py` writes diagnostics sidecar.
- `scripts/2026-01-16/run_second_order_weight_activated.py` writes diagnostics sidecar.
- `scripts/2026-01-16/run_*` scripts also emit block-level diagnostics sidecars (Phase 2).

### Stress key selection

Canonical key selection:
- `src/pax/stress/stress_keys.py:pick_stress_key`
- `src/pax/stress/stress_reader.py:resolve_camera_stress_map`

These functions are the only authorized selectors for stress keys in planning and perturbation scripts.

