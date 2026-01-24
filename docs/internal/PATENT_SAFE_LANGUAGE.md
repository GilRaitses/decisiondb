#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# --- Required internal docs sanity checks ---
# These are guardrails for award/patent packaging. Keep them lightweight and deterministic.
REQUIRED_INTERNAL_DOCS=(
  "docs/internal/PATENT_SAFE_LANGUAGE.md"
)

for doc in "${REQUIRED_INTERNAL_DOCS[@]}"; do
  if [[ ! -f "$doc" ]]; then
    echo "[pre-commit] Missing required internal doc: $doc" >&2
    echo "[pre-commit] Create the file or restore it before committing." >&2
    exit 1
  fi
  # Fail fast on empty files (common drift failure mode)
  if [[ ! -s "$doc" ]]; then
    echo "[pre-commit] Required internal doc is empty: $doc" >&2
    echo "[pre-commit] Populate it before committing." >&2
    exit 1
  fi
done

# --- End required internal docs sanity checks ---

# (rest of the original hook script continues here)