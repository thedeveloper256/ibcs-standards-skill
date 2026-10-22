# Worked Examples

Five complete page specifications. Each shows the same discipline: decide the message, choose the structure, specify the visual, encode meaning, write the text, and verify integrity.

The numbers are illustrative. The notation and reasoning are the point. In the Markdown titles below, whole lines are bold for readability; in production, bold only the measure and keep the unit in regular type (UN 2.2).

## Example 1 — Monthly Sales, AC vs PL, Absolute and Relative Variances

### Context

A consumer-goods company reviews FY2026 with its sales director in January 2027. The director needs to see both the level of sales against plan and where the gap is concentrated, without opening a separate variance report.

### Data shape

- 12 months, January–December 2026.
- Net sales in EUR m.
- Two scenarios: Actual (`AC`) and Plan (`PL`).
- Monthly values range from 8.1 to 13.2 mEUR.
- FY2026 AC: 128.4 mEUR; PL: 134.6 mEUR; absolute variance: −6.2 mEUR; relative variance: −4.6%.

### Decision and message

**Key message:** “Net sales reached 128.4 mEUR in 2026, 6.2 mEUR (4.6%) below plan; the gap is concentrated in Q4.”

The decision is whether to change the Q1 2027 sales plan or fund a recovery action. The page must make the size and timing of the gap obvious in one view.

### Structure

A horizontal three-tier chart on one shared monthly category axis:

1. **Primary tier:** grouped columns for AC and PL.
2. **Secondary tier:** absolute variance columns (`ΔPL`).
3. **Tertiary tier:** relative variance pins (`ΔPL%`).

The tiers answer three questions in order: What happened? How large is the gap in money? How large is the gap relative to plan?

### Visual specification

- Landscape page; the three tiers share the same 12 monthly categories.
- Primary tier height about 55% of the chart area; secondary about 25%; tertiary about 20%.
- Grouped columns: AC and PL overlap; PL is the reference behind AC; each column is 2/3 of the category width, with the reference offset according to creation date.
- Secondary tier: absolute variance columns of the same width as the base columns, on a scale that includes zero; positive bars above the zero line, negative below.
- Tertiary tier: very thin pins; pin head filled to show AC; labels outside the pin in the direction of change.
- Value scales: primary 0–16 mEUR; secondary −2.0 to +1.0 mEUR; tertiary −15% to +10%. Each tier has its own axis and a clear zero line.
- Legend: once, above the primary tier, `AC` solid dark and `PL` outlined. The variance tiers are named in their tier labels, not with a second legend.
- Data labels: label the last month and the extrema; label every variance bar/pin because the variance is the message. Use at most three digits (for example, `−0.8`, `−4.6%`).
- Gridlines: none; the zero line and labels carry the reference.

### Semantic encoding

- `AC`: solid dark fill.
- `PL`: outlined, no fill, dark outline.
- `ΔPL` columns: solid fill because the minuend is AC; the color is green/red/blue by impact; the axis encodes the reference (PL) with a double outline.
- `ΔPL%` pins: the pin body is green/red/blue by impact; the pin head is solid dark to show AC; the axis encodes PL.
- Positive variances carry `+`; negative variances carry `−`. Q4 variances are negative and red.
- Labels use `ΔPL` and `ΔPL%`; no ambiguous `AC-PL` is needed because the title and legend already identify the comparison.
- Grayscale fallback: red → dark gray, green → light gray, blue → medium gray. The signs remain readable without color.

### Text elements

**Page title (three lines):**

**Group**
**Net sales, EUR m**
**Jan–Dec 2026, AC and PL, ΔPL, ΔPL%**

**Key message:** “Net sales reached 128.4 mEUR in 2026, 6.2 mEUR (4.6%) below plan; the gap is concentrated in Q4.”

**Subtitle:** “Monthly development and plan variance.”

**Annotations:**

