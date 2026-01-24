I. Visual Grammar for Phase Maps (Non-Theoretical, Implementation-Safe)

The goal is to make phase maps look like engineering diagnostics, not physics diagrams or theory cartoons.

1. What a phase map is allowed to look like

Core visual object
	•	A partitioned parameter space
	•	Axes labeled with representation parameters only
	•	Regions colored or hashed by discrete decision ID
	•	Boundaries shown as adjacency discontinuities, not curves

Think “configuration map” or “compatibility chart”, not “phase diagram”.

⸻

2. Axes rules (hard constraint)

Axes must be:
	•	Explicitly labeled as representation parameters
Examples:
	•	temporal_window_size (ms)
	•	kernel_bandwidth
	•	aggregation_rule_id
	•	threshold_percentile

Axes must NOT:
	•	Use abstract symbols like λ, β, γ
	•	Be labeled as “order parameter”, “control parameter”, “temperature”, etc.

Rule:
If an axis cannot be directly instantiated as a configuration key in code, it cannot appear on the figure.

⸻

3. Region encoding rules

Allowed encodings:
	•	Flat colors with legend: “decision_id = A, B, C”
	•	Discrete texture fills (dots, stripes) for grayscale safety
	•	Explicit region labels with IDs (e.g. D_03, D_07)

Forbidden encodings:
	•	Gradients
	•	Heatmaps
	•	Smooth interpolation
	•	Colorbars implying continuity

Rule:
Color implies categorical membership only, never magnitude.

⸻

4. Boundary representation

Boundaries must be:
	•	Pixel-aligned
	•	Cell-to-cell
	•	Shown as thin separators or adjacency lines

Boundaries must NOT be:
	•	Smoothed
	•	Fit with curves
	•	Described as “critical lines” or “transition curves”

Label boundaries as:
	•	“decision change boundary”
	•	“identity discontinuity”

Never as:
	•	phase transition
	•	bifurcation
	•	critical threshold

⸻

5. Annotations and captions

Allowed caption language:
	•	“regions of constant decision identity”
	•	“representation configurations yielding identical outputs”
	•	“observed discontinuities under representation variation”

Forbidden caption language:
	•	emergent phase
	•	critical regime
	•	attractor
	•	tipping point
	•	intelligence

Caption test:
Could a compiler engineer read this without thinking it is physics?
If yes, it passes.

⸻

6. Visual checklist (enforceable)

Before a figure is allowed:
	•	All axes are named configuration parameters
	•	All colors map to discrete IDs
	•	No gradients present
	•	No smooth curves drawn
	•	No theoretical nouns in caption

This can literally be a CI checklist later.

⸻

II. “Do Not Violate” Glossary (For Automatic Retrofit)

This glossary is meant to be mechanically applied. An agent can search and replace, flag, or block merges.

⸻

A. Forbidden terms (hard ban)

These words should never appear in repos, READMEs, or patents:
	•	phase transition
	•	criticality
	•	critical point
	•	bifurcation
	•	order parameter
	•	attractor
	•	chaos
	•	emergence
	•	intelligence
	•	regime (unless explicitly “decision regime”)
	•	dynamics (unless referring to logged time series)
	•	system state (use “output identity” instead)

⸻

B. Required replacements (canonical)

Use these mappings exactly.

Forbidden term	Required replacement
phase map	decision identity map
phase diagram	representation partition map
transition	decision change
critical boundary	identity boundary
stable phase	constant decision region
unstable	representation-sensitive
[banned: identity transition replaces this]	decision identity change
emergent behavior	observed output pattern

No synonyms allowed. Consistency beats style.

⸻

C. Approved core vocabulary (safe set)

These terms are always allowed and define scope:
	•	representation
	•	representation family
	•	representation parameter
	•	encoding
	•	sweep
	•	configuration
	•	discrete decision
	•	decision identity
	•	identity boundary
	•	stability
	•	fracture
	•	logging
	•	diagnostics
	•	partition
	•	adjacency
	•	neighborhood

If a concept cannot be expressed with these words, it probably does not belong in the repo.

