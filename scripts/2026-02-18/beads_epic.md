# Beads epic: pax frontier dynamics diagnostics

Beads tracker:

- Epic: `decisiondb-6mc`
- Phase 1 Discovery: `decisiondb-6mc.1`
- Phase 2 Construction: `decisiondb-6mc.2`
- Phase 3 Synthesis: `decisiondb-6mc.3`
- Phase 4 Analysis: `decisiondb-6mc.4`
- Phase 5 Publication: `decisiondb-6mc.5`

## Phase declarations

### Phase 1 Discovery

- Goal: Audit term-paper A* code and heuristic variants.
- Artifact: `astar_audit.md`
- Verification:
  - Heuristic definitions listed for each variant.
  - Open and closed set behavior documented.
  - Reopening and pruning behavior documented.

### Phase 2 Construction

- Goal: Add toggleable frontier instrumentation with no decision-rule changes.
- Artifact: `frontier_trace.jsonl`
- Verification:
  - One trace record per expansion step.
  - Includes expanded node, g/h/f, frontier size, open additions, prunes, closed changes.

### Phase 3 Synthesis

- Goal: Visualize frontier behavior under three heuristic conditions.
- Artifacts:
  - `gifs/panel_a_baseline.gif`
  - `gifs/panel_b_paper_heuristic.gif`
  - `gifs/panel_c_stress_weighted.gif`
- Verification:
  - GIFs share synchronized frame counts.
  - Each frame shows open, closed, expanded node, and step progression.

### Phase 4 Analysis

- Goal: Diagnose whether admissible-path nodes are pruned before evaluation.
- Artifact: `frontier_pruning_diagnosis.md`
- Verification:
  - Findings reference trace step indices.
  - Variant differences are search-process observations, not speculation.

### Phase 5 Publication

- Goal: Publish reviewer-facing diagnostic summary page.
- Artifact: `index.html`
- Verification:
  - Includes explanation, three GIF panels with captions, concise findings, and admissibility note.

## Completion status

- [x] Phase 1 Discovery completed
- [x] Phase 2 Construction completed
- [x] Phase 3 Synthesis completed
- [x] Phase 4 Analysis completed
- [x] Phase 5 Publication completed

## Verification results

- Trace records written: 914 total expansions
  - Panel A baseline: 57
  - Panel B paper heuristic: 418
  - Panel C stress-weighted heuristic: 439
- GIF synchronization check:
  - `panel_a_baseline.gif`: 439 frames
  - `panel_b_paper_heuristic.gif`: 439 frames
  - `panel_c_stress_weighted.gif`: 439 frames
- Diagnosis summary:
  - First divergence at step 2 for weighted variants
  - No permanent pruning of baseline-path nodes before expansion
  - No frontier collapse under 10 percent peak criterion