1. “Q4 accounts for 4.1 mEUR of the 6.2 mEUR annual gap.”
2. “The second half accounts for 5.1 mEUR of the gap; the first half accounts for 1.1 mEUR.”

**Footnotes:** “Source: Sales reporting system, 2027-01-15. Plan version: FY2026 approved budget. EUR m, rounded. ΔPL = AC − PL; ΔPL% = (AC − PL) / PL.”

### Integrity checks

- [ ] Primary, secondary, and tertiary tiers share the same monthly categories.
- [ ] The primary value axis starts at zero; the variance axes include zero and are not truncated.
- [ ] Grouped columns are not a stacked chart; AC and PL are not added together.
- [ ] `ΔPL` and `ΔPL%` are not confused; no percentage-point claim is made for an absolute measure.
- [ ] Every variance sign matches the underlying values; positive variances carry `+`.
- [ ] Colors are semantic; no decorative color appears anywhere else on the page.
- [ ] The page still reads in grayscale.
- [ ] The title is descriptive; the key message is separate.
- [ ] The source and plan version are visible.

### What would be wrong

- Making PL a solid dark column, which would give the reference more visual weight than actual.
- Truncating the primary axis at 8 mEUR to “show the variation.”
- Stacking AC and PL in one column as if they were additive.
- Using a dual-axis line for the relative variance instead of a pin tier.
- Putting a takeaway sentence in the title and omitting the key message.
- Using a rainbow palette for the months.
- Reporting `ΔPL%` without stating the denominator, or computing a percentage against a negative plan value.
- Adding a 12 × 24 table of every month and product to the same page.
- Using a logarithmic axis for absolute sales without the CH 1.2 exception.
- Treating the variance column’s solid fill as sufficient without applying the impact color.

## Example 2 — Structure Analysis with Remainder

### Context

A group sells in 42 countries. The board asks which countries drive net sales in FY2026. A list of all 42 would be unreadable, but omitting the small countries would violate exhaustiveness.

### Data shape

- 42 countries; FY2026 net sales in EUR m; actual only.
- Top 8 countries account for 78% of sales; the remaining 34 countries account for 22%.
- Germany is the largest at 21%; the smallest displayed country is 5.6%.

### Decision and message

**Key message:** “The top 8 countries generated 78% of net sales in 2026; Germany alone contributed 21%, about 1.7 times the next-largest market.”

The decision is where to focus market investment. The page must show the concentration and preserve the full total.

### Structure

A vertical single-bar chart with:

- The top 8 countries sorted by descending sales.
- A remainder bar labeled “Rest of world (34 countries)” at the bottom.
- A wider gap between the eighth country and the remainder bar.

The remainder makes the analysis exhaustive: the bars add to 100% of group sales. A supporting table provides exact lookup and shares.

### Visual specification

- Vertical category axis with country names, horizontal labels.
- One bar per category; bar width 2/3 of category width.
- Horizontal value axis starts at zero; no gridlines; direct labels at the end of each bar.
- The remainder bar uses the same bar width and category height as the other bars but is separated by a gap at least twice the normal category gap; its length encodes the accumulated 28.2 mEUR.
- Germany is highlighted with a blue ellipse; no other country gets a unique color.
- Sort order is descending by value; the remainder is always last.
- Label `Rest of world (34)` on the axis and `22%` at the bar end.

#### Supporting table

The page pairs the chart with a compact table: the chart shows concentration, the table provides exact lookup and shares. Neither repeats the other’s purpose.

| Country | AC 2026 (EUR m) | Share of total | Rank |
|---|---:|---:|---:|
| Germany | 27.0 | 21.0% | 1 |
| USA | 16.0 | 12.5% | 2 |
| China | 14.0 | 10.9% | 3 |
| France | 11.0 | 8.6% | 4 |
| UK | 9.5 | 7.4% | 5 |
| Japan | 8.0 | 6.2% | 6 |
| Brazil | 7.5 | 5.8% | 7 |
| India | 7.2 | 5.6% | 8 |
| Rest of world (34) | 28.2 | 22.0% | — |
| **Total** | **128.4** | **100.0%** | — |

