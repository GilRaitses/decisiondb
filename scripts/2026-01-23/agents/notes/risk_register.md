# Risk Register

| Risk | Potential Impact | Mitigation |
|------|------------------|------------|
| Identity ill-posed due to equivalence policy ambiguity | Decision identity could be undefined or vary unpredictably | Policy must be versioned, documented, and referenced by exact string; enforce policy via code, not prose. |
| Representation family underspecified | Sweep results may omit relevant parameter ranges | Define an explicit parameter grid (list or discretized range) and store its hash; enforce that the grid is passed to the generator. |
| Engine not truly fixed | Outcomes may change between runs, breaking reproducibility | Lock engine binary, config, and version; compute a content hash of the executable and config. |
| Sweep grid not deterministic | Results may differ across runs even with same parameters | Use canonical JSON ordering for parameters and enforce that the grid is generated from a deterministic function. |
| Misleading visualization implying optimization | Viewer may interpret plot as performance optimization | Include a check step that verifies the visualization contains only categorical identity (color/label) and no continuous metrics. |
| Terminology drift in new sections | Miscommunication and loss of glossary consistency | Enforce that the glossary is imported verbatim; prohibit synonyms for core terms ("representation", "engine", "decision identity", "equivalence policy"). |
