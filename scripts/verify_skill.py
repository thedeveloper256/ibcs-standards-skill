#!/usr/bin/env python3
"""Verify the IBCS skill package against the design spec."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SKILL = ROOT / ".opencode" / "skills" / "ibcs-standards"
SKILL = DEFAULT_SKILL
SPEC = ROOT / "docs" / "superpowers" / "specs" / "2026-10-20-ibcs-standards-skill-design.md"

SKILL_CANDIDATES = [
    ROOT / ".opencode" / "skills" / "ibcs-standards",
    ROOT / ".claude" / "skills" / "ibcs-standards",
    ROOT / ".agents" / "skills" / "ibcs-standards",
    ROOT / "skills" / "ibcs-standards",
]


def rule_files(skill: Path) -> dict[str, Path]:
    return {
        "SI": skill / "references" / "rules" / "si-simplify.md",
        "UN": skill / "references" / "rules" / "un-unify.md",
        "CH": skill / "references" / "rules" / "ch-check.md",
        "SA": skill / "references" / "rules" / "sa-say.md",
        "ST": skill / "references" / "rules" / "st-structure.md",
        "EX": skill / "references" / "rules" / "ex-express.md",
        "CO": skill / "references" / "rules" / "co-condense.md",
    }


def discover_skill(explicit: str | None) -> Path:
    if explicit:
        path = Path(explicit).expanduser()
        if not path.is_absolute():
            path = (Path.cwd() / path).resolve()
        return path
    for candidate in SKILL_CANDIDATES:
        if (candidate / "SKILL.md").exists():
            return candidate
    return DEFAULT_SKILL


REQUIRED_FIELDS = [
    "**Requirement.**",
    "**Why.**",
    "**Apply.**",
    "**Exceptions / limits.**",
    "**Audit.**",
    "**Source.**",
]
REQUIRED_FILES = [
    "references/framework.md",
    "references/composition-playbook.md",
    "references/worked-examples.md",
    "references/audit-checklist.md",
    "references/source-and-license.md",
    "assets/page-spec-template.md",
    "LICENSE",
]
CHART_NAMES = [
    "single column", "stacked column", "grouped column", "horizontal pin",
    "growth waterfall", "variance waterfall", "line chart",
    "single bar", "stacked bar", "grouped bar", "vertical pin",
    "calculation waterfall", "remainder bar", "scattergram", "bubble chart",
]
TABLE_TYPES = ["time series table", "variance table", "cross table", "combined table"]
SEMANTIC_TERMS = [
    "solid dark", "solid light", "outlined", "hatched", "ΔPL", "ΔPY",
    "ΔPL%", "ΔPY%", "percentage point", "green", "red", "blue",
    "scale band", "outlier", "trend arrow", "annotation reference",
]
GLOSSARY_TERMS = [
    "actual", "previous year", "plan", "budget", "forecast",
    "measure", "scenario", "period", "structure dimension",
    "notation", "MECE", "YTD", "YTG", "MAT", "MAA",
]
TOOL_GUIDES = ["python.md", "powerbi.md", "excel.md", "html-js.md"]

failures: list[str] = []
notes: list[str] = []


def fail(message: str) -> None:
    failures.append(message)


def missing(path: Path, allow_missing: bool) -> bool:
    if path.exists():
        return False
    target = notes if allow_missing else failures
    try:
        label = path.relative_to(ROOT)
    except ValueError:
        label = path
    target.append(f"MISSING: {label}")
    return True


def main() -> int:
    global SKILL

    parser = argparse.ArgumentParser()
    parser.add_argument("--allow-missing", action="store_true")
    parser.add_argument(
        "--skill-dir",
        help="Path to the skill directory; auto-detects .opencode, .claude, .agents, or skills/",
    )
    args = parser.parse_args()
    SKILL = discover_skill(args.skill_dir)

    if not SPEC.exists():
        fail(f"missing spec: {SPEC}")
        expected: dict[str, str] = {}
    else:
        spec = SPEC.read_text(encoding="utf-8")
        appendix = spec.split("## Appendix A", 1)[1].split("## Appendix B", 1)[0]
        inventory = re.findall(r"^- ((?:SI|UN|CH|SA|ST|EX|CO) \d+\.\d+) (.+)$", appendix, re.M)
        expected = dict(inventory)
        if len(expected) != 105:
            fail(f"spec inventory has {len(expected)} sub-rules, expected 105")

    seen: dict[str, str] = {}
    for prefix, path in rule_files(SKILL).items():
        if missing(path, args.allow_missing):
            continue
        text = path.read_text(encoding="utf-8")
        ids = re.findall(rf"^### ({prefix} \d+\.\d+) — ", text, re.M)
        if len(ids) != len(set(ids)):
            fail(f"{path.name}: duplicate rule IDs")
        for rule_id in ids:
            if rule_id in seen:
                fail(f"{rule_id} appears in both {seen[rule_id]} and {path.name}")
            seen[rule_id] = path.name
        for block in re.split(r"(?=^### )", text, flags=re.M):
            match = re.match(rf"^### ({prefix} \d+\.\d+) — ", block)
            if not match:
                continue
            for field in REQUIRED_FIELDS:
                if field not in block:
                    fail(f"{match.group(1)} missing {field}")
        notes.append(f"{path.name}: {len(ids)} sub-rules")

    if not args.allow_missing:
        for rule_id in sorted(set(expected) - set(seen)):
            fail(f"rule files missing ID: {rule_id}")
        for rule_id in sorted(set(seen) - set(expected)):
            fail(f"rule files have extra ID: {rule_id}")

    completeness = SKILL / "references" / "completeness-map.md"
    if not missing(completeness, args.allow_missing):
        text = completeness.read_text(encoding="utf-8")
        mapped = set(re.findall(r"^\| ((?:SI|UN|CH|SA|ST|EX|CO) \d+\.\d+) \|", text, re.M))
        if not args.allow_missing:
            if len(mapped) != 105:
                fail(f"completeness map has {len(mapped)} IDs, expected 105")
            if mapped != set(expected):
                fail(
                    "completeness map mismatch: "
                    f"missing {sorted(set(expected) - mapped)}, "
                    f"extra {sorted(mapped - set(expected))}"
                )

    skill_md = SKILL / "SKILL.md"
    if not missing(skill_md, args.allow_missing) and not args.allow_missing:
        text = skill_md.read_text(encoding="utf-8")
        frontmatter = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not frontmatter:
            fail("SKILL.md missing YAML frontmatter")
        else:
            front = frontmatter.group(1)
            name_match = re.search(r"^name:\s*(\S+)\s*$", front, re.M)
            if not name_match:
                fail("SKILL.md frontmatter missing name")
            elif name_match.group(1) != SKILL.name:
                fail(
                    f"SKILL.md frontmatter name {name_match.group(1)!r} "
                    f"does not match folder {SKILL.name!r}"
                )
            if not re.search(r"^description:\s*\S", front, re.M):
                fail("SKILL.md frontmatter missing description")
        line_count = len(text.splitlines())
        if line_count >= 500:
            fail(f"SKILL.md has {line_count} lines, expected <500")
        for phrase in ["closed-book", "Create workflow", "Review workflow", "Reference router", "Output contract"]:
            if phrase.lower() not in text.lower():
                fail(f"SKILL.md missing phrase: {phrase}")
        for rel in re.findall(r"`(references/[A-Za-z0-9_./-]+\.md)`", text):
            if not (SKILL / rel).exists():
                fail(f"SKILL.md router target missing: {rel}")

    catalog = SKILL / "references" / "chart-and-table-catalog.md"
    if not missing(catalog, args.allow_missing):
        text = catalog.read_text(encoding="utf-8").lower()
        for name in CHART_NAMES + TABLE_TYPES:
            if name not in text:
                fail(f"chart catalog missing: {name}")

    semantic = SKILL / "references" / "semantic-notation.md"
    if not missing(semantic, args.allow_missing):
        text = semantic.read_text(encoding="utf-8").lower()
        for term in SEMANTIC_TERMS:
            if term.lower() not in text:
                fail(f"semantic notation missing: {term}")

    for guide in TOOL_GUIDES:
        path = SKILL / "references" / "implementation" / guide
        if missing(path, args.allow_missing):
            continue
        text = path.read_text(encoding="utf-8").lower()
        for phrase in ["limitations", "ibcs"]:
            if phrase not in text:
                fail(f"{guide} missing: {phrase}")

    tokens = SKILL / "assets" / "starter-tokens.json"
    if not missing(tokens, args.allow_missing):
        try:
            json.loads(tokens.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(f"starter-tokens.json invalid JSON: {exc}")

    glossary = SKILL / "references" / "glossary.md"
    if not missing(glossary, args.allow_missing):
        text = glossary.read_text(encoding="utf-8").lower()
        for term in GLOSSARY_TERMS:
            if term.lower() not in text:
                fail(f"glossary missing: {term}")

    for rel in REQUIRED_FILES:
        missing(SKILL / rel, args.allow_missing)

    for note in notes:
        print(f"NOTE: {note}")
    if failures:
        print("\nFAILURES:")
        for item in failures:
            print(f"- {item}")
        return 1
    print("\nPASS: skill package meets structural checks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
