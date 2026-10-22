# IBCS Standards Skill — Design Spec

**Date:** 2026-10-20  
**Status:** Draft for user review  
**Artifact:** `.opencode/skills/ibcs-standards/`  
**Portability:** The artifact is plain Markdown with a standard `SKILL.md` entry point. `.opencode` is the canonical in-repo path, but the folder can be installed in any harness's skills directory.  
**Skill ID:** `ibcs-standards`  
**Source:** *International Business Communication Standards (IBCS) Version 2.0*, 2026-07-02, 169 pages, CC BY-SA 4.0.

---

## 1. Summary

Build one agent skill that acts as a **closed-book working substitute** for the IBCS Standards v2.0. An agent with only this skill folder must be able to:

- answer rule-level questions with the correct rule ID;
- audit a report page and identify violations by severity;
- choose the correct chart or table and specify its anatomy;
- encode scenarios, variances, measures, time periods, and markers correctly;
- write the key message, three-line title, and page structure;
- implement the result in Python, Power BI, Excel, or HTML/JS.

The skill is a practical substitute, not a verbatim reproduction of ISO 24896 and not a certification or legal-compliance authority. Every rule entry cites its source page so claims remain verifiable.

---

## 2. Problem

The project contains the 169-page IBCS v2.0 PDF. Applying it currently requires reading or searching a large document, interpreting figures, and remembering rule IDs. That is slow and error-prone, and it makes consistent review difficult.

An earlier draft `SKILL.md` framed the skill as a distilled practitioner's guide and explicitly said it was "not a replacement" for the PDF. That contradicts the requirement. The draft will be revised into a complete, closed-book knowledge base.

---

## 3. Goal and definition of “substitute”

**Goal.** Enable normal IBCS design, review, explanation, and implementation work without opening the PDF.

**Closed-book means:**

1. The agent can retrieve any of the 105 sub-rules by ID or topic.
2. The agent can apply the rule to a described page without asking for the PDF.
3. The agent can distinguish what the standard requires from what is a recommendation or a gap.
4. The agent can produce a page specification or audit using the skill's templates and checklists.
5. The agent can map the rule to at least one implementation approach in the four supported tools.

**Substitute does not mean:**

- reproducing ISO 24896 normative text verbatim;
- replacing the source for formal certification, legal review, or contractual compliance;
- reproducing the PDF's figures pixel-for-pixel;
- covering topics the standard itself leaves for future versions.

When a question falls outside the catalog, the skill must say so and cite the gap. It must not invent a rule.

---

## 4. Users and use cases

**Primary user:** a report author, analyst, controller, or designer using an agent harness (OpenCode, Claude Code, or another `SKILL.md`-compatible harness) to create or repair business reporting.

| Use case | Example request | Required skill behavior |
|---|---|---|
| Rule lookup | “What does UN 4.1 require for absolute variance labels?” | Return the rule text, notation, exceptions, and source page. |
| Page design | “Design a one-page sales report comparing AC with PL for 2026.” | Produce the output contract: message, title, visual spec, encoding, text elements, checks. |
| Audit | “Review this dashboard: truncated axis, solid plan columns, pie chart, rainbow colors.” | Rank findings by severity and cite the exact rule IDs. |
| Visual selection | “We have 12 countries and 3 years of sales; which visual?” | Recommend bars plus a remainder category, not a pie or spaghetti chart. |
| Semantic encoding | “How do I show actual vs forecast in a stacked column?” | Specify solid vs outlined/hatched fills and the segment treatment. |
| Tool implementation | “How do I render outlined plan columns in Power BI?” | Give an IBCS-specific workaround and state native limitations. |
| Teaching | “Explain solid, outlined, and hatched.” | Explain the semantic model with examples and exceptions. |

**Trigger conditions:** IBCS, ISO 24896, SUCCESS, semantic notation, solid/outlined/hatched, scenario comparison, variance analysis, KPI page, dashboard, business chart, business table, report review, chart selection, “is this clear/honest/decision-ready.”

---

## 5. Scope

### In scope

| Area | Top-level rules | Sub-rules |
|---|---|---|
| SIMPLIFY (SI) | 5 | 14 |
| UNIFY (UN) | 5 | 18 |
| CHECK (CH) | 5 | 15 |
| SAY (SA) | 5 | 14 |
| STRUCTURE (ST) | 5 | 14 |
| EXPRESS (EX) | 5 | 14 |
| CONDENSE (CO) | 5 | 16 |
| **Total** | **35** | **105** |

