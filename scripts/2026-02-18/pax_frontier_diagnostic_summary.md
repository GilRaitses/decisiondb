# 1. Executive Summary (<= 300 words)

This diagnostic asks whether observed route differences in pax A* are caused by premature frontier pruning or frontier collapse, rather than map representation alone. The target was the paper pathfinding implementation and its heuristic conditions.

Instrumentation was added at expansion-step granularity. For each step, the trace records the expanded node, g, h, f, frontier size before and after expansion, nodes added to open set, nodes skipped or pruned, closed-set updates, stale heap skips, and best candidate path state. These records were written to `frontier_trace.jsonl`.

Three synchronized GIFs were generated to visualize frontier dynamics:

- baseline distance-only condition
- paper heuristic condition with stress-weighted cost and distance-only heuristic (alpha 0.033)
- stress-weighted diagnostic condition with stronger stress emphasis (alpha 0.099 and stress-influenced heuristic term)

Each GIF shows open set, closed set, expanded node, and time progression at matched expansion indices.

Key findings for the tested OD pair (Grand Central to Carnegie Hall):

- all three variants found a path
- divergence from baseline search order begins at step 2 for weighted variants
- exploration volume increases in weighted variants (57 baseline, 418 paper, 439 stress-weighted)
- no frontier collapse was observed under the configured collapse criterion
- baseline-path nodes were not permanently pruned before expansion in weighted variants

Conclusion for this run: premature pruning of admissible-path nodes was not observed. Differences are attributable to search trajectory changes induced by objective weighting and heuristic condition, not to observed frontier collapse.

# 2. A* Implementation Audit

Audited implementation: `docs/deliverables/code/run_pathfinding.py`, with cross-checks against `src/pax/pathfinding/astar.py` and `src/pax/pathfinding/learned_heuristic.py`.

Heuristic variants examined:

- distance-only baseline (`alpha=0.0`)
- stress-aware raw (`alpha>0` with raw stress)
- stress-aware regularized (`alpha>0` with topology-adjusted stress)

Admissibility and consistency:

- implemented h is Manhattan distance only in the deliverable code path
- g includes distance plus nonnegative stress penalty when alpha is positive
- under standard lower-bound assumptions, this is admissible for the weighted objective
- consistency can fail if graph edge geometry and Manhattan lower-bound assumptions do not hold

Open and closed set handling:

- open set is a heap with duplicate node entries allowed
- closed set is final for each node once popped
- stale heap entries are skipped at pop time

Reopening behavior:

- no node reopening is implemented after closed-set insertion

Pruning and early exit:

- pruning occurs via closed-set filtering and no-better-g rejection
- immediate return on first goal pop
- no explicit frontier-size or f-threshold cutoff

Potential premature-pruning risk factors:

- no-reopen closed-set policy under any consistency violation
- immediate goal-pop termination

# 3. Instrumentation Details

Frontier element definition:

- a frontier element is a heap entry `(f, node)` that has not yet been closed

Per-step logged metrics:

- `variant`, `step`, `expanded_node`
- `g`, `h`, `f`
- `frontier_size_before_pop`, `frontier_size_after_expansion`
- `open_nodes_count`, `open_nodes`
- `nodes_added_to_open` with parent and g/h/f
- `nodes_removed_or_pruned` with reason and cost context when relevant
- `closed_set_added`, `closed_set_size`, `closed_nodes`
- `best_path_candidate`
- `stale_open_entries_skipped_since_last_expansion`
- `goal_reached`

Pruning event detection:

- `neighbor_in_closed_set`: neighbor skipped because it is already closed
- `no_better_g`: neighbor candidate rejected because tentative g is not better
- stale frontier entries are counted separately as skipped-at-pop events

Trace and visualization synchronization:

- each expansion record carries a monotonic `step`
- GIF frames are indexed by expansion step
- all panels are synchronized by using the maximum step count and holding the last state for shorter traces
- final synchronized output: 439 frames per panel

# 4. Visualization Artifacts

