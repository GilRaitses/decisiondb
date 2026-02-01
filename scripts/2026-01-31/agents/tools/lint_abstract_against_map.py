#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


def _title_case(term: str) -> str:
    return " ".join(word.capitalize() for word in term.split())


def _add_term(allow: set[str], term: str) -> None:
    cleaned = term.strip()
    if not cleaned:
        return
    allow.add(cleaned)
    if cleaned.lower() == cleaned and " " in cleaned:
        allow.add(_title_case(cleaned))


def load_allowlist(map_path: Path) -> set[str]:
    data = yaml.safe_load(map_path.read_text(encoding="utf-8"))
    allow: set[str] = set()

    concepts = data.get("concept_lineage", [])
    if isinstance(concepts, list):
        for item in concepts:
            if not isinstance(item, dict):
                continue
            name = item.get("concept_name")
            if isinstance(name, str):
                _add_term(allow, name)
            aliases = item.get("aliases", [])
            if isinstance(aliases, list):
                for alias in aliases:
                    if isinstance(alias, str):
                        _add_term(allow, alias)

    interfaces = data.get("interface_inventory", [])
    if isinstance(interfaces, list):
        for item in interfaces:
            if not isinstance(item, dict):
                continue
            name = item.get("interface_name")
            if isinstance(name, str):
                _add_term(allow, name)
            aliases = item.get("aliases", [])
            if isinstance(aliases, list):
                for alias in aliases:
                    if isinstance(alias, str):
                        _add_term(allow, alias)
            fields = item.get("fields_or_signals", [])
            if isinstance(fields, list):
                for field in fields:
                    if not isinstance(field, dict):
                        continue
                    field_name = field.get("name")
                    if isinstance(field_name, str):
                        _add_term(allow, field_name)

    figures = data.get("figure_concept_alignment", [])
    if isinstance(figures, list):
        for item in figures:
            if not isinstance(item, dict):
                continue
            anchored = item.get("anchored_concept")
            if isinstance(anchored, str):
                _add_term(allow, anchored)

    thesis = data.get("thesis")
    if isinstance(thesis, str):
        _add_term(allow, thesis)

    return allow


def tokenize_candidate_terms(text: str) -> set[str]:
    title_phrases = set(
        re.findall(r"\b(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b", text)
    )
    snake_tokens = set(re.findall(r"\b[a-z]+(?:_[a-z0-9]+)+\b", text))
    return {t.strip() for t in title_phrases | snake_tokens if t.strip()}


def _collect_abstract_paths(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    if not path.is_dir():
        return []
    return sorted(p for p in path.rglob("abstract*.txt") if p.is_file())


def main() -> int:
    if len(sys.argv) != 3:
        print(
            "usage: lint_abstract_against_map.py <phase_crosslineage_map.yaml> <abstract.txt|directory>"
        )
        return 2

    map_path = Path(sys.argv[1])
    target_path = Path(sys.argv[2])

    allow = load_allowlist(map_path)
    abstracts = _collect_abstract_paths(target_path)
    if not abstracts:
        print("SKIP: no abstract files found")
        return 0

    failures = []
    for abstract_path in abstracts:
        abstract = abstract_path.read_text(encoding="utf-8")
        candidates = tokenize_candidate_terms(abstract)
        unknown = sorted(t for t in candidates if t not in allow)
        if unknown:
            failures.append((abstract_path, unknown))

    if failures:
        print("FAIL: abstract contains out of map terms")
        for abstract_path, unknown in failures:
            print(f"{abstract_path}:")
            for term in unknown:
                print(f"- {term}")
        return 1

    print("PASS: abstract terms align with map")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