Also in scope:

- definitions and page anatomy;
- chart and table taxonomy, anatomy, and selection;
- scenario, variance, measure, time, structure, marker, and format notation;
- composition playbook and templates;
- five worked page examples;
- audit checklist, severity model, and report template;
- glossary and rule index;
- implementation guides for Python, Power BI, Excel, and HTML/JS;
- completeness map and source traceability;
- license and attribution.

### Out of scope

- Verbatim ISO 24896 normative text. The ISO standard is a separate copyrighted document; the IBCS PDF references it but does not reproduce it.
- Certification, legal, or contractual compliance claims.
- A full-text mirror of the PDF. The user chose a structured working substitute, not a bundled dump.
- Reproduction of the PDF's figures. The skill describes anatomy in words and cites figure/page references.
- Pixel-perfect templates for every tool.
- Topics the standard explicitly defers to future versions: other measure types, adjustment-analysis visualization, selecting visualization, area/boxplot/two-value-axis notation. These are documented as gaps, not filled in.

---

## 6. Design principles

1. **Closed-book completeness.** Every sub-rule has an entry. “See the PDF” is never the only answer.
2. **Traceability.** Each entry carries its rule ID and source page.
3. **Progressive disclosure.** `SKILL.md` routes; reference files load only when needed.
4. **One skill, modular references.** Avoid trigger fragmentation and duplicated rules.
5. **Normative honesty.** Separate ISO requirements, IBCS rules, and the author's suggestions.
6. **Actionability.** Every rule has an application instruction and an audit question.
7. **Tool honesty.** State what a tool cannot do natively and give a workaround.
8. **Composition before decoration.** A clear message outranks a pretty page.
9. **Examples over adjectives.** Worked specs show what “compliant” means.
10. **Small surface, deep references.** `SKILL.md` stays under 500 lines.

---

## 7. Package architecture

```text
.opencode/skills/ibcs-standards/
├── SKILL.md
├── LICENSE
├── references/
│   ├── framework.md
│   ├── rules/
│   │   ├── si-simplify.md
│   │   ├── un-unify.md
│   │   ├── ch-check.md
│   │   ├── sa-say.md
│   │   ├── st-structure.md
│   │   ├── ex-express.md
│   │   └── co-condense.md
│   ├── chart-and-table-catalog.md
│   ├── semantic-notation.md
│   ├── composition-playbook.md
│   ├── worked-examples.md
│   ├── audit-checklist.md
│   ├── glossary.md
│   ├── completeness-map.md
│   ├── implementation/
│   │   ├── python.md
│   │   ├── powerbi.md
│   │   ├── excel.md
│   │   └── html-js.md
│   └── source-and-license.md
└── assets/
    ├── starter-tokens.json
    └── page-spec-template.md
```

The directory name determines the skill ID: `ibcs-standards`. The frontmatter `name` is the display label.

---

## 8. Content specification

### 8.1 `SKILL.md`

**Frontmatter**

```yaml
name: IBCS Standards
description: Use when designing, reviewing, fixing, or explaining business reports, presentations, dashboards, charts, tables, KPI pages, variance analyses, or scenario comparisons; when someone mentions IBCS, ISO 24896, SUCCESS, semantic notation, solid/outlined/hatched scenarios, variance colors, small multiples, or asks whether a visual is clear, honest, or decision-ready; or when choosing chart/table types for business data. Covers notation and composition, with implementation guidance for Python, Power BI, Excel, and HTML/JS.
```

The description is trigger-focused, third-person, and does not summarize a workflow. It names the concrete contexts and keywords an agent or user would use.

**Body sections**

1. **What this skill is** — closed-book working substitute; 105 sub-rules; source and limits.
2. **The one-sentence model** — say the message first, prove it with the right visual, encode meaning consistently.
3. **Two layers** — notation (SI/UN/CH) vs composition (SA/ST/EX/CO); why both are required.
4. **Non-negotiables** — 12 high-cost rules with IDs and exceptions.
5. **Create workflow** — seven steps: frame, message, structure, visual, encode, compose, verify.
6. **Review workflow** — six steps: read, integrity, semantics, composition, clutter, report.
7. **Decision shortcuts** — analytical question → preferred visual.
8. **Reference router** — need → file.
9. **Output contract** — required fields for a design and for an audit.
10. **Closed-book contract** — what to do when the skill lacks an answer; no invented rules.
11. **Honesty rules** — requirement vs recommendation vs suggestion; tool limitations.
12. **Source and license** — citation and link to `references/source-and-license.md`.

