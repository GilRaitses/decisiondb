# Crosslineage guardrails

## Abstract lint

Run the lint against the crosslineage map and the work-tree:

```sh
python3 scripts/2026-01-31/agents/tools/lint_abstract_against_map.py \
  scripts/2026-01-31/agents/notes/phase_crosslineage_map.yaml \
  scripts/2026-01-31/agents/work-tree
```

The lint scans the target directory for files named `abstract*.txt` and checks
Title Case phrases and snake_case tokens against the allowlist extracted from
`phase_crosslineage_map.yaml`. If no abstract files are found it exits with a
SKIP message.

## Map invariant override

The map is enforced by CI. To allow a deliberate edit, include an override file
in the same change:

```
.github/override/phase_crosslineage_map_edit.override
```

Its content must be exactly:

```
ALLOW_MAP_EDIT_OVERRIDE
```

## Pre-commit hook

The repository includes a convenience pre-commit hook in `.githooks/pre-commit`.
If you already use a hooks manager, integrate the logic there instead of
overriding your hooks path.

File mode is not used for enforcement. CI and the pre-commit hook are the
authoritative guardrails.
