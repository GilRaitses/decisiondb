#!/bin/bash
# Package arXiv submission tarball (LaTeX + figures only, no .md or .DS_Store)
set -e
cd "$(dirname "$0")/arxiv"

# Files to include (exclude .md, .DS_Store, .aux, .log, .out, .tex.bak)
tar -czvf ../arxiv_submission.tar.gz \
  decisiondb_manuscript.tex \
  decisiondb_manuscript.bbl \
  bibliography.bib \
  sections/ \
  figures/figure2_schema.pdf

echo "Created arxiv_submission.tar.gz"