Target: 300–450 lines. No duplicated rule catalog.

### 8.2 `references/framework.md`

- Purpose and source version.
- Notation vs composition.
- SUCCESS table with all seven principles and rule ranges.
- Definitions: business reporting, report, report page, visual, visual component, dimensions, categories, measures, scenarios, periods, structure dimensions, notation manual.
- ISO 24896 relationship: notation alignment; IBCS adds explanation, examples, and composition.
- Page anatomy: key message, title lines, subtitle, visual, labels/legend, annotations, footnotes, source.
- How to use the skill and its router.
- Source map by section and page range.

### 8.3 Rule files

One file per principle:

| File | Rule IDs | Sub-rules |
|---|---|---|
| `rules/si-simplify.md` | SI 1–5 | 14 |
| `rules/un-unify.md` | UN 1–5 | 18 |
| `rules/ch-check.md` | CH 1–5 | 15 |
| `rules/sa-say.md` | SA 1–5 | 14 |
| `rules/st-structure.md` | ST 1–5 | 14 |
| `rules/ex-express.md` | EX 1–5 | 14 |
| `rules/co-condense.md` | CO 1–5 | 16 |

Each file begins with a short principle overview, then the top-level rules, then every sub-rule. Cross-references link to related rules and reference files.

### 8.4 Rule entry schema

Every sub-rule uses this exact structure:

```markdown
### UN 4.1 — Unify scenario analyses

**Requirement.** Analyze scenarios by comparing them and by calculating absolute
and relative variances. Use consistent signs and abbreviations...

**Why.** ...

**Apply.** ...

**Exceptions / limits.** ... (or “None stated in v2.0.”)

**Audit.** Is each variance labeled with the correct sign, reference, and
percentage/percentage-point notation?

**See also.** UN 3.2, UN 4.2, `semantic-notation.md`.

**Source.** p. 49–55.
```

Quality bar:

- The requirement is faithful to the source, in imperative prose.
- The rationale explains the consequence of violating it.
- The application is concrete enough to act on.
- Exceptions are only those stated in the source, or explicitly marked as not stated.
- The audit question is answerable from a page.
- The source page is exact.
- No invented numbers, colors, or rules.
- Where the standard defers a topic, write “Not specified in v2.0” and point to the gap list.

### 8.5 `references/chart-and-table-catalog.md`

**Chart selection matrix** by analytical question, axis orientation, and data conditions.

**Chart families:**

- Horizontal/time: single column, stacked column, grouped column, horizontal pin, growth waterfall, variance waterfall, line.
- Vertical/structure: single bar, stacked bar, grouped bar, vertical pin, calculation waterfall, variance waterfall, remainder bar.
- Two value axes: scattergram, bubble chart, bubble pie.

For each chart type: purpose, anatomy (axes, components, widths, labels, legends), use when, avoid when, variants, and source page. Include the “no specific notation concept yet” status for area, boxplot, and two-value-axis charts.

**Table taxonomy:**

- Column types: row header, scenario, variance, time, measure, structure, “of which,” remainder, “percent of,” totals, hierarchical, nested.
- Row types: column header, measure, structure, “of which,” remainder, “percent of,” totals, hierarchical, nested.
- Table types: time series, variance, cross, combined.
- Layout rules: widths, alignment, vertical lines/gaps, row heights, horizontal lines, totals placement, hierarchy placement.

**Selection guidance:** table for lookup and precision; chart for comparison and message; why tables and charts do not compete.

### 8.6 `references/semantic-notation.md`

