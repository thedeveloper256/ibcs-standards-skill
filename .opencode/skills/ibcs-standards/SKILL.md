---
name: IBCS Standards
description: Use when designing, reviewing, fixing, or explaining business reports, presentations, dashboards, charts, tables, KPI pages, variance analyses, or scenario comparisons; when someone mentions IBCS, ISO 24896, SUCCESS, semantic notation, solid/outlined/hatched scenarios, variance colors, small multiples, or asks whether a visual is clear, honest, or decision-ready; or when choosing chart/table types for business data. Covers notation and composition, with implementation guidance for Python, Power BI, Excel, and HTML/JS.
---

# IBCS Standards

## What this skill is

This is a **closed-book working substitute** for the IBCS Standards v2.0. It encodes all 35 top-level rules and all 105 sub-rules, plus the notation system, chart/table catalog, composition playbook, worked examples, audit checklist, and implementation guidance. You can design, review, explain, and implement IBCS work without opening the source PDF.

- **Source:** *International Business Communication Standards (IBCS) Version 2.0*, Rolf Hichert and Jürgen Faisst, IBCS Media, 2026-07-02, 169 pages, CC BY-SA 4.0.
- **Notation:** aligned with ISO 24896. **Composition:** IBCS guidance for message, structure, visual choice, and density.
- **Limits:** this is not a verbatim ISO 24896 copy, not a certification or legal-compliance authority, and not a full-text mirror of the PDF. It summarizes and reorganizes the source for practical use.
- **Traceability:** every rule entry has an ID and source page. The PDF is the traceability source, not the working source.
- **Deferred topics:** v2.0 does not fully specify measure types beyond absolute/relative, adjustment-analysis visualization, selecting visualization, area/boxplot/two-value-axis notation. The skill labels those gaps; it does not invent rules.

The package is modular. This file routes; the reference files carry the detail. Load only what the task needs.

## The one-sentence model

**Say the message first, prove it with the right visual, and encode meaning consistently.**

A report is a decision instrument, not a container for data. The message tells the audience what matters; the visual provides evidence; the notation makes the evidence trustworthy.

## Two layers

| Layer | Question | Principles | What it governs |
|---|---|---|---|
| **Notation** | Does the visual mean what it appears to mean? | SIMPLIFY, UNIFY, CHECK | Clutter, terminology, dimensions, scenarios, variances, scales, integrity |
| **Composition** | Does the page help the audience decide? | SAY, STRUCTURE, EXPRESS, CONDENSE | Message, storyline, chart/table choice, information density |

Notation without composition produces clean but pointless pages. Composition without notation produces persuasive but unreliable pages. Apply both.

## Non-negotiables

These are the highest-cost rules. Exceptions are limited to those stated in v2.0; do not invent others.