The table uses right-aligned numbers, a separated remainder row, a bold total, and no vertical lines. The remainder is not ranked.

### Semantic encoding

- AC: solid dark fill for all bars, including the remainder.
- No color by country; color would imply a meaning that does not exist.
- The blue ellipse is a highlighting marker for Germany.
- The gap before the remainder is a structural separator, not a value encoding.
- Labels use one decimal and the unit stated in the title; no thousands separators are needed at these magnitudes.
- Remainder is labeled as a remainder, not as a country.

### Text elements

**Page title (three lines):**

**Group**
**Net sales, EUR m**
**FY2026, AC**

**Key message:** “The top 8 countries generated 78% of net sales in 2026; Germany alone contributed 21%, about 1.7 times the next-largest market.”

**Subtitle:** “Top 8 countries and remainder, sorted by sales.”

**Annotation:** “Rest of world combines 34 countries, each below 7.2 mEUR (5.6%). The remainder is excluded from the country ranking and average.”

**Footnote:** “Source: Group sales consolidation, 2027-01-20. FY2026 actual. EUR m, rounded. Top 8 + rest of world = 100% of group sales.”

### Integrity checks

- [ ] The bars are sorted descending; the remainder is last.
- [ ] Top 8 plus remainder equals 100% of group sales.
- [ ] The remainder is separated by a wider gap and labeled as a remainder.
- [ ] The value axis starts at zero.
- [ ] Bar widths are consistent; the remainder is not drawn wider or taller.
- [ ] Germany is highlighted without giving it a different data color.
- [ ] The remainder is excluded from ranking and averaging.
- [ ] No pie chart, 3D effect, or rainbow palette.

### What would be wrong

- Showing 42 countries with unreadable labels.
- Showing the top 8 and silently dropping the other 34, so the chart does not add to 100%.
- Calling the remainder a country or ranking it among countries.
- Sorting alphabetically when the message is concentration.
- Using a different color for every country.
- Using a pie chart or a colored map for country shares; the map would imply that area is the measure (CH 3.3, EX 2.1).
- Starting the value axis above zero.
- Including the remainder in the average or in a “top 10” ranking.

## Example 3 — P&L Calculation Waterfall

### Context

The management board reviews the FY2026 actual P&L. The CFO wants to show how sales becomes net income, with the main cost blocks visible, and to make the cost intensity clear without a second table.

### Data shape

- FY2026 actual, EUR m.
- Net sales: 128.4.
- Material costs: −42.1.
- Personnel costs: −31.7.
- Other operating costs: −18.6.
- EBITDA: 36.0.
- Depreciation: −7.2.
- EBIT: 28.8.
- Interest: −2.1.
- EBT: 26.7.
- Tax: −5.9.
- Net income: 20.8.

### Decision and message

**Key message:** “Net income reached 20.8 mEUR (16.2% of sales) in 2026; material and personnel costs consumed 57.5% of sales.”

The board is deciding whether to approve a cost program. The page must make the size of the cost blocks relative to sales visible.

### Structure

A vertical calculation waterfall:

- Base bar: net sales.
- Contribution bars: material, personnel, other operating costs, depreciation, interest, tax.
- Subtotals: EBITDA, EBIT, EBT.
- Total: net income.

The sequence follows the calculation scheme, not a time or structure dimension.

### Visual specification

- Vertical category axis with the P&L lines in calculation order.
- Base and total bars: 2/3 of the category width, solid dark.
- Contribution bars: same 2/3 width, neutral mid-gray; negative contributions extend from the preceding cumulative value to the left, positive contributions to the right.
- Subtotals: solid dark, bold labels, separated by a light horizontal line.
- Assisting lines connect the end of each bar to the start of the next.
- Value axis starts at zero and extends to at least 140 mEUR; the bridge stays on one scale.
- Data labels at the end of each bar: `128.4`, `−42.1`, `−31.7`, `−18.6`, `36.0`, `−7.2`, `28.8`, `−2.1`, `26.7`, `−5.9`, `20.8`.
- A right-hand annotation column states `% of sales`: 100.0, 32.8, 24.7, 14.5, 28.0, 5.6, 22.4, 1.6, 20.8, 4.6, 16.2.