- Scenario types and fills: actual (solid dark), previous period (solid light), plan/budget (outlined), forecast (outlined + hatched); abbreviations AC, PY, PL, BU, FC.
- Stacked charts: scenario notation on the lowest segment; upper segments in gray shades; outline/hatch for planned/forecast segments.
- Scenario comparisons: order by time; same-period order by creation date; AC/FC foreground; scenario triangles; reference scenario on axis.
- Variances: absolute (`ΔPL`, `ΔPY`, `AC-PL`, `FC-PL`), relative (`ΔPL%`, `ΔPY%`), signs, `+`, percentage points, N/A for negative denominators.
- Variance colors: green desirable, red undesirable, blue neutral; grayscale fallbacks; color-deficiency guidance.
- Variance widths and labels: same width/scale as base; thin pins; labels outside in the direction of change; pin heads; axis encoding.
- Measures: absolute vs relative; 2/3 vs 1/3 category width; thick vs thin lines.
- Time: left-to-right; table columns; abbreviations; `.2026`, `2026.`, `Jan..Mar`; category widths by period length.
- Structure: vertical axes; horizontal labels; exceptions for interval/cardinal scales.
- Time-series analyses: YTD (`_Jun 2026`), YTD average, last-date value, YTG (`Jun 2026_`), moving (`~Jun 2026`), MAT/MAA, temporal indexing.
- Structure analyses: averaging, ranking, selecting, indexing, normalizing.
- Adjustment analyses: currency, inflation, seasonal; note the visualization gap.
- Markers: assisting lines/areas, difference markers, trend arrows, highlighting ellipses, reference arrowheads, annotation references, scale bands, outlier markers.
- Formats: numbers, currencies, physical units, dates, negative values, plus signs.
- Accessibility: color deficiency, grayscale, not relying on color alone.

### 8.7 `references/composition-playbook.md`

**SAY**

- Goals and audience.
- Situation → complication → question → answer.
- Message types: detect, explain, suggest.
- Message-first sequencing and cultural/negative-message caution.
- Evidence, precise words, highlighting, sources, annotations.
- Repeat and consequences for presentations; differences for written reports and dashboards.
- Templates: key message sentence, executive summary page, presentation opening/closing.

**STRUCTURE**

- Consistent items, statement types, wording, visualizations.
- MECE: non-overlapping reporting structures, measures, and dimensions; exhaustive arguments and structures.
- Hierarchical structures: deductive vs inductive reasoning; when each works.
- Visualizing structure in reporting, tables, and notes.

**EXPRESS**

- Chart vs table.
- Chart selection and replacement rules.
- Quantitative over conceptual; avoiding text slides.
- Adding scenarios and variances.
- Explaining causes with trees, clusters, and correlations.

**CONDENSE**

- Small fonts, components, visuals.
- Margins and empty space.
- Adding data points and dimensions.
- Overlay, multi-tier, extended charts; embedded chart components and explanations.
- Small multiples, related charts, chart–table combinations, charts in text pages.

**Page patterns**

- Page anatomy and three-line title formula.
- Written report vs presentation vs dashboard.
- Common composition anti-patterns and fixes.

### 8.8 `references/worked-examples.md`

Five complete page specifications:

1. **Monthly sales, AC vs PL, absolute and relative variances** — horizontal three-tier chart: grouped columns, absolute variance columns, relative variance pins. Includes message, title, encoding, labels, and checks.
2. **Structure analysis with remainder** — vertical single bars, sorted, “Rest of…” category separated by a wider gap, totals and labels.
3. **P&L calculation waterfall** — vertical calculation waterfall with base, contribution, subtotal, and totals bars.
4. **KPI dashboard with small multiples** — page grid, identical scales, per-visual titles, key message, annotations.
5. **Executive summary slide** — message + evidence chart + consequences, no text slide.

Each example contains: context, data shape, decision/message, structure, visual specification, semantic encoding, text elements, integrity checks, and “what would be wrong.”

### 8.9 `references/audit-checklist.md`

- Severity model:
  - **Critical:** integrity failures that make the visual misleading.
  - **Major:** semantic or composition failures that change interpretation.
  - **Minor:** clutter, redundancy, density, and polish.
- Full checklist grouped by pass, each item with rule ID.
- Common anti-patterns table: symptom → rule ID → fix.
- Triage rules: integrity before semantics before styling.
- Findings report template:

```markdown
1. [Critical] <finding> — <rule ID>. Evidence: <...>. Fix: <...>.
2. [Major] <finding> — <rule ID>. Evidence: <...>. Fix: <...>.
3. [Minor] <finding> — <rule ID>. Evidence: <...>. Fix: <...>.
```

- Stop conditions: if the axis is truncated or scales conflict, do not spend time on minor styling until the integrity issue is resolved.

### 8.10 `references/glossary.md`