| # | Rule | Rule ID | Exception / limit |
|---|---|---|---|
| 1 | Time runs left-to-right on horizontal axes; structure runs top-to-bottom on vertical axes. | UN 3.3, UN 3.4 | Interval/cardinal statistical scales such as bell curves may need a horizontal axis. Local period abbreviations are acceptable if consistent. |
| 2 | Value axes start at zero. | CH 1.1 | Indexed data with small deviations from 100% may zoom in; place category labels at the 100% line. This does not license truncating an ordinary absolute-value chart. |
| 3 | The same unit uses the same scale across visuals on a page. | CH 4.1–4.3 | If scales must differ, use scale bands or size the charts to the data. |
| 4 | Never clip, break, or truncate visual components to fit a scale. | CH 2.1 | An outlier marker is not a clipped component. Creative 2D/3D scaling is allowed only when proportional and truthful (CH 2.2). |
| 5 | Encode scenarios by fill: actual = solid dark, previous period = solid light, plan/budget = outlined, forecast = outlined + hatched. | UN 3.2 | In an ordinary time series, earlier periods need not be lightened. Exact color codes are not prescribed; keep them consistent. |
| 6 | Variances carry a sign and a reference: `+` for positive, `Δ` + reference (`ΔPL`, `ΔPY`), `%` suffix for relative variances, percentage points for ratio differences. | UN 4.1 | A relative variance with a negative or otherwise uninterpretable denominator is `N/A`, not a computed percentage. |
| 7 | Variance color: green = desirable, red = undesirable, blue = neutral. | UN 4.1 | Color is semantic, not arithmetic; a positive cost variance can be red. Use the grayscale fallbacks and a non-color cue for accessibility. |
| 8 | Absolute measures use columns/bars at 2/3 of category width; relative measures use 1/3; relative lines are 50% of the thick line. | UN 3.1 | A comprehensive notation for other measure types is a future topic; state that gap. |
| 9 | For time-series and variance tables, put time, scenarios, and variances in columns; put measures and structure categories in rows. For cross tables, structures may appear in both columns and rows. | UN 3.3, EX 1.2 | One-dimensional lists without row headers are not tables. Combined tables may nest column/row types. |
| 10 | Page titles have three lines: who (reporting unit), what (measure), when (time/scenario/variance). Titles describe; they do not evaluate. | UN 2.2 | Screen layouts may combine lines with a pipe; the exact position may vary by organization but must be consistent. |
| 11 | The key message comes first, in a complete sentence, and is visually highlighted. | SA 3.2, SA 4.3 | In presentations with negative, unexpected, or unpleasant messages, or in cultural contexts where directness is impolite, build context first — but do not bury the message. Written reports/dashboards still lead with the message. |
| 12 | Remove decoration. Use color, weight, and emphasis only for analytical meaning. | SI 1–2 | A light fill may group content if it stays away from text; decorative backgrounds, frames, shadows, and 3D are not allowed. |

### Rule ID validity

Before citing an ID, check it against this range table. Do not invent an ID, a sub-rule number, or a source page.

| Principle | Valid sub-rule ranges | Count |
|---|---|---|
| SI | 1.1–1.3, 2.1–2.3, 3.1–3.2, 4.1–4.3, 5.1–5.3 | 14 |
| UN | 1.1–1.2, 2.1–2.5, 3.1–3.4, 4.1–4.4, 5.1–5.3 | 18 |
| CH | 1.1–1.3, 2.1–2.2, 3.1–3.3, 4.1–4.5, 5.1–5.2 | 15 |
| SA | 1.1–1.2, 2.1–2.3, 3.1–3.2, 4.1–4.5, 5.1–5.2 | 14 |
| ST | 1.1–1.4, 2.1–2.3, 3.1–3.2, 4.1–4.2, 5.1–5.3 | 14 |
| EX | 1.1–1.2, 2.1–2.5, 3.1–3.2, 4.1–4.2, 5.1–5.3 | 14 |
| CO | 1.1–1.3, 2.1–2.2, 3.1–3.2, 4.1–4.5, 5.1–5.4 | 16 |

**Specific traps:** there is no `UN 5.4`, `UN 5.5`, or `UN 10`; the UN 5 series ends at 5.3, and UN 1 ends at 1.2. If a needed rule is not in the table, check `references/completeness-map.md` rather than guessing.

## Create workflow

Use this when designing a new page, visual, report, or dashboard.

### 1. Frame the decision

- Who is the audience: function, position, knowledge, expectations, objections, cultural context?
- What should they know or do after this page?
- What is the cost of misunderstanding?
- Is the goal to inform, explain, or decide?

Write one sentence: “After this page, the audience should decide/understand ___.”

**Rules:** SA 1.1, SA 1.2. **Reference:** `references/rules/sa-say.md`.

### 2. Write the message

Use situation → complication → question → answer. The answer is the key message: a complete sentence with subject, verb, magnitude, comparison, time, and consequence.

Example: “Net sales reached 128.4 mEUR in 2026, 6.2 mEUR (4.6%) below plan; the gap is concentrated in Q4.”

Do not use the title as the message. The title is descriptive; the message is evaluative.

**Rules:** SA 2.1–2.3, SA 3.1–3.2. **Reference:** `references/rules/sa-say.md`.

### 3. Structure the content

