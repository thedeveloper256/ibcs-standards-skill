# IBCS Standards Skill

A closed-book OpenCode skill for designing, reviewing, fixing, and explaining business reports, presentations, dashboards, charts, tables, KPI pages, variance analyses, and scenario comparisons using IBCS v2.0 notation.

It encodes all **35 top-level rules** and **105 sub-rules** across SIMPLIFY, UNIFY, CHECK, SAY, STRUCTURE, EXPRESS, and CONDENSE, plus semantic notation, a chart/table catalog, a composition playbook, five worked examples, an audit checklist, a completeness map, a glossary, and implementation guides for Python, Power BI, Excel, and HTML/JS.

> **Independent derivative work.** This repository is not affiliated with, endorsed by, or certified by the IBCS Association, the authors of IBCS v2.0, or ISO. It is a working summary, not a substitute for the official IBCS source or ISO 24896 for legal, certification, or formal-compliance purposes. IBCS is a registered trademark of IBCS Institute.

## What is in this repository

```text
.opencode/skills/ibcs-standards/
├── SKILL.md
├── LICENSE
├── assets/
│   ├── page-spec-template.md
│   └── starter-tokens.json
└── references/
    ├── framework.md
    ├── glossary.md
    ├── semantic-notation.md
    ├── chart-and-table-catalog.md
    ├── composition-playbook.md
    ├── worked-examples.md
    ├── audit-checklist.md
    ├── completeness-map.md
    ├── source-and-license.md
    ├── implementation/
    │   ├── python.md
    │   ├── powerbi.md
    │   ├── excel.md
    │   └── html-js.md
    └── rules/
        ├── si-simplify.md
        ├── un-unify.md
        ├── ch-check.md
        ├── sa-say.md
        ├── st-structure.md
        ├── ex-express.md
        └── co-condense.md
```

Also included:

- `scripts/verify_skill.py` — structural verification harness for rule counts, entry schema, router targets, coverage map, and required files.
- `docs/superpowers/specs/2026-10-20-ibcs-standards-skill-design.md` — design and acceptance criteria.
- `BENCHMARK.md` — current closed-book evaluation summary.

The source PDF is **not** redistributed in this repository.

## Quick start

### Use this repository as the project

1. Clone the repository.
2. Open the folder in VS Code with the OpenCode extension.
3. Start a session and ask an IBCS question, for example:

   > Design a one-page IBCS dashboard showing 24 months of sales actual vs plan, with the plan gap by product category.

OpenCode discovers `.opencode/skills/ibcs-standards/` automatically. You can also load it explicitly by mentioning `@ibcs-standards`.

### Install into another project

Copy the whole `ibcs-standards` folder, preserving its name:

```text
<your-project>\.opencode\skills\ibcs-standards
```

Do not copy only `SKILL.md`; the references and assets are part of the skill.

### Install globally for all projects

Copy the folder to the OpenCode global skills directory:

```text
C:\Users\<username>\.config\opencode\skills\ibcs-standards
```

On macOS/Linux:

```text
~/.config/opencode/skills/ibcs-standards
```

Reload VS Code or start a new OpenCode session after copying.

## Verify the package

From the repository root:

```powershell
python scripts/verify_skill.py
```

Expected result:

```text
PASS: skill package meets structural checks.
```

The harness checks the exact rule counts (SI 14, UN 18, CH 15, SA 14, ST 14, EX 14, CO 16), the 105-row completeness map, required rule-entry fields, router targets, JSON validity, and required sections.

## Evaluation

The current closed-book evaluation scored **94.0% with the skill vs 44.9% without it** across five tasks: rule retrieval, page design, audit, encoding, and tool implementation. The page-design task now scores 9/9 with a shared legend and full integrity checks.

See [`BENCHMARK.md`](BENCHMARK.md) for the per-task results and caveats. These are development evaluations, not a certification or a guarantee of correctness.

## License and attribution

The repository content is licensed under **CC BY-SA 4.0**. See [`LICENSE`](LICENSE) and the skill’s [`source-and-license.md`](.opencode/skills/ibcs-standards/references/source-and-license.md).

Source attribution: *International Business Communication Standards (IBCS) Version 2.0*, Rolf Hichert and Jürgen Faisst, IBCS Media, Hilden, 2026, ISBN 978-3-9821414-4-2, licensed under CC BY-SA 4.0. This repository condenses and rewrites the material for closed-book agent use and does not reproduce the source figures or ISO 24896 text.