- Alphabetical glossary of the source's terms and references.
- Short definitions and rule cross-references.
- Acronyms used in the standard: AC, PY, PL, BU, FC, YTD, YTG, MAT, MAA, MECE, CAGR, and others actually present in the source.
- No invented definitions; source page references where useful.

### 8.11 `references/completeness-map.md`

A table with one row per sub-rule:

| Rule ID | Title | Rule file | Source page | Checklist item | Worked example |
|---|---|---|---|---|---|

Plus:

- Coverage summary: 35 top-level, 105 sub-rules, 100% mapped.
- Explicit gaps: measure types, adjustment visualization, selecting visualization, area/boxplot/two-value-axis notation, and any other “future version” items.
- Verification procedure: count headings, compare against the inventory in Appendix A, spot-check random rules against the PDF.
- Change log.

### 8.12 Implementation guides

Each guide covers the same headings:

1. What the tool does natively.
2. IBCS mapping: scenario fills, variance colors, measure widths, axes, labels, tables.
3. Limitations and workarounds.
4. Code/config snippets.
5. Accessibility.
6. Verification checklist.

**Python (`python.md`)** — matplotlib and plotly: zero baselines, bar widths, scenario fills/hatches, variance colors, pins, waterfalls, annotations, tables, small multiples, no chartjunk.

**Power BI (`powerbi.md`)** — theme JSON, DAX measures for scenarios/variances, conditional formatting, axis settings, table/matrix design, native limitations for pattern fills and per-series outlines, SVG/HTML workaround.

**Excel (`excel.md`)** — chart types, axis minimums, pattern fills, outlines, data labels, table layout, number formats, small multiples, limitations such as per-series bar widths.

**HTML/JS (`html-js.md`)** — CSS/SVG patterns, ECharts/D3/Chart.js/Vega-Lite patterns, zero baselines, bar widths, labels, accessible tables, print styles.

Code snippets are illustrative and must be verified during evaluation. If a tool cannot do something natively, the guide says so.

### 8.13 Assets

**`starter-tokens.json`** — non-normative starter tokens:

- scenario fills: actual, previous, plan, budget, forecast;
- variance colors and grayscale fallbacks;
- hatch patterns;
- a `$comment` stating that IBCS does not prescribe exact color codes and that organizations should keep tokens consistent.

**`page-spec-template.md`** — fill-in template matching the output contract: decision, audience, message, title lines, visual spec, encoding, text elements, checks.

### 8.14 Source and license

`references/source-and-license.md` contains:

- Full citation: *International Business Communication Standards (IBCS) Version 2.0*, Rolf Hichert and Jürgen Faisst, IBCS Media, Hilden, 2026, ISBN 978-3-9821414-4-2.
- License: CC BY-SA 4.0; this skill is a derivative work and is shared under the same license.
- ISO 24896 relationship and the limits of this skill.
- Source page map and verification instructions.
- Change log with version/date.

`LICENSE` at the skill root repeats the CC BY-SA 4.0 notice and link.

---

## 9. Workflows and routing

### Create workflow

1. Frame the decision and audience.
2. Write the key message.
3. Structure the argument MECE.
4. Choose the visual.
5. Encode semantics.
6. Compose the page.
7. Verify integrity and composition.

### Review workflow

1. Read as a decision-maker.
2. Integrity pass (critical).
3. Semantic pass (major).
4. Composition pass (major).
5. Clutter pass (minor).
6. Report findings with severity, rule ID, evidence, and fix.

### Routing

`SKILL.md` routes to one or more references based on the task:

- rule lookup → specific rule file;
- chart/table choice → catalog;
- encoding → semantic notation;
- message/structure → composition playbook;
- audit → checklist;
- implementation → tool guide;
- definitions → framework/glossary;
- coverage verification → completeness map.

### Closed-book fallback

If the skill does not contain an answer:

1. Say “not covered by this skill.”
2. Check whether the source defers the topic to a future version.
3. If the source has a rule but the skill lacks detail, treat it as a skill gap and record it for revision.
4. Do not invent a rule, color, dimension, or chart type.

---

## 10. Accuracy, traceability, and licensing