⸻

D. Sentence templates (safe reuse)

Agents should prefer these exact templates:
	•	“We record the discrete decision identity produced under each representation configuration.”
	•	“Decision identity is constant within regions of representation space and changes at discrete boundaries.”
	•	“These maps characterize stability and fracture of outputs under representation variation.”
	•	“No assumptions are made about continuity or underlying system properties.”

Using templates prevents drift.

⸻

E. Automatic retrofit rules (for agents)

An agent refactoring existing docs should:
	1.	Scan for forbidden terms
	2.	Replace using canonical mapping
	3.	Insert the boilerplate paragraph on representation-induced transitions if any boundary language appears
	4.	Reject any figure that violates the visual checklist
	5.	Downgrade metaphoric language to operational descriptions

This is enforceable without understanding the science.

1. Where phase-map language belongs

Grants (NSF, SU, NRT, fellowships)

Use phase maps only as diagnostic summaries.
Do not use “criticality” as a property of the system.

Allowed framing:
	•	“representation–decision phase maps”
	•	“stability regions and transition boundaries”
	•	“mapping where discrete outputs change under representational variation”

Purpose in grants:
	•	Demonstrates methodological rigor
	•	Shows how emergent behavior is detected, not asserted
	•	Aligns with evaluation language around diagnostics, interpretability, and validation

Avoid entirely:
	•	“phase transitions”
	•	“critical dynamics”
	•	“edge of chaos”

Grants care about what you can measure and compare, not metaphors.

⸻

Papers (methods vs discussion)

Methods sections
Phase maps are defined operationally and mechanically.
	•	Construction procedure
	•	Parameter axes
	•	Discrete output identifiers
	•	Adjacency rules for detecting changes

Discussion sections only
You may gesture cautiously to broader concepts:
	•	“resembles phase-like behavior”
	•	“suggests sensitivity to representation”

But you must explicitly state:
	•	No claim about underlying system criticality
	•	Transitions are induced by representation choice

This keeps reviewers from reading theory where you are doing diagnostics.

⸻

Repos and READMEs (most strict)

Repos are implementation contracts, not interpretive spaces.

Use:
	•	“decision phase map”
	•	“representation sweep results”
	•	“output identity partitioning”

Never use:
	•	criticality
	•	emergence
	•	intelligence
	•	phase transition

If it cannot be implemented deterministically, it does not belong in a repo README.

⸻

2. One-paragraph boilerplate explaining “criticality” safely

You can reuse this verbatim.

In this work, terms such as transition, boundary, or critical point refer strictly to observed changes in discrete output identity across neighboring representation configurations. These terms do not imply physical, biological, or cognitive criticality in the underlying system. All transitions are defined operationally with respect to a fixed decision process applied to fixed data, and arise solely from variation in representational encoding. The resulting maps characterize the stability and fracture of decision identity under representational change, rather than making claims about intrinsic phase behavior of the system being studied.

This paragraph neutralizes almost every possible misreading.

⸻

3. Fully EPO-safe “Phase Map” section

This is suitable for a patent, README, or award appendix.

Phase Maps and Representation-Induced Transitions

A phase map is a derived data structure constructed from a systematic sweep over a family of representations applied to fixed raw data and evaluated by a fixed decision process. Each point in the representation domain corresponds to a specific configuration of representation parameters, such as kernel choice, aggregation window, threshold value, or encoding scheme. For each configuration, the decision process produces a discrete output identifier.

The phase map partitions the representation domain into regions in which the same discrete output identifier is produced. Boundaries between regions are detected by comparing the output identifiers associated with adjacent representation configurations according to a predefined neighborhood relation in parameter space. A boundary is recorded when two neighboring configurations yield different output identifiers.

Phase maps are computed entirely from logged execution results and do not assume continuity, smoothness, or parametric structure in the decision process. They serve as diagnostic summaries that reveal where decision identity is stable under representational variation and where it changes abruptly. These maps do not assert properties of the underlying system, but instead characterize the dependence of discrete outputs on representational choices under controlled conditions.