Make the argument MECE: mutually exclusive, collectively exhaustive. Separate reporting structures, measures, and structure dimensions. Choose deductive reasoning when the premises are strong and the issue is controversial; choose inductive grouping when the evidence is best organized into homogeneous, non-overlapping, exhaustive arguments.

**Rules:** ST 1–5. **Reference:** `references/rules/st-structure.md`.

### 4. Choose the visual

Tables are for lookup and precision. Charts are for comparison and message. Match the analytical question and data shape:

- time → horizontal axis;
- structure → vertical axis;
- two measures → scattergram;
- three measures → bubble chart;
- composition → stacked columns/bars;
- scenario comparison → grouped columns/bars or a variance tier;
- relative variance → pins;
- stock change → growth waterfall;
- flow variance → variance waterfall;
- calculation → calculation waterfall;
- many categories → remainder bar.

**Rules:** EX 1–2. **References:** `references/chart-and-table-catalog.md`, `references/rules/ex-express.md`.

### 5. Encode meaning

Apply the notation:

- scenario fills (AC solid dark, PY solid light, PL/BU outlined, FC outlined + hatched);
- measure widths (2/3 absolute, 1/3 relative; thick vs thin lines);
- variance signs (`ΔPL`, `ΔPY`, `ΔPL%`, `ΔPY%`, `+`, `N/A`, percentage points);
- variance colors (green/red/blue with grayscale fallbacks);
- time markers (YTD, YTG, moving, indexing);
- structure markers (averaging, ranking, indexing, normalizing);
- number, currency, unit, and date formats.

**Rules:** UN 1–5, CH 4–5. **Reference:** `references/semantic-notation.md`.

### 6. Compose the page

Add:

1. key message;
2. three-line title (who / what / when);
3. subtitle only if the page has multiple visuals;
4. visual(s) with labels and legends — for a multi-series visual, specify one shared legend and its position;
5. annotations with references;
6. footnotes and sources.

Use small multiples, multi-tier charts, overlays, extended charts, or chart–table combinations only when they increase understanding. Keep the page dense but legible.

**Rules:** UN 2, CO 1–5. **References:** `references/composition-playbook.md`, `references/rules/co-condense.md`.

### 7. Verify integrity

Check, in this order:

- zero baselines (CH 1.1);
- no clipped components (CH 2.1);
- identical scales for the same unit, or scaling markers (CH 4.1–4.3);
- correct area/volume encoding (CH 3.1–3.2);
- map colors only for area data (CH 3.3);
- equal class widths (CH 1.3);
- inflation/currency adjustments visible (CH 5.1–5.2);
- scenario/variance notation (UN 3–4);
- title/message/evidence (SA 2–4);
- grayscale and color-vision check.

Then run `references/audit-checklist.md`.

## Review workflow

Use this when auditing, critiquing, or fixing an existing page.

### 1. Read as a decision-maker

What is the page trying to say? Is the message first? Can you prove it from the visual? If not, the composition problem comes before the styling problem. Identify the decision, audience, and claimed message.

### 2. Integrity pass — critical

Look for truncated axes, clipped or broken components, inconsistent scales for the same unit, area/volume distortion, misleading map colors, unequal class widths, and hidden inflation/currency effects.

**Stop and fix these first.** If the axis is truncated or the scales conflict, do not spend time on fonts or colors. A beautiful page with a broken scale is still wrong.

**Rules:** CH 1–5.

### 3. Semantic pass — major

Check scenario fills, variance signs/colors, measure widths, axis orientation, time/structure notation, markers, number/unit/date formats, and missing comparisons.

**Rules:** UN 1–5.

### 4. Composition pass — major

Check the three-line descriptive title, key message, MECE structure, hierarchy, chart/table choice, replacement of inappropriate visuals, labels/legends, annotations, and sources.

**Rules:** SA 1–5, ST 1–5, EX 1–5.

### 5. Clutter pass — minor

Check decorative elements, backgrounds, frames, shadows, gridlines, redundant words, long numbers, unnecessary labels, oversize fonts, wasted margins, and empty space.

**Rules:** SI 1–5, CO 1–5.

