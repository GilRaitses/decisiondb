# A* audit for pax term-paper deliverable code

## Scope

Primary audited implementation:

- `docs/deliverables/code/run_pathfinding.py` in `GilRaitses/pax` (term-paper deliverables bundle).

Cross-reference implementation for parity checks:

- `src/pax/pathfinding/astar.py`
- `src/pax/pathfinding/learned_heuristic.py`

## Heuristic variants used in the paper workflow

The deliverables pipeline (`run_pathfinding`) uses one A* core (`astar_with_stress`) under different stress configurations.

| Variant ID | How it is invoked | g-cost definition | h-cost definition | Notes |
| --- | --- | --- | --- | --- |
| V1 baseline | `run_pathfinding(..., alpha=0.0)` | Distance only (`distance + 0*stress`) | Manhattan distance to goal | Distance-first baseline |
| V2 stress-aware raw | `astar_with_stress(..., alpha>0, stress_scores=raw)` | `distance + alpha*edge_stress` | Manhattan distance to goal | Uses raw camera-derived stress |
| V3 stress-aware regularized | `astar_with_stress(..., alpha>0, stress_scores=apply_topology_adjustments(...))` | `distance + alpha*edge_stress` | Manhattan distance to goal | Uses ridge and basin stress adjustments from `apply_topology_adjustments` |

Important mismatch:

- The file header text says heuristic is `manhattan + alpha*accumulated_stress`.
- The actual code uses `new_f = new_g + h` where `h` is only Manhattan distance.

## Admissibility and consistency assessment

### V1 baseline

- Heuristic: Manhattan distance in meters from node coordinates.
- If edge distance is metric distance on the road graph, this is admissible and consistent for distance cost.

### V2 and V3 stress-aware variants

- Heuristic remains Manhattan distance only.
- g-cost adds non-negative stress term (`alpha*stress`).
- Since h ignores stress, h does not overestimate total objective if Manhattan distance is a lower bound on remaining distance.
- Under that condition, h is admissible for the stress-augmented objective and usually consistent.

### Risk caveat

- If graph edge weights violate metric assumptions relative to the Manhattan coordinate transform, consistency can fail.
- The implementation does not include closed-node reopening, so inconsistency would directly cause pruning risk.

## Open set frontier management

Observed in `astar_with_stress`:

- `open_set` is a binary heap (`heapq`).
- Entries are full `Node` snapshots with full path state.
- Duplicate node IDs are allowed in the heap. There is no per-node best-g map in the frontier.
- Frontier shrink behavior depends on closed-set filtering at pop time.

Implication:

- Heap can contain stale worse entries for the same node.
- Stale entries are skipped only after pop if node already moved to closed.

## Closed set policy

- `closed_set` stores expanded node IDs.
- A node is inserted into closed immediately after pop and before neighbor expansion.
- Once a node is in closed, all future attempts to reach it are skipped.

## Node reopening behavior

- Reopening is **not allowed**.
- There is no logic to remove a closed node when a better g-cost is found later.
- This is acceptable only if heuristic plus edge costs satisfy consistency conditions.

## Pruning rules, thresholds, and early exits

Explicit pruning and exit behavior:

1. **Closed-set prune**
   - Skip popped nodes already in closed.
   - Skip neighbor generation if neighbor already in closed.
2. **Goal early exit**
   - Return immediately on first goal pop.
3. **No numeric cutoffs**
   - No frontier size cap.
   - No f-threshold prune.
   - No depth cutoff.

The only pruning mechanism is closed-set irreversibility plus stale heap suppression.

## Learned or engineered heuristic components beyond raw stress

In the term-paper deliverable code:

- `apply_topology_adjustments` injects engineered stress transformations:
  - Ridge nodes: stress floor to `>= 0.8`
  - Basin nodes: stress cap to `<= 0.4`
- These are learned or calibrated at a policy level, but are applied to **cost field values**, not to heuristic `h`.

In the larger pax codebase (`learned_heuristic.py`):

- Additional engineered adjustments include corridor discounts, theater boosts, and avenue-level ridge or basin rules.
- Even there, heuristic remains distance-only in `_heuristic_with_stress`.

## Frontier-collapse relevance summary

For this code path, premature elimination of viable alternatives can only come from:

1. Closed-set no-reopen policy under any inconsistency in effective heuristic-cost pairing.
2. Strong stress-weighted g-cost shaping that causes one branch to dominate before alternatives are expanded.
3. Immediate goal return on first goal pop.

No explicit hard prune threshold exists. Collapse would therefore be search-policy driven, not threshold driven.