### Semantic encoding

- Actual base and total bars: solid dark.
- Contribution bars: neutral gray, because this is a calculation scheme, not a variance analysis. Do not color costs red merely because they reduce profit; red would imply an unfavorable variance that is not being measured.
- If the page also compared AC with PL, variance colors would apply only to the variance bars, not to the calculation contributions.
- Signs: negative contributions carry `−`; positive contributions carry `+` only when they are framed as variances. In this neutral calculation, the direction and label carry the sign.
- Percent-of-sales figures are ratios, not variances; do not add percentage points unless comparing two ratios.
- Labels are outside the bars, never inside thin bars.

### Text elements

**Page title (three lines):**

**Group**
**P&L, EUR m and % of sales**
**FY2026, AC**

**Key message:** “Net income reached 20.8 mEUR (16.2% of sales) in 2026; material and personnel costs consumed 57.5% of sales.”

**Subtitle:** “Calculation from net sales to net income.”

**Annotations:**

1. “Material and personnel costs together are 73.8 mEUR, 57.5% of sales.”
2. “EBITDA margin is 28.0%; depreciation and interest reduce it to an EBT margin of 20.8%.”

**Footnote:** “Source: Consolidated P&L, 2027-02-05. FY2026 actual. EUR m, rounded. Percentages are calculated on net sales. Totals may not add due to rounding.”

### Integrity checks

- [ ] The bridge is additive: 128.4 − 42.1 − 31.7 − 18.6 = 36.0; 36.0 − 7.2 = 28.8; 28.8 − 2.1 = 26.7; 26.7 − 5.9 = 20.8.
- [ ] The value axis starts at zero and uses one scale for all bars.
- [ ] No component is clipped or broken.
- [ ] Base, contribution, subtotal, and total bars are visually distinct.
- [ ] Assisting lines connect successive bars.
- [ ] Labels are outside the bars and readable.
- [ ] Percentages use the same sales base and are labeled as `% of sales`.
- [ ] The page does not imply that costs are “bad” by using variance red.

### What would be wrong

- Coloring every cost contribution red as if it were an unfavorable variance.
- Omitting EBITDA, EBIT, or EBT subtotals so the reader cannot follow the calculation.
- Using a pie chart to show cost composition, which loses the calculation sequence.
- Truncating the value axis or breaking a bar.
- Labeling percentages without stating the base.
- Using 3D or decorative gradients.
- Showing the same numbers again in a table that adds nothing.
- Using full-width bars for absolute measures instead of 2/3 of the category width.
- Comparing multi-year values without showing inflation or currency effects where they materially change the conclusion (CH 5.1–5.2).

## Example 4 — KPI Dashboard with Small Multiples

### Context

A group sales director reviews six regions monthly. The board pack needs one page that shows whether the regions are on plan and where the gap is concentrated, without six unrelated charts.

### Data shape

- Six regions: North, West, South, East, Central, Export.
- 12 months, January–December 2026.
- Net sales in EUR m; AC and PL.
- Same unit and comparable scale; monthly values between 0.4 and 5.8 mEUR per region.
- Group AC: 128.4 mEUR; PL: 134.6 mEUR; gap: −6.2 mEUR.

### Decision and message

**Key message:** “Five of six regions finished below plan; North accounts for 61% of the 6.2 mEUR group gap.”

The decision is where to deploy the Q1 2027 recovery budget. The page must show both the pattern in each region and the relative size of each region's gap.

### Structure

A 2 × 3 grid of small multiples:

- Same chart type in every panel: grouped columns for AC and PL.
- Same monthly x-axis and same value scale (0–6 mEUR) in every panel.
- Each panel has its own subtitle with the region name and its own `ΔPL` label.
- The overall page has one key message and one title.

### Visual specification

- Landscape page; 2 columns × 3 rows; equal panel sizes.
- Each panel: 12 monthly categories; AC solid dark, PL outlined; grouped columns; no gridlines.
- Same scale across all panels; a shared scale band or a note states `0–6 mEUR` once.
- Each panel labels only the last month and the largest absolute variance; the panel subtitle carries the region total.
- North is highlighted with a blue ellipse around its largest negative variance and an annotation.
- Shared legend at the top: `AC` solid dark, `PL` outlined.
- Footer: source, period, plan version, and a note that all panels share the same scale.

### Semantic encoding

- AC: solid dark; PL: outlined; no region gets its own color.
- Negative `ΔPL` values are red; positive values are green; the sign is always shown.
- North's annotation uses a blue highlighting ellipse and an annotation reference; the ellipse does not replace the variance color.
- All panels use the same bar widths (2/3 category width) and the same category spacing.
- Grayscale fallback: the signs and the ellipse remain visible; red/green become dark/light gray.

### Text elements

**Page title (three lines):**

**Group**
**Net sales, EUR m**
**Jan–Dec 2026, AC and PL, ΔPL**

**Key message:** “Five of six regions finished below plan; North accounts for 61% of the 6.2 mEUR group gap.”

**Panel subtitles:** `North`, `West`, `South`, `East`, `Central`, `Export`, each with the region's `ΔPL` total.

**Annotation:** “North is 3.8 mEUR below plan; its Q4 gap alone is 2.2 mEUR.”

**Footnote:** “Source: Regional sales reporting, 2027-01-18. FY2026 plan version 3. EUR m, rounded. All panels use the same 0–6 mEUR scale; group total includes consolidation effects.”

### Integrity checks

- [ ] All six panels use the same chart type, x-axis, and value scale.
- [ ] The value axis starts at zero.
- [ ] The 2 × 3 grid is readable at print size; no panel is too small for its labels.
- [ ] Each panel has a title and a `ΔPL` total; the overall page has one key message.
- [ ] Colors mean scenario or variance, not region.
- [ ] North's highlight is a marker, not a data color.
- [ ] The page survives grayscale and color-vision checks.
- [ ] The group total is reconciled with the panel totals; consolidation effects are footnoted.

### What would be wrong

- Giving each panel a different scale so small regions look as large as big ones.
- Using a different chart type per region.
- Replacing the panels with six gauges or six pie charts.
- Using one color per region, so color no longer means scenario or variance.
- Omitting the overall key message and leaving six unrelated charts.
- Making the page so dense that labels are unreadable.
- Forgetting the consolidation reconciliation between regional and group totals.

## Example 5 — Executive Summary Slide

### Context

The board must decide whether to fund a targeted promotion in the North region for Q1 2027. The CFO and sales director present a one-slide summary. The audience is senior, skeptical of unsubstantiated claims, and short on time.

### Data shape

- FY2026 North net sales bridge, EUR m: PL 42.0; volume effect −2.9; price effect +0.7; mix effect −1.6; AC 38.2.
- Net gap: −3.8 mEUR.
- Proposed action: targeted North promotion; expected recovery 2.4 mEUR in Q1 2027; cost 0.6 mEUR; net expected benefit 1.8 mEUR.
- Risk: competitor response could reduce the recovery by up to 0.8 mEUR.

### Decision and message

**Key message:** “North net sales are 3.8 mEUR below plan, driven mainly by volume; approve a targeted North promotion expected to recover 2.4 mEUR in Q1 2027 for a net benefit of 1.8 mEUR.”

The decision is a clear yes/no on the promotion. The slide must give the evidence, the consequence, and the next step without becoming a text slide.

### Structure

