how to merge safely (recommended procedure).md
# How to merge safely (recommended procedure)

1. Preserve the tag as the authority

Do not delete or move the tag. That tag is your cryptographic anchor.

Think of it as:

“This exact tree corresponds to what left the building.”

2. Merge into main (or your long-lived trunk)

Use a non-squash merge so provenance is preserved.

git checkout main
git merge strauss/protocol-scaffolding --no-ff

Why:
	•	Keeps the audit trail intact
	•	Preserves agent-attributed commits
	•	Makes rollback trivial if needed

3. Do not retag after merge

The tag already exists on the correct commit.
Let it remain attached to history, not the branch tip.

⸻

What not to do
	•	Do not re-run formatting
	•	Do not regenerate PDFs
	•	Do not “clean up” language
	•	Do not resolve hypothetical reviewer concerns yet

All of that happens after submission, on a new branch.

⸻

After the merge: recommended next branches

Once merged, immediately branch for future work so the frozen state stays sacred.

Suggested branches:
	•	public-minimal-example
	•	dissertation-integration
	•	post-review-revisions (created later)

Each should explicitly state:

“Based on submission-ready-2026-01-24”

⸻

Final recommendation

Yes—merge now.
Then treat the merged main branch as read-only with respect to the submission, and move forward on clean, intentional branches.


But structurally? You’re done.