- Every rule entry cites a source page. Page references use PDF page numbers (1–169), which match the printed body page numbers; front-matter pages use roman numerals.
- Every chart/table entry cites its EX rule and page.
- The completeness map is the single source of truth for coverage.
- A random sample of at least 20 rules is checked against the PDF before release.
- The skill never presents ISO 24896 text as reproduced; it describes the alignment and cites the source.
- The skill is licensed CC BY-SA 4.0, with attribution to the IBCS Association and the authors.
- Tool snippets are illustrative; the guides state when behavior is version-dependent.

---

## 11. Testing and evaluation

### 11.1 RED — baseline without the skill

Run five prompts with no skill and no PDF. Record the exact failures.

| # | Prompt | What baseline is likely to miss |
|---|---|---|
| 1 | “In IBCS, how do I label an absolute plan variance and a relative plan variance, and what color is a favorable variance?” | Exact `ΔPL` / `ΔPL%` notation, sign rules, green/red/blue semantics. |
| 2 | “I have 24 months of monthly sales for actual and plan, plus 12 product categories. Design one page.” | Three-line title, multi-tier chart, scenario encoding, variance tiers, not pie/dual-axis. |
| 3 | “Review this page: the y-axis starts at 80, plan columns are solid, the composition is a pie chart, and the palette is rainbow.” | Rule IDs, severity order, correct scenario fill, pie replacement, color semantics. |
| 4 | “How do I show actual vs forecast in a stacked column, and what width should a margin line use?” | Solid vs outlined/hatched, lowest-segment rule, 2/3 vs 1/3 widths, thin line for ratio. |
| 5 | “How do I render outlined plan columns and hatched forecast columns in Power BI and matplotlib?” | Native tool limitations, SVG/hatch workarounds, exact semantic mapping. |

Baseline outputs are saved to `iteration-1/eval-N/without_skill/outputs/`.

### 11.2 GREEN — with the skill only

Run the same five prompts with the skill folder and **no PDF access**. Save to `iteration-1/eval-N/with_skill/outputs/`.

Assertions:

- cites the correct rule ID(s);
- uses exact notation (`ΔPL`, `ΔPL%`, `+`, solid/outline/hatch, 2/3 vs 1/3);
- chooses the correct chart/table and axis orientation;
- ranks audit findings by severity and gives concrete fixes;
- states tool limitations honestly;
- does not invent a rule;
- identifies any gap as a gap.

### 11.3 Coverage sweep

- One retrieval question per principle (7 questions).
- Ten random sub-rule IDs from the 105, asking for requirement + application.
- Verify each answer cites the correct rule file and source page.
- Verify the completeness map has no missing IDs.

### 11.4 REFACTOR

- Fix gaps exposed by GREEN and the coverage sweep.
- Rerun the affected prompts.
- Do not add rules that are not in the source.

### 11.5 Grading and review

- Grade with the skill-creator grader schema: `text`, `passed`, `evidence`.
- Aggregate with `scripts/aggregate_benchmark.py`.
- Generate the review viewer with `eval-viewer/generate_review.py` (static HTML if needed).
- Present qualitative outputs and the benchmark to the user.
- Iterate on feedback.

### 11.6 Test workspace

Use a temp workspace outside the skill folder:

```text
<temp>\opencode\ibcs-skill-workspace\
  iteration-1\
    eval-0-rule-retrieval\
    eval-1-page-design\
    eval-2-audit\
    eval-3-encoding\
    eval-4-tool-implementation\
    benchmark.json
    benchmark.md
```

This keeps the project clean and prevents the eval agents from reading the PDF.

---

## 12. Success criteria

- All 105 sub-rules are present and mapped; zero missing IDs.
- `SKILL.md` is under 500 lines and routes correctly.
- Closed-book with-skill runs materially outperform baseline on specificity, correctness, and rule-ID citation.
- No invented rules in any eval run.
- A page specification from the skill includes every output-contract field.
- An audit from the skill ranks integrity findings before styling and gives concrete fixes.
- Tool guides state at least one real limitation per tool.
- A random 20-rule spot check matches the PDF.
- The user can complete normal design/review work without opening the PDF.

---

## 13. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Over-summarization loses nuance | Full rule schema with exceptions and source pages; 20-rule spot check. |
| Hallucinated rules fill gaps | Explicit “not specified” entries; closed-book fallback; no-invention assertions. |
| Context bloat | One file per principle; router; SKILL.md under 500 lines. |
| Tool APIs change | Principle-first guides; label snippets illustrative; verify during evals. |
| Figure-dependent rules are hard to convey | Describe anatomy in words; use ASCII layouts; cite figure pages. |
| Licensing | CC BY-SA 4.0 notice, attribution, share-alike; no ISO text reproduction. |
| Trigger failure | Trigger-rich description; manual trigger tests; optional description optimization later. |
| Staleness | Version stamp, source map, changelog. |

---

## 14. Resolved decisions and non-goals

**Resolved:**

- One skill, modular references.
- Canonical project-local install at `.opencode/skills/ibcs-standards/`; copy to a harness-specific skills directory as needed.
- Full 105-sub-rule catalog plus practical core.
- Closed-book working substitute, not a full-text mirror.
- All four tool guides: Python, Power BI, Excel, HTML/JS.
- No figure reproduction; describe and cite.
- No verbatim ISO text.

**Non-goals:**

- Certification or legal compliance.
- Pixel-perfect templates.
- A general chart-design skill unrelated to IBCS.
- Reproducing the PDF as a single dump.

---

## 15. Implementation phases

1. **RED:** run baseline prompts, record failures.
2. **Core knowledge:** framework + seven rule files.
3. **Application knowledge:** semantic notation, chart/table catalog, composition playbook.
4. **Practice:** worked examples, audit checklist, glossary, completeness map.
5. **Implementation:** four tool guides, tokens, page template, license.
6. **Revise SKILL.md** against the completed references.
7. **GREEN:** closed-book evals, coverage sweep, grading, viewer.
8. **REFACTOR:** close gaps, rerun, final review.

Detailed task breakdown belongs in the implementation plan created after this spec is approved.

---

## 16. Acceptance checklist

- [ ] All 105 sub-rules have entries with requirement, why, apply, exceptions, audit, source.
- [ ] All 35 top-level rules have overviews.
- [ ] Chart/table catalog covers every type named in EX 1.1 and EX 1.2.
- [ ] Semantic notation covers scenarios, variances, measures, time, structure, markers, formats.
- [ ] Composition playbook covers SA, ST, EX, CO with templates.
- [ ] Five worked examples are complete.
- [ ] Audit checklist has severity, full checks, anti-patterns, and report template.
- [ ] Glossary covers the source's terms.
- [ ] Completeness map has 105 rows and no gaps.
- [ ] Four tool guides exist with limitations.
- [ ] `SKILL.md` is under 500 lines and routes correctly.
- [ ] CC BY-SA 4.0 attribution and license are present.
- [ ] Closed-book evals pass the assertions; no invented rules.
- [ ] User reviews and approves the final output.

---

## Appendix A — Rule inventory (105 sub-rules)

### SIMPLIFY (14)

- SI 1.1 Avoid cluttered layouts
- SI 1.2 Avoid colored or filled backgrounds
- SI 1.3 Avoid animation and transition effects
- SI 2.1 Avoid frames, shades, and pseudo-3D without meaning
- SI 2.2 Avoid decorative colors
- SI 2.3 Avoid decorative fonts
- SI 3.1 Replace grid lines and value axes with data labels
- SI 3.2 Avoid vertical lines by right-aligning data
- SI 4.1 Avoid superfluous words
- SI 4.2 Avoid obvious terms
- SI 4.3 Avoid repeated words
- SI 5.1 Avoid labels for small values
- SI 5.2 Avoid long numbers
- SI 5.3 Avoid unnecessary labels

### UNIFY (18)

- UN 1.1 Unify terms and abbreviations
- UN 1.2 Unify numbers, units, and dates
- UN 2.1 Unify key messages
- UN 2.2 Unify titles and subtitles
- UN 2.3 Unify the position of legends and labels
- UN 2.4 Unify annotations
- UN 2.5 Unify footnotes
- UN 3.1 Unify measures
- UN 3.2 Unify scenarios
- UN 3.3 Unify time periods, use horizontal axes
- UN 3.4 Unify structure dimensions, use vertical axes
- UN 4.1 Unify scenario analyses
- UN 4.2 Unify time series analyses
- UN 4.3 Unify structure analyses
- UN 4.4 Unify adjustment analyses
- UN 5.1 Unify highlighting markers
- UN 5.2 Unify scaling markers
- UN 5.3 Unify outlier markers

### CHECK (15)

