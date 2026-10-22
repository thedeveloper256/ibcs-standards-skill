# Composition Playbook

Notation makes a page truthful. Composition makes it useful. This playbook covers the four composition principles — SAY, STRUCTURE, EXPRESS, CONDENSE — and the page patterns that combine them.

**Source:** IBCS v2.0, pages 78–156. Rule IDs point to the detailed entries in `rules/`.

## 1. SAY — Convey the message

### 1.1 Goals and audience

Start with two questions:

1. **What is my goal?** To inform about a detection, to make the audience understand a problem, or to obtain a decision and cause action. The ultimate goal is a decision; a page that only reports numbers has not yet done the job.
2. **Who is the audience?** Their function, position, knowledge, experience, attitudes, behavior, worries, and cultural background determine what they need. Ask who might disagree with the message and why.

**Rule IDs:** SA 1.1, SA 1.2.

### 1.2 Situation → complication → question → answer

A good introduction follows four moves:

1. **Situation:** the facts and goals the audience already accepts. Start with a positive or widely accepted description to prevent early contradiction.
2. **Complication:** the challenge or problem that affects the audience.
3. **Question:** the relevant question from the audience's perspective.
4. **Answer:** the key message that answers the question.

**Rule IDs:** SA 2.1, SA 2.2, SA 2.3, SA 3.1.

### 1.3 Message types

| Type | What it does | Example |
|---|---|---|
| Detection | States a checkable fact or finding. | “Net sales were 6.2 mEUR below plan in 2026.” |
| Explanation | Gives reasons for a detection. | “The gap is driven by volume loss in the North, not by price.” |
| Suggestion | Recommends a decision or action. | “Approve a targeted promotion in the North in Q1 2027.” |

Use a complete sentence. A detection should be precise enough to be checked; an explanation or suggestion adds more value than a bare number.

**Rule ID:** SA 3.1.

### 1.4 Message first

Put the key message before the evidence. Every report, presentation, dashboard, page, or exhibit can be summarized in one clear overall message; the audience should not have to wait until the end to hear it.

**Caution:** in presentations (not written reports) involving negative, unexpected, or unpleasant messages, such as layoffs, or in cultural contexts where directness may be impolite, build context before stating the message. Do not bury it.

**Rule ID:** SA 3.2.

### 1.5 Support the message

- **Evidence:** use facts, figures, charts, tables, and images that directly support the claim. A slide should explain or prove the message by itself.
- **Precise words:** avoid vague “relevant” or “significant” (in common speech). Use quantities, comparisons, periods, and sources.
- **Highlight:** underline or emphasize the important facts with consistent markers. A page without highlights tends to be statistics, not a message.
- **Sources:** name them in footnotes. Projected slides may omit them; written reports, handouts, and dashboards must include them.
- **Annotations:** use them in written reports, handouts, and dashboards; link each to the part it explains. Slides may rely on the speaker.

**Rule IDs:** SA 4.1–4.5.

### 1.6 Summarize and explain consequences

- In a presentation, repeat the key message at the end in one sentence. Do not end with “Thank you for your attention.”
- Explain the proposed decision, its consequences, and its implications. The real objective is to convince the audience of both the message and the next steps.
- In written reports and dashboards, do not repeat the message mechanically; readers can return to the summary.

**Rule IDs:** SA 5.1, SA 5.2.

### 1.7 Templates

**Key message sentence:**

`<Subject> <verb> <magnitude> <comparison> <time>, <consequence>.`

Example: “Net sales grew 8.4% to 124 mEUR in 2026, 3.1 pp above plan, driven by Wholesale.”

**Executive summary page:**

1. Key message (one sentence).
2. Three to five supporting findings, each with evidence.
3. One chart or table that proves the main finding.
4. Decision requested, consequences, and next step.
5. Sources and definitions.

**Presentation opening:**

1. Situation in one or two sentences.
2. Complication in one sentence.
3. Question in one sentence.
4. Answer (key message) in one sentence.

**Presentation closing:**

1. Repeat the key message.
2. State the decision requested.
3. Explain the consequences and implications.
4. State the next step and owner.

## 2. STRUCTURE — Organize the content

### 2.1 Consistency

- **Items:** group like with like.
- **Statements:** do not mix detections, explanations, and suggestions in one list.
- **Wording:** use the same grammatical pattern, especially in lists.
- **Visualizations:** use the same visual form for the same content.

**Rule IDs:** ST 1.1–1.4.

### 2.2 MECE

A structure is **mutually exclusive (ME)** when its elements do not overlap, and **collectively exhaustive (CE)** when they cover the whole topic. Together they form a **MECE** structure.

Check three levels:

1. **Reporting structure:** chapters, sections, and paragraphs should not cover the same aspect.
2. **Business measures:** measures on one hierarchical level should be disjoint. Material costs and cost of goods sold overlap if material costs are a component of COGS; depreciation and fixed costs overlap if depreciation is already in fixed costs.
3. **Structure dimensions:** categories at the same level should be disjoint. Norway, Sweden, Denmark, and Finland overlap with “Nordics” if all appear at the same level.

For exhaustiveness, include all categories or add a labeled remainder (“Rest of…”) and use consistent remainder notation.

**Rule IDs:** ST 2.1–2.3, ST 3.1–3.2.

### 2.3 Hierarchical structures

| Reasoning | Pattern | Best for | Risk |
|---|---|---|---|
| **Deductive** | Statement → comment → conclusion → message; answers “why” | Controversial discussions, demonstrating need for action, strong premises | The audience must reproduce the deduction; the argument collapses if a premise is questionable. |
| **Inductive** | Homogeneous, non-overlapping, exhaustive arguments → key message | Explanatory storylines, grouping evidence | A missing or overlapping argument weakens the conclusion. |

**Rule IDs:** ST 4.1, ST 4.2.

### 2.4 Visualize structure

- In reporting: outlines, dashboards, summaries, tabs.
- In tables: make hierarchy visible in both columns and rows; use indentation, gaps, lines, bold totals, and consistent types.
- In notes: use indentation, numbering, grouping, and annotation references.

**Rule IDs:** ST 5.1–5.3.

## 3. EXPRESS — Choose the proper visualization

### 3.1 Chart vs table

- **Table:** lookup, precision, many exact values, honest and neutral. It does not compete with a chart.
- **Chart:** comparison, pattern, message. A chart is selective and can be biased by data selection, chart type, and highlighting; that is why notation and integrity matter.
- **Rule:** a chart conveying a key message cannot be replaced by a table; a table needed for lookup should not be replaced by a chart with dense labels.

**Rule ID:** EX 1.

### 3.2 Chart selection

Use the selection matrix in `chart-and-table-catalog.md`. The short version:

- Time series → horizontal category axis.
- Structure → vertical category axis.
- Relationship between two measures → scattergram; three measures → bubble chart.
- Composition → stacked columns/bars.
- Scenario comparison → grouped columns/bars, scenario triangles, or a variance tier.
- Relative variance → pins.
- Change in a stock → growth waterfall.
- Variance between periods/scenarios → variance waterfall.
- Calculation scheme → calculation waterfall.
- Many categories → remainder bar.

**Rule IDs:** EX 1.1, EX 1.2.

### 3.3 Replacement rules

| Replace | With | Exception |
|---|---|---|
| Pie/ring | Bars, stacked columns | Point-positioned pie on a map, two or three values, for market size/share. |
| Gauge/speedometer | Bars/columns | Real-time monitoring, semantic current-deviation coloring, clear target, no better alternative. |
| Radar/spider | Bars | Genuine two-dimensional analysis or meaningful circular arrangement. |
| Funnel | Bars or proportional shape | Shape encodes a real process and area is proportional. |
| Spaghetti | Small multiples | Exact height comparison across lines; interactive filtering. |
| Traffic light | Bars, table bars | Binary yes/no or threshold compliance where magnitude is irrelevant. |

**Rule IDs:** EX 2.1–2.5.

### 3.4 Quantitative over conceptual; no text slides

- Prefer charts, photos, and maps to box-and-arrow diagrams that need explanation. Use no more than three or four conceptual representations in an hour, and only when essential.
- Avoid text slides in live presentations. Recite the text or put it in a handout; show definitions or quotes only when they are the subject.

**Rule IDs:** EX 3.1, EX 3.2.

### 3.5 Add comparisons and explain causes

- Add scenarios (plan, previous year) whenever available.
- Add absolute and relative variances with standard notation.
- Explain causes with tree structures, clusters, and correlations; distinguish correlation from causation.

**Rule IDs:** EX 4.1, EX 4.2, EX 5.1–5.3.

## 4. CONDENSE — Increase information density

### 4.1 Small elements

Use the smallest fonts, components, and visuals that remain legible. Smaller visuals leave room for context, not for decoration.

**Rule IDs:** CO 1.1–1.3.

### 4.2 Maximize space

Use narrow margins and reduce empty space, but keep whitespace that provides clarity, structure, and focus.

**Rule IDs:** CO 2.1, CO 2.2.

### 4.3 Add data

- Add data points: a longer series often reveals patterns without hurting comprehension.
- Add dimensions: three or more dimensions can reveal structures, if they remain legible.

**Rule IDs:** CO 3.1, CO 3.2.

### 4.4 Add visual components

| Combination | What it does | Watch out |
|---|---|---|
| **Overlay** | Two or more basic charts share a category axis. | Different value axes are hard to read; integrated variances make labeling and the primary pattern hard to see. Prefer multi-tier when space allows. |
| **Multi-tier** | Secondary (and tertiary) charts sit above/right of the primary on the same category axis. | Each tier needs its own value axis; same units must share the same scale. |
| **Extended** | Additional context charts extend the category axis. | Use the same value axis; keep the relationship real. |
| **Embedded components** | Table bars, sparklines, traffic lights. | Sparklines need proper scaling; traffic lights only for two or three states. |
| **Embedded explanations** | Short text linked to the visual. | In presentations the speaker may provide the explanation. |

**Rule IDs:** CO 4.1–4.5.

### 4.5 Add visuals

- **Small multiples:** same type and same scale; up to around 25; add “Others” beyond that; enlarge a large-value chart rather than changing its scale.
- **Related charts:** different measures with a real relationship; use consistent notation and scaling markers where scales differ; trees for root causes.
- **Chart–table combinations:** each visual adds supplementary information; do not duplicate the same numbers.
- **Charts and tables in text pages:** place them close to the sentence they support; give each a title and, if possible, a key message.

**Rule IDs:** CO 5.1–5.4.

## 5. Page patterns

### 5.1 Page anatomy

1. Key message.
2. Page title line 1: **who** (reporting unit, filters).
3. Page title line 2: **what** (measure(s), unit, analytical annotation).
4. Page title line 3: **when** (period(s), scenario(s), variance(s)).
5. Subtitle, only for multiple visuals.
6. Visual(s).
7. Labels and legends.
8. Annotations.
9. Footnotes and sources.

Titles are descriptive. They identify content; they do not evaluate or state the conclusion. The key message carries the evaluation.

### 5.2 Three-line title formula

**Line 1 — who:** `Group`, `Region North`, `Product A`, `FY2026 plan`, or the active filter.

**Line 2 — what:** `Net sales, EUR m`, `Return on sales, %`, `Headcount`, with the measure in bold and the unit in regular type. In the Markdown examples, whole lines are bold for readability; in production, bold only the measure.

**Line 3 — when:** `Jan–Dec 2026, AC and PL, ΔPL, ΔPL%`, using `&` when scenarios together form one continuous time series (for example, `Jan 2024–Dec 2026, AC & FC, ΔPL`) and “and” when multiple scenarios are shown for every period.

Example:

**Group**
**Net sales, EUR m**
**Jan–Dec 2026, AC and PL, ΔPL, ΔPL%**

### 5.3 Written report vs presentation vs dashboard

| Medium | Primary mode | Key message | Evidence | Annotations | Sources |
|---|---|---|---|---|---|
| Written report | Reading, lookup, traceability | First, repeated in summary | Detailed charts and tables | Required, linked | Required |
| Presentation | Listening, deciding | First, repeated at end; caution for negative/cultural contexts | One clear visual per point; no text slides | Usually spoken | Slides may omit; handout must include |
| Dashboard | Exploration, monitoring | First, consistent position | Interactive filters; same notation and scales | Required where they explain | Required |

### 5.4 Common composition anti-patterns

| Anti-pattern | Problem | Fix |
|---|---|---|
| “Sales” as the title | No who/what/when; not descriptive enough | Three-line title. |
| Takeaway title | Mixes title and message; violates descriptive-title rule | Descriptive title + separate key message. |
| Key message at the end | Audience must wait for the point | Message first (with sensitive-message exception). |
| Text slide | Audience reads instead of listens | Chart, or handout for the text. |
| Pie of many slices | Hard to compare; one-dimensional | Sorted bars or stacked columns. |
| Gauge wall | Low information density; hard comparison | Bars/columns with target and deviation. |
| Rainbow palette | Color has no stable meaning | Semantic palette; one meaning per color. |
| Spaghetti chart | Intersecting lines obscure trends | Small multiples. |
| Chart and table with the same numbers | Redundant, wastes space | Keep the one that serves the purpose; use the other for supplementary data. |
| Small multiples with different scales | False comparison | Identical scale; resize instead. |
| Empty space filled with decoration | Low density, no information | Add relevant data/context or reduce the page. |
| “Thank you for your attention” | Does not close the argument | Repeat the key message and next step. |

## 6. Composition checklist

- [ ] The goal and audience are explicit.
- [ ] The key message is one complete sentence and comes first.
- [ ] The introduction follows situation → complication → question → answer where appropriate.
- [ ] The structure is MECE and hierarchical.
- [ ] The visual matches the analytical question.
- [ ] Inappropriate chart types are replaced, with documented exceptions.
- [ ] Scenarios and variances are added where meaningful.
- [ ] The page uses the three-line descriptive title.
- [ ] Evidence, sources, annotations, and highlights support the message.
- [ ] The conclusion states consequences and next steps for a decision-oriented audience.
- [ ] The page is dense but legible; no decoration displaces data.