A three-part slide:

1. **Top:** key message in one sentence.
2. **Middle:** one variance waterfall from PL to AC for North, showing volume, price, and mix effects.
3. **Bottom:** three short consequence lines — decision requested, expected net benefit, main risk — plus the next step and owner.

No bullet list of background facts; the speaker provides the narrative.

### Visual specification

- Landscape slide; key message across the top in one or two lines.
- Variance waterfall: PL 42.0 base; volume −2.9; price +0.7; mix −1.6; AC 38.2 total.
- Horizontal category axis with the bridge categories; value axis starts at zero; assisting lines connect the bars; bars use 2/3 category width (absolute measure).
- Base PL bar outlined; AC total bar solid dark; contribution bars solid (minuend AC) and colored green/red/blue by impact; labels outside the bars with signs.
- Bottom band: three short lines, each with a label and a number; no paragraph text.
- Footnote with source, plan version, and the basis for the 2.4 mEUR recovery estimate.

### Semantic encoding

- PL base: outlined; AC total: solid dark.
- Contribution bars: solid fill because the minuend is AC; color by impact.
- Volume −2.9: undesirable, red.
- Price +0.7: desirable, green.
- Mix −1.6: undesirable, red.
- Labels: `−2.9`, `+0.7`, `−1.6`; the gap `−3.8` is stated in the key message and annotated next to the AC bar.
- The expected recovery is a forecast, not an actual: if shown as a bar, it must be outlined + hatched (`FC`), never solid dark.
- The promotion cost is a plan/forecast outflow, not an actual; label it and use the appropriate outline/hatch if visualized.
- Color is reserved for variance impact; the decision lines use neutral text.

### Text elements

**Page title (three lines):**

**Group — North**
**Net sales, EUR m**
**FY2026, AC and PL, ΔPL**

**Key message:** “North net sales are 3.8 mEUR below plan, driven mainly by volume; approve a targeted North promotion expected to recover 2.4 mEUR in Q1 2027 for a net benefit of 1.8 mEUR.”

**Bottom band:**

- **Decision:** Approve 0.6 mEUR promotion budget for North, Q1 2027.
- **Expected net benefit:** 1.8 mEUR (2.4 mEUR recovery − 0.6 mEUR cost).
- **Main risk:** Competitor response; recovery could be 0.8 mEUR lower.
- **Next step:** Regional director to submit execution plan by 2027-02-15.

**Footnote:** “Source: FY2026 North sales bridge, 2027-01-25; Q1 2027 recovery estimate from regional sales model v4. PL = approved FY2026 plan. EUR m, rounded. Recovery is a forecast and is not yet in the plan.”

### Integrity checks

- [ ] The bridge adds: 42.0 − 2.9 + 0.7 − 1.6 = 38.2.
- [ ] The total gap is −3.8 and is consistent with the key message and Example 4’s North gap.
- [ ] The page is titled as North, and every bridge number is North-level, not group-level.
- [ ] The value axis starts at zero; no bar is clipped.
- [ ] PL is outlined; AC is solid dark; forecast is outlined + hatched if shown.
- [ ] Red/green/blue are applied to variance impact, not to arbitrary categories.
- [ ] The slide is not a text slide; the bottom band has short decision lines, not bullet paragraphs.
- [ ] The expected benefit is labeled as an estimate, with its basis and risk.
- [ ] The next step has an owner and a date.
- [ ] Sources and plan version are visible.

### What would be wrong

- A slide of bullet points with no evidence chart.
- Ending with “Thank you for your attention” instead of the decision and next step.
- Showing the recovery as a solid actual bar, implying it has already happened.
- Hiding the 0.8 mEUR risk or presenting the 1.8 mEUR benefit as certain.
- Using a pie chart or a gauge for the bridge.
- Mixing group-level and North-level numbers under a North title.
- Making the title a takeaway sentence and omitting a separate key message.
- Leaving the decision, owner, and date implicit.