- CH 1.1 Avoid truncated axes
- CH 1.2 Avoid logarithmic axes
- CH 1.3 Avoid different class sizes
- CH 2.1 Avoid clipped visual components
- CH 2.2 Use creative solutions for challenging scaling issues
- CH 3.1 Use correct area comparisons, prefer linear ones
- CH 3.2 Use correct volume comparisons, prefer linear ones
- CH 3.3 Avoid misleading colored areas in maps
- CH 4.1 Use identical scale for the same unit
- CH 4.2 Size charts to given data
- CH 4.3 Use scaling markers if necessary
- CH 4.4 Use outlier markers if necessary
- CH 4.5 Use magnifying glasses
- CH 5.1 Show the impact of inflation
- CH 5.2 Show the currency impact

### SAY (14)

- SA 1.1 Know own goals
- SA 1.2 Know target audience
- SA 2.1 Map situation
- SA 2.2 Explain problem
- SA 2.3 Raise question
- SA 3.1 Detect, explain, or suggest
- SA 3.2 Say message first
- SA 4.1 Provide evidence
- SA 4.2 Use precise words
- SA 4.3 Highlight message
- SA 4.4 Name sources
- SA 4.5 Link annotations
- SA 5.1 Repeat message
- SA 5.2 Explain consequences

### STRUCTURE (14)

- ST 1.1 Use consistent items
- ST 1.2 Use consistent types of statements
- ST 1.3 Use consistent wording
- ST 1.4 Use consistent visualizations
- ST 2.1 Build non-overlapping reporting structures
- ST 2.2 Build non-overlapping business measures
- ST 2.3 Build non-overlapping structure dimensions
- ST 3.1 Build exhaustive arguments
- ST 3.2 Build exhaustive structures
- ST 4.1 Use deductive reasoning
- ST 4.2 Use inductive reasoning
- ST 5.1 Visualize structure in reporting
- ST 5.2 Visualize structure in tables
- ST 5.3 Visualize structure in notes

### EXPRESS (14)

- EX 1.1 Use appropriate chart types
- EX 1.2 Use appropriate table types
- EX 2.1 Replace pie and ring charts
- EX 2.2 Replace gauges, speedometers
- EX 2.3 Replace radar and funnel charts
- EX 2.4 Replace spaghetti charts
- EX 2.5 Replace traffic lights
- EX 3.1 Prefer quantitative representations
- EX 3.2 Avoid text slides in presentations
- EX 4.1 Add scenarios
- EX 4.2 Add variances
- EX 5.1 Show tree structures
- EX 5.2 Show clusters
- EX 5.3 Show correlations

### CONDENSE (16)

- CO 1.1 Use small fonts
- CO 1.2 Use small components
- CO 1.3 Use small visuals
- CO 2.1 Use narrow page margins
- CO 2.2 Reduce empty space
- CO 3.1 Add data points
- CO 3.2 Add dimensions
- CO 4.1 Show overlay charts
- CO 4.2 Show multi-tier charts
- CO 4.3 Show extended charts
- CO 4.4 Embed chart components in tables
- CO 4.5 Embed explanations
- CO 5.1 Show small multiples
- CO 5.2 Show related charts on one page
- CO 5.3 Show chart-table combinations
- CO 5.4 Show charts and tables in text pages

---

## Appendix B — Source section map

| Section | Pages |
|---|---|
| Introduction, definitions | iii–xiv |
| NOTATION | 15 |
| SIMPLIFY | 16–23 |
| UNIFY | 24–67 |
| CHECK | 68–75 |
| COMPOSITION | 77 |
| SAY | 78–86 |
| STRUCTURE | 87–95 |
| EXPRESS | 96–142 |
| CONDENSE | 143–156 |
| Table of figures | 157–161 |
| Terms and references | 163–166 |
| Further resources | 167–169 |

---

## Appendix C — Closed-book eval assertions

| Eval | Assertions |
|---|---|
| Rule retrieval | Correct rule ID; correct requirement; sign/color/width detail; source page; no invented rule. |
| Page design | Three-line title; message first; correct chart family and axis; scenario encoding; variance encoding; labels/legend; integrity checks. |
| Audit | At least three findings; correct severity order; rule IDs; concrete fixes; no styling before integrity. |
| Encoding | Solid/outline/hatch; lowest-segment rule; 2/3 vs 1/3; thick vs thin line; forecast hatch; plan outline. |
| Tool implementation | Correct tool limitation; workaround; semantic mapping; no false native-support claim. |

---

*End of spec.*