## `gifs/panel_a_baseline.gif`

- Condition: baseline distance-only
- Intended view: reference frontier growth and convergence under distance objective
- Observable behavior: compact search, 57 expansions, direct convergence, no collapse signature

## `gifs/panel_b_paper_heuristic.gif`

- Condition: paper heuristic setup (alpha 0.033, distance-only h)
- Intended view: how paper objective reshapes frontier and expansion order
- Observable behavior: divergence from baseline by step 2, broader exploration, 418 expansions, no visible frontier collapse

## `gifs/panel_c_stress_weighted.gif`

- Condition: stress-emphasized diagnostic variant (alpha 0.099, stress-influenced h term)
- Intended view: whether stronger stress weighting induces early elimination or collapse
- Observable behavior: early divergence by step 2, highest exploration count (439), no visible frontier collapse

Visibility of collapse or early pruning:

- no panel shows sustained frontier collapse under the configured criterion
- prune events are present in traces, but admissible baseline-path nodes are still expanded later

# 5. Comparative Interpretation

Search trajectories diverge at step 2 in both weighted variants relative to baseline.

Early pruning of admissible paths:

- prune events on baseline-path nodes are recorded in weighted variants
- these events are mostly closed-set filtering and no-better-g rejections after competing expansions
- no baseline-path node was permanently excluded before expansion in the tested run

Failure before optimal expansion:

- no variant failed to find a path
- there is no evidence in this run that route failure occurred before candidate-path expansion

Search-level versus representation-level signal:

- all variants share the same graph representation
- observed differences are generated by search objective and heuristic condition
- evidence in this diagnostic supports search-trajectory divergence, not representation-level blockage, for this OD pair

# 6. Relationship to Original Paper Claims

Strengthened:

- the diagnostic confirms that path differences can be examined at frontier level, not only by final route outputs
- the weighted objective materially changes expansion behavior, consistent with the paper's stress-aware routing framing

Requires clarification or revision:

- the deliverable header text suggests a stress-augmented heuristic formula, while executed code in the audited path uses distance-only h
- frontier-level evidence should accompany route-level claims when discussing pruning or admissibility concerns

Attribution of observed instability:

- in this tested route, instability manifests as large differences in expansion volume and ordering
- this is attributable to heuristic and cost design choices in search mechanics
- this diagnostic did not produce evidence that representation alone caused the observed differences

# 7. Limitations and Open Questions

Not resolved:

- behavior across multiple OD pairs, including known failure cases outside this tested route
- guarantees about admissibility and consistency over the full graph and all parameterizations
- sensitivity of conclusions to collapse-threshold definition

Ambiguities that remain:

- whether other route scenarios exhibit true pre-evaluation elimination of admissible alternatives
- whether no-reopen policy produces failures when heuristic consistency assumptions are stressed

Additional instrumentation needed for stronger external inference:

- full-batch OD replay traces, including failed-route cases
- explicit per-node first-seen versus first-expanded timing across variants
- counterfactual logging of closed-node improvements that would require reopening
- run-level comparators that align identical OD sets and report pruning outcomes by node class

# 8. Repository Integration Notes

Artifact locations in this repo:

- summary file: `scripts/2026-02-18/pax_frontier_diagnostic_summary.md`
- audit: `scripts/2026-02-18/astar_audit.md`
- trace: `scripts/2026-02-18/frontier_trace.jsonl`
- diagnosis: `scripts/2026-02-18/frontier_pruning_diagnosis.md`
- GIFs: `scripts/2026-02-18/gifs/panel_a_baseline.gif`, `panel_b_paper_heuristic.gif`, `panel_c_stress_weighted.gif`

Public page update:

- reviewer page: `scripts/2026-02-18/index.html`
- it embeds all three GIF panels with captions and a concise findings summary

Recommended reading order for external review:

1. `pax_frontier_diagnostic_summary.md`
2. `index.html`
3. `frontier_pruning_diagnosis.md`
4. `astar_audit.md`
5. `frontier_trace.jsonl` for step-level evidence