### 6. Report findings

For each finding, state:

- **Severity:** critical / major / minor.
- **Rule ID:** exact IBCS rule.
- **Evidence:** what on the page demonstrates the problem. If you quantify a distortion (for example, “the gap looks 2× too large”), show the calculation; otherwise describe it qualitatively.
- **Fix:** a concrete change, not “improve clarity.”
- **Residual risk:** what remains uncertain after the fix.

Order by severity, then by impact on the decision. Do not dump all 105 rules; fix what changes the decision.

**Reference:** `references/audit-checklist.md`.

## Decision shortcuts

| Analytical question | Preferred visual | Notes |
|---|---|---|
| How did one measure develop over time? | Single column; line chart for many points or trend focus | Time on horizontal axis |
| How is a total composed over time? | Stacked column | All values same sign; usually ≤5 series |
| How does actual compare with plan/previous year over time? | Grouped column, or single column + scenario triangles | Reference scenario behind primary |
| How large is the relative variance over time? | Horizontal pin | Thin pins; pin head shows the scenario analyzed |
| What caused a change in a stock over time? | Growth waterfall | Base/total columns plus contributions |
| What caused a variance between periods/scenarios? | Variance waterfall | Flow measure; assisting lines connect columns |
| How does a structure compare in one period? | Single bar | Structure on vertical axis; sort meaningfully |
| How is a structure composed? | Stacked bar | All values same sign; usually ≤5 series |
| How does a structure compare across scenarios? | Grouped bar, or single bar + scenario triangles | Reference behind primary |
| How large is the relative variance by structure? | Vertical pin | Thin bars/pins |
| What caused a difference in a calculation? | Calculation waterfall | Base/totals bars plus contributions |
| Are two measures related? | Scattergram | Two value axes |
| Are three measures related? | Bubble chart | Bubble area encodes the third measure |
| Do I need exact values or lookup? | Table | Time/scenario/variance in columns |
| Many categories, need exhaustiveness? | Bar chart + remainder | “Rest of…” separated by a wider gap |

If the visual is a pie, ring, gauge, radar, funnel, spaghetti, or traffic light, check the replacement rules before using it. Each has a narrow exception; see `references/rules/ex-express.md`.

## Reference router

Load only what the task needs.

| Need | Read |
|---|---|
| Mental model, definitions, ISO relationship, page anatomy | `references/framework.md` |
| SIMPLIFY rules (clutter, decoration, redundancy) | `references/rules/si-simplify.md` |
| UNIFY rules (terminology, text, dimensions, analyses, markers) | `references/rules/un-unify.md` |
| CHECK rules (axes, scales, integrity, adjustments) | `references/rules/ch-check.md` |
| SAY rules (goals, message, evidence, sources) | `references/rules/sa-say.md` |
| STRUCTURE rules (MECE, hierarchy, visualization) | `references/rules/st-structure.md` |
| EXPRESS rules (chart/table choice, replacements, comparisons) | `references/rules/ex-express.md` |
| CONDENSE rules (small elements, density, combined visuals) | `references/rules/co-condense.md` |
| Chart/table selection, anatomy, layout | `references/chart-and-table-catalog.md` |
| Scenario fills, variance encoding, markers, formats | `references/semantic-notation.md` |
| Composition playbook and templates | `references/composition-playbook.md` |
| Five complete page examples | `references/worked-examples.md` |
| Audit checklist, severity model, anti-patterns | `references/audit-checklist.md` |
| All 105 rules with titles, files, pages, examples | `references/completeness-map.md` |
| Terms and abbreviations | `references/glossary.md` |
| Python implementation | `references/implementation/python.md` |
| Power BI implementation | `references/implementation/powerbi.md` |
| Excel implementation | `references/implementation/excel.md` |
| HTML/JS implementation | `references/implementation/html-js.md` |
| Citation, license, verification, changelog | `references/source-and-license.md` |
| Starter tokens (non-normative) | `assets/starter-tokens.json` |
| Page specification template | `assets/page-spec-template.md` |

## Output contract

### Design output

When producing a page design or specification, include:

1. **Decision and audience.** One sentence: what decision, for whom, by when.
2. **Key message.** One complete sentence, with number, comparison, time, and consequence.
3. **Title.** Three lines: who, what, when. Descriptive, not evaluative.
4. **Structure.** The MECE argument or storyline, including the order of evidence.
5. **Visual specification.** Chart/table family, axes, scales, series, tiers, sorting, and why this family fits.
6. **Semantic encoding.** Scenario fills, measure widths, variance signs/colors, markers, formats, `N/A` handling.
7. **Text elements.** Subtitle, legend/label placement, annotations with references, footnotes, source.
8. **Integrity checks.** Which checks passed; which trade-offs and deferred topics remain.
9. **Open trade-offs.** What is omitted, approximated, or dependent on missing data.

Use `assets/page-spec-template.md` when a full specification is useful.

### Audit output

When reviewing, include for each finding:

- **Finding:** what is wrong.
- **Severity:** critical / major / minor.
- **Rule ID:** the specific IBCS rule.
- **Evidence:** the exact observation, value, or comparison on the page.
- **Fix:** a concrete change, with the expected result.
- **Residual risk:** what remains uncertain after the fix.

Order by severity. If the page has a critical integrity failure, say so first and stop the cosmetic review until it is fixed.

## Closed-book fallback

When the skill does not contain an answer:

1. **Check the completeness map** (`references/completeness-map.md`) for the rule ID and the relevant rule file.
2. **Check the semantic notation, chart catalog, and audit checklist** for an established pattern.
3. **If the topic is deferred in v2.0**, say “Not specified in v2.0” and name the gap. Then derive a consistent treatment from the closest specified rule, and label the derivation as a recommendation, not an IBCS rule.
4. **Do not invent** a rule ID, color, threshold, exception, chart type, or source page. Do not imply that a local convention is normative.
5. **If the answer genuinely requires the source PDF** (for example, a figure-only detail), state exactly what is missing and why. Do not make the PDF the normal working path.
6. **For tool-specific gaps**, state the native limitation and give a tested workaround. Do not claim native support that does not exist.

## Honesty rules

- **Separate the three authorities.** ISO 24896 requirements, IBCS rules, and your own design suggestions are different. Label them.
- **Cite rule IDs.** Use exact numbering (`UN 4.1`, `CH 1.1`, `EX 2.1`) so the reader can verify.
- **Cite the source page when explaining a rule.** The rule files give a page (for example, `UN 4.1, p. 49–55`). Include it when the task is retrieval, explanation, or audit. If you cannot confirm the page, say so.
- **Verify the ID before citing it.** Check the valid ranges above or the completeness map. An invented ID is worse than no ID.
- **Do not invent rules.** If the standard does not specify something, say so. “Not specified in v2.0” is a valid, useful answer.
- **Do not invent quantification.** If you say a visual exaggerates a difference by a factor, show the calculation. Otherwise describe the distortion qualitatively.
- **Do not overclaim certification.** This skill is not ISO-certified, not legally binding, and not endorsed by the IBCS Association or the authors.
- **Name tool limitations.** If a tool cannot produce outlined or hatched columns natively, say so and offer a workaround.
- **Protect the message.** A visually perfect page that hides the decision is still a failure. Composition outranks decoration.
- **Respect the data.** Do not adjust scales, labels, or colors to make a weak result look stronger.

## Source and license

**Citation:** *International Business Communication Standards (IBCS) Version 2.0*, Rolf Hichert and Jürgen Faisst, IBCS Media, Hilden, 2026, ISBN 978-3-9821414-4-2, 169 pages, version date 2026-07-02, CC BY-SA 4.0.

**License:** This skill is a derivative work licensed under CC BY-SA 4.0. See `LICENSE` and `references/source-and-license.md` for attribution, the derivative-work notice, the ISO caveat, the source page map, verification instructions, and the changelog.

**ISO caveat:** ISO 24896 is a separate standard. This skill does not reproduce its text and does not claim ISO certification or legal compliance. For formal compliance, consult the ISO standard and the current IBCS source.
