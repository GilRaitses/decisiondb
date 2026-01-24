STYLE_GUIDE.md

DecisionDB Documentation and Visualization Standards

This document defines mandatory language, visualization, and terminology rules for all documentation, figures, repositories, and manuscripts associated with DecisionDB and related systems. Its purpose is to ensure conceptual clarity, patent safety, and cross-domain interpretability by enforcing an operational, non-theoretical framing.

This guide is not stylistic preference. It is a compliance document.

⸻

1. Scope and Intent

DecisionDB studies how discrete decision identities depend on representational choices applied to fixed data and fixed decision engines.

All documentation must:
	•	Treat representation as a configurable encoding choice.
	•	Treat discrete decision identity as the primary observable.
	•	Avoid theoretical, physical, or metaphoric interpretations of observed structure.

This project does not propose theories of intelligence, dynamics, emergence, or criticality. It provides diagnostic instrumentation.

⸻

2. Core Conceptual Object

The only central object is the decision-valued mapping:

f : R → D

Where:
	•	R is a family of representations constructed from fixed raw data.
	•	D is a set of discrete decision identities produced by a fixed engine.

All language, figures, and analyses must be reducible to this mapping.

⸻

3. Approved Vocabulary (Safe Set)

The following terms are always allowed and define the permitted conceptual space:
	•	representation
	•	representation family
	•	representation parameter
	•	encoding
	•	configuration
	•	sweep
	•	discrete decision
	•	decision identity
	•	decision change
	•	decision stability
	•	fracture
	•	identity boundary
	•	partition
	•	adjacency
	•	neighborhood
	•	logging
	•	diagnostics
	•	observable
	•	output identity

If a concept cannot be expressed using this vocabulary, it likely does not belong in this repository.

⸻

4. Forbidden Vocabulary (Hard Ban)

The following terms must not appear anywhere in documentation, figures, captions, code comments, or manuscripts:
	•	phase transition
	•	phase diagram
	•	criticality
	•	critical point
	•	bifurcation
	•	attractor
	•	order parameter
	•	chaos
	•	emergence
	•	emergent
	•	intelligence
	•	dynamics (unless strictly referring to recorded time series)
	•	system state
	•	regime (unless explicitly “decision regime”)

Any appearance of these terms should be treated as a blocking error.

⸻

5. Canonical Replacements

If prohibited terms appear in legacy material, they must be replaced using the following exact mappings:

Prohibited Term	Required Replacement
phase map	decision identity map
phase diagram	representation partition map
transition	decision change
critical boundary	identity boundary
stable phase	constant decision region
unstable	representation-sensitive
[banned: identity transition replaces this]	decision identity change
emergent behavior	observed output pattern

No alternative synonyms are permitted.

⸻

6. Visual Grammar for Decision Identity Maps

Decision identity maps are diagnostic artifacts, not theoretical diagrams.

6.1 Axes Rules

Axes must:
	•	Be explicitly labeled as representation parameters.
	•	Correspond to concrete configuration keys.

Examples:
	•	temporal_window_ms
	•	kernel_bandwidth
	•	aggregation_rule_id
	•	threshold_percentile

Axes must not:
	•	Use symbolic parameters (λ, β, γ).
	•	Reference physical or abstract control variables.

If an axis cannot be instantiated in code, it cannot appear in a figure.

⸻

6.2 Region Encoding

Allowed:
	•	Flat colors representing discrete decision IDs.
	•	Discrete textures or patterns.
	•	Explicit region labels (e.g. D_01, D_04).

Forbidden:
	•	Gradients.
	•	Heatmaps.
	•	Continuous colorbars.
	•	Interpolated shading.

Color and texture encode categorical membership only, never magnitude.

⸻

6.3 Boundary Representation

Boundaries must:
	•	Be pixel-aligned or cell-adjacent.
	•	Indicate adjacency changes between configurations.

Boundaries must not:
	•	Be smoothed.
	•	Be fit with curves.
	•	Be described as transitions, bifurcations, or thresholds.

Approved labels:
	•	“decision change boundary”
	•	“identity discontinuity”

⸻

6.4 Captions and Annotations

Approved caption language:
	•	“regions of constant decision identity”
	•	“representation configurations yielding identical outputs”
	•	“observed identity changes under representation variation”

Forbidden caption language:
	•	any reference to physics, biology, learning, or emergence
	•	metaphors implying underlying system behavior

Caption test:
A compiler engineer should be able to read the caption without inferring theory.

⸻

7. Required Sentence Templates

To prevent language drift, prefer the following exact constructions:
	•	“We record the discrete decision identity produced under each representation configuration.”
	•	“Decision identity is constant within regions of representation space and changes at discrete boundaries.”
	•	“These maps characterize stability and fracture under representation variation.”
	•	“No assumptions are made about continuity or underlying system properties.”

These templates may be reused verbatim.

⸻

8. Interpretation Boundary

Interpretive claims about learning, memory, biology, or physical systems must not appear in:
	•	repositories
	•	READMEs
	•	figures
	•	patents
	•	technical documentation

Such interpretations may appear only in:
	•	discussion sections of papers
	•	talks
	•	separate conceptual essays

The infrastructure remains strictly diagnostic.

⸻

9. Enforcement Rules for Agents

Automated agents modifying this repository must:
	1.	Scan for forbidden vocabulary.
	2.	Replace terms using canonical mappings.
	3.	Reject figures violating the visual grammar.
	4.	Insert approved sentence templates when describing identity boundaries.
	5.	Avoid introducing new conceptual nouns.

Failure to comply is grounds for rejection.

⸻

10. Design Principle Summary

DecisionDB is not about finding the correct representation.

It is about measuring how decisions depend on representation.

Everything in this repository exists to make that dependence explicit, enumerable, and inspectable.
