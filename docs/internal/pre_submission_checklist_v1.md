# Pre-Submission Checklist (DecisionDB)

Status: layout frozen, content review in progress

## Layout & Structure (LOCKED)
- [x] layout_freeze.yaml committed
- [x] Page count stable (10 pages)
- [x] Figure placement verified (pages 2, 6, 6, 8, 9)
- [x] No float warnings
- [x] No overfull/underfull hbox warnings
- [x] Section headers contain no colons
- [x] Figure captions visually distinct from body text

## Figures
- [x] Figures embedded inline (not collected at end)
- [x] No placeholder tokens (<EXP_ID_*>) in submission build
- [x] No TikZ text leaking outside figure environments
- [x] All figures labeled and referenced consistently

## Content Integrity
- [x] No scope expansion (diagnostic framing preserved)
- [x] No learning / optimization claims introduced
- [x] Terminology consistent with frozen glossary
- [x] Minimal Example section present and self-contained

## Compilation
- [x] Clean pdflatex run
- [x] No auxiliary debug comments in main.tex
- [x] Bibliography compiles cleanly

## Ready for:
- [ ] External verification (Levi)
- [ ] Final content polish
- [ ] Camera-ready formatting