Policy Lineage Record v1

A DecisionDB equivalence policy defines the canonicalization and hashing rules that bind raw engine output to a stable decision identity.

A policy is identified by a content-addressed policy_id. A policy may optionally declare a parent_policy_id to describe lineage, but lineage does not imply compatibility.

Policy states
	•	DRAFT: not authorized for decision persistence
	•	FROZEN: authorized for decision persistence and replay verification

Compatibility
	•	v1 does not permit in-place semantic edits to a frozen policy
	•	any semantic change requires a new policy_id
	•	doc-only clarifications may be committed without changing policy_id if and only if the content-addressed policy definition is unchanged

Required fields for any policy definition
	•	policy_id
	•	policy_name
	•	policy_version
	•	canonicalization_ruleset_id
	•	hash_function and parameters
	•	binding_rules: what fields are included in payload_hash
	•	parent_policy_id (optional)
	•	status: DRAFT or FROZEN
