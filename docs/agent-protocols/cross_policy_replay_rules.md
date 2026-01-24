Cross-Policy Replay Rules v1

Replay verification is defined as recomputation of decision_id and payload_hash for a persisted decision, using the exact policy_id bound to that decision at persistence time.

Rules
	•	Replay is only valid when recomputed under the decision’s recorded policy_id
	•	Cross-policy replay is forbidden in v1
	•	Any attempt to recompute a decision under a different policy must be treated as a new decision candidate, not a verification event

Rationale
This prevents accidental “verification by reinterpretation,” preserves audit clarity, and keeps the system legible as policy families grow.