# Public Minimal Example: Outline

Title:
A Minimal Diagnostic Example of Representation-Dependent Outcomes

1. Problem Setup (Toy Domain)
	•	Fixed dataset or graph
	•	Fixed solver (e.g. shortest path, classifier threshold, simulator)

2. Two Representations
	•	Same data
	•	Different deterministic encodings
	•	Explicitly declared differences

3. Fixed Engine
	•	No learning
	•	No optimization
	•	Run once per representation

4. Outcome Identity
	•	Discrete result
	•	Defined equivalence rule (plain language)

5. Observation
	•	Sometimes outcomes match
	•	Sometimes they differ
	•	The difference is not noise — it is structural

6. Why This Matters
	•	Reproducibility
	•	Debugging
	•	Auditability
	•	Understanding failure modes

Explicitly excluded:
	•	Governance rules
	•	Policy evolution
	•	Replay databases
	•	Enforcement language
