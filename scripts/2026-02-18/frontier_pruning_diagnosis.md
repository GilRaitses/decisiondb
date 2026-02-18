# Frontier pruning diagnosis

## Route and evidence basis

- OD pair: Grand Central to Carnegie Hall
- Baseline path nodes: 18
- Baseline explored nodes: 57

## Variant comparison

| Variant | Path found | Nodes explored | First divergence step | Frontier peak | Collapse step |
| --- | --- | ---: | ---: | ---: | ---: |
| Panel A baseline | True | 57 |  | 146 |  |
| Panel B paper heuristic | True | 418 | 2 | 98 |  |
| Panel C stress-weighted heuristic | True | 439 | 2 | 87 |  |

## 1) Where admissible-path nodes were pruned

### Panel B paper heuristic

- Recorded 172 prune events on baseline-path nodes.
- Sample events: step 2 node 418 (neighbor_in_closed_set), step 3 node 11 (neighbor_in_closed_set), step 3 node 418 (neighbor_in_closed_set), step 4 node 11 (neighbor_in_closed_set), step 4 node 418 (neighbor_in_closed_set), step 5 node 418 (neighbor_in_closed_set), step 6 node 11 (neighbor_in_closed_set), step 6 node 418 (neighbor_in_closed_set)
- No baseline-path node was permanently pruned before any expansion.

### Panel C stress-weighted heuristic

- Recorded 178 prune events on baseline-path nodes.
- Sample events: step 2 node 418 (neighbor_in_closed_set), step 3 node 418 (neighbor_in_closed_set), step 4 node 11 (neighbor_in_closed_set), step 4 node 418 (neighbor_in_closed_set), step 5 node 11 (neighbor_in_closed_set), step 5 node 418 (neighbor_in_closed_set), step 7 node 11 (neighbor_in_closed_set), step 7 node 418 (neighbor_in_closed_set)
- No baseline-path node was permanently pruned before any expansion.

Interpretation:

- Prune events occur as normal closed-set filtering and no-better-g rejection.
- In this run, baseline-path nodes were still expanded later, so there is no evidence that admissible candidates were eliminated before evaluation.

## 2) Whether pruning occurred before sufficient exploration

- Panel B paper heuristic explored 418 nodes.
  - Frontier did not collapse below the 10 percent peak threshold.
- Panel C stress-weighted heuristic explored 439 nodes.
  - Frontier did not collapse below the 10 percent peak threshold.

Interpretation:

- Exploration volume increased substantially in weighted variants, and frontier collapse was not observed under the configured collapse criterion.
- The traces do not show premature frontier exhaustion.

## 3) Whether failures differ across heuristic variants

- All variants found a path.
- Search order diverged early (step 2) for both weighted variants.
- Weighted variants had much larger expansion counts: baseline 57, paper 418, stress-weighted 439.
- Panel C did not fail, but it increased search effort relative to Panel B.

## 4) Search-level versus representation-level instability

- Differences are driven by search policy inputs (cost shaping and heuristic weighting), because all variants use the same graph representation.
- For this diagnostic run, evidence points to search-level divergence and objective reweighting, not representation-level blockage.
- No run provided evidence of admissible-route removal before node evaluation.

