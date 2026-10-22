# Semantic Notation

This is the working reference for IBCS notation. It encodes content so that similar things look similar and different things look different. Color, fill, width, orientation, and markers all carry meaning; none of them is decoration.

**Source:** IBCS v2.0, pages 40–67, with supporting details from pages 24–39. ISO 24896 defines the normative notation requirements; this is a practical summary.

## 1. Scenario notation

| Scenario | Abbreviation | Fill | Meaning | Typical use |
|---|---|---|---|---|
| Actual | `AC` | **Solid dark** | Measured data about the present or past. | Current performance, actuals to date. |
| Previous period | `PY` | **Solid light** | Measured data from an earlier period. | Scenario comparison where the earlier period is the reference. |
| Plan | `PL` | **Outlined** (no fill or white fill; dark outline) | Fictitious, planned data. | Target, budget, plan. |
| Budget | `BU` | **Outlined** | Fictitious, budgeted data. | Budget where it is distinct from plan. |
| Forecast | `FC` | **Outlined + hatched** (dark hatch stripes) | Expected data, partly fictitious but based on measured data. | Latest estimate, forecast. |

**Rules.**

- Use the same notation across charts, tables, and text.
- The outline of plan/budget suggests that the area will “fill up” when actual data materializes.
- Forecast keeps the outline and adds dark hatch stripes; the stripe color corresponds to measured data.
- In a time series with multiple periods, do not lighten every earlier period; the light previous-period fill is for a scenario comparison, not for ordinary history.
- Exact color codes are not prescribed. Keep the chosen values consistent within the organization; `assets/starter-tokens.json` is a non-normative starting point.

## 2. Stacked charts

- Apply scenario notation to the **lowest segment** of each stacked column/bar.
- Fill the upper segments with different **gray shades** so the segments remain distinguishable.
- If an upper segment is plan/budget or forecast, add the corresponding **outline** or **hatch**.
- Use stacked columns/bars only when all values have the same sign.
- Position the most important data series directly on the axis.

## 3. Scenario comparisons

- Arrange scenarios of different periods in **temporal ascending order**.
- For the same period, order scenarios by **creation date**.
- Use scenario labels (`AC`, `PY`, `PL`, `BU`, `FC`) rather than year labels in the comparison; state the period in the title, legend, or header.
- Keep `AC` and `FC` in the **foreground**; place the reference scenario behind them.
- A third scenario can be shown with a **scenario triangle**.
- Encode the **reference scenario on the axis**: outlined axis for plan/budget, solid light axis for previous year.
- Encode the **minuend in the fill**: solid for AC, hatched for FC, outlined if PL is the minuend.

## 4. Measures

| Measure type | Column/bar width | Line weight | Example |
|---|---|---|---|
| Absolute measure | **2/3 of category width** | Thick line | Sales in EUR, headcount, volume. |
| Relative measure (ratio, share) | **1/3 of category width** (half the absolute width) | Thin line (50% of thick) | Return on sales, market share. |

- A ratio has the same unit in numerator and denominator and is expressed in percent.
- A share has the same absolute measure in numerator and denominator.
- The width/line-weight distinction lets readers recognize the measure type without reading the label.
- V2.0 does not yet specify a comprehensive notation for other measure types (value/volume, flow/stock, desirable/undesirable impact). State the gap; do not invent normative rules.

## 5. Variances

### 5.1 Absolute variance

- `ΔPL` = the difference between a scenario and plan: `AC-PL` or `FC-PL`.
- `ΔPY` = the difference between a scenario and previous year: `AC-PY` or `FC-PY`.
- If it is unclear whether AC or FC is compared to plan, write `AC-PL` or `FC-PL`.
- Put `+` on positive variances. Negative variances carry the minus sign.
- Use the same width and scale as the base columns/bars.
- Label outside the variance component in the direction of increase/decrease.
- **Color** the variance by impact: green, red, or blue.
- **Fill pattern** follows the minuend: solid for AC, hatched for FC, outlined for PL. A solid green/red variance column means the minuend is AC; a hatched green/red column means FC; an outlined green/red column means PL is the minuend.

### 5.2 Relative variance

- `ΔPL%` = `(AC-PL)/PL*100` or `(FC-PL)/PL*100`.
- `ΔPY%` = `(AC-PY)/PY*100` or `(FC-PY)/PY*100`.
- If ambiguous, write `(AC-PL)%` or `(FC-PL)%`.
- Put `+` on positive values.
- Display as a **thin pin** (vertical pin for structure, horizontal pin for time).
- The **pin body** is colored by impact (green/red/blue); the **pin head** uses the minuend's scenario fill (solid dark for AC, hatched for FC, outlined for PL).
- The axis shows the reference scenario.
- Use `N/A` when a relative variance cannot be interpreted, such as a positive value compared with a negative denominator. Do not compute a misleading percentage.

### 5.3 Ratio variances in percentage points

When the underlying measure is itself a ratio or percentage, the **absolute** variance is expressed in **percentage points (pp)**, not percent:

`AC 50% − PL 40% = +10 pp`.

A relative variance of a ratio can still be expressed as a percentage if the denominator is meaningful; do not confuse the two.

### 5.4 Variance colors

| Impact | Color | Grayscale fallback |
|---|---|---|
| Desirable | **Green** | Light gray |
| Undesirable | **Red** | Dark gray |
| Neutral / ambiguous | **Blue** | Medium gray |

- Color is semantic, not arithmetic: a positive cost variance can be undesirable (red), a negative cost variance can be desirable (green).
- In grayscale, use the fallbacks above.
- For color-vision deficiency, use blue-green in place of green and/or add a non-color cue (sign, shape, label).
- Never rely on color alone; the sign, label, and position must already carry the message.

### 5.5 Variance layout

- Variance columns/bars use the same width and scale as the base.
- Relative variances use thin pins, not full-width columns/bars.
- Labels sit outside the component in the direction of change.
- For absolute variances, the **fill pattern** encodes the minuend: solid for AC, hatched for FC, outlined for PL. The **color** encodes impact: green/red/blue. The **axis** encodes the reference scenario: outlined (two parallel lines) for PL/BU, solid light for PY.
- For relative variances, the pin body color encodes impact; the pin head fill encodes the minuend; the axis encodes the reference.
- Keep variance scales consistent across the page.

## 6. Time periods and time-series analyses

### 6.1 Orientation and period notation

- Time runs **left to right** on horizontal axes and in table columns.
- Dates: `YYYY-MM-DD` (ISO 8601).
- Periods: `YYYY`, `YYYY-Qn`, `YYYY-MM`.
- First day of a period: leading full stop (`.2026`, `.Jun`).
- Last day of a period: trailing full stop (`2026.`, `Jun.`).
- A span: two full stops (`Jan..Mar`), not an ellipsis.
- Category width can encode the period type: a year is wider than a quarter, a quarter wider than a month. Keep the allocation consistent at least across a page.

### 6.2 Analysis markers

| Analysis | Marker | Example |
|---|---|---|
| Year-to-date | Underscore prefix | `_Jun 2026` |
| Year-to-date average | Underscore prefix + average marker | `_Jun 2026` plus the organization's average sign |
| Last date value (stock) | Underscore prefix + trailing full stop | `_Jun 2026.` |
| Year-to-go | Underscore suffix | `Jun 2026_` |
| Moving analysis | Tilde prefix | `~Jun 2026` |
| Moving annual total | `MAT` | `MAT Jun 2026` |
| Moving annual average | `MAA` | `MAA Jun 2026` |
| Temporal indexing | Black arrowhead pointing right at the index point; `100%` or `100` to its left | `100% →` at the reference period |

The exact average glyph is not prescribed; use the organization's standard marker consistently.

## 7. Structure analyses

- Put structure dimensions on **vertical axes**; keep labels horizontal. Time is the horizontal axis.
- **Averaging:** append or prefix the organization's average sign; add an assisting line if helpful.
- **Ranking:** mark with an arrow (`country names↓`, `product sales↑`).
- **Selecting:** v2.0 does **not** specify a visualization. Describe the selection in text or use an accepted local convention; do not invent a normative marker.
- **Indexing:** black arrowhead near the index point, with `100%` or `100` next to it.
- **Normalizing:** assisting line representing 100%, with a black arrowhead at one end and `100%` or `100` next to the arrowhead.

## 8. Adjustment analyses

- Use adjustment analyses to neutralize currency, inflation, or seasonal effects.
- Recalculate one scenario with factors from another, for example, actual sales at previous-year exchange rates.
- Show both adjusted and unadjusted values and explain the adjustment.
- **Visualization gap:** v2.0 does not prescribe a specific visualization for adjustment analyses. Do not invent one; use the closest established notation and label the adjustment.

## 9. Markers

| Marker | Purpose | Design |
|---|---|---|
| Assisting line/area | Separate, group, or coordinate content | Light, consistent; can carry scenario design on the axis |
| Difference marker | Highlight the distance between two assisting lines | Two parallel lines projecting the length; marker between them; green/red/blue by impact; arrowhead optional |
| Trend arrow | Show the direction and magnitude of a trend | Starts at the first period, ends at the last; arrowhead in the time direction; optional calculation label such as `CAGR: 10.8%`; color by impact |
| Highlighting ellipse | Emphasize a specific value | Blue ellipse |
| Reference arrowhead | Point to an index or benchmark | Arrowhead close to the reference point; label (`100%`, `Market avg.`) next to it |
| Annotation reference | Link an annotation to the content it explains | Consistently designed paired markers |
| Scale band | Make different scales comparable | Line parallel to the category axis at the same numerical height; light fill between line and axis |
| Outlier marker | Show a value beyond the visible scale without scaling the chart to it | Omit the pin head; add a triangle pointing in the direction of growth |

Standardize and document any additional marker in the organization's notation manual.

## 10. Text, numbers, units, and dates

- **Numbers:** narrow blank space as thousands delimiter (`1 234`); decimal comma or point consistently (`1,23` or `1.23`). At most three digits in charts and four in tables; otherwise round or use prefixes.
- **Negative values:** one format throughout, either `-123` or `(123)`.
- **Positive values:** no plus sign unless the value is a variance.
- **Currencies:** ISO 4217 codes (`EUR`, `CHF`, `USD`, `GBP`). Avoid special currency symbols when multiple currencies appear.
- **Metric prefixes:** lowercase `k`, `m`, `b` for monetary values; state the unit in the title or header.
- **Physical units:** SI units, consistent and stated.
- **Dates:** ISO 8601 `YYYY-MM-DD`.
- **Percentages:** state the base; use `pp` for percentage-point differences of ratios.

## 11. Accessibility

- Do not rely on color alone: use signs, labels, shapes, or position as redundant cues.
- Use the grayscale fallbacks when the medium is monochrome.
- For color-vision deficiency, replace green with blue-green and/or add a pattern or marker distinction.
- Keep contrast sufficient for text, labels, and fine lines.
- Test the page in grayscale and with a color-vision simulator before publishing.

## 12. Deferred topics

The following are **not specified in v2.0** as complete notation concepts:

- Comprehensive measure-type notation beyond absolute/relative.
- Visualization of adjustment analyses.
- Visualization of selecting in structure analyses.
- Specific notation for area charts.
- Specific notation for boxplot/range charts.
- Specific notation for charts with two value axes.
- Additional scaling visualizations beyond scale bands.

When a task touches one of these, say so explicitly and derive a consistent treatment from the closest specified notation. Do not present the derivation as an IBCS rule.

## 13. Encoding checklist

For every visual, confirm:

- [ ] Every scenario has the correct fill: AC solid dark, PY solid light, PL/BU outlined, FC outlined + hatched.
- [ ] Stacked charts apply scenario notation to the lowest segment; upper segments use gray shades.
- [ ] Absolute measures use 2/3 category width; relative measures use 1/3; lines are thick vs thin (50%).
- [ ] Absolute variances use `ΔPL`/`ΔPY` or explicit `AC-PL`/`FC-PL`; relative variances use `ΔPL%`/`ΔPY%`.
- [ ] Positive variances carry `+`; ratio variances use percentage points; negative denominators show `N/A`.
- [ ] Variance colors are green/red/blue with the documented grayscale fallbacks.
- [ ] Time runs left to right; period abbreviations are consistent; category widths respect period length.
- [ ] Structure categories sit on a vertical axis with horizontal labels.
- [ ] YTD/YTG/moving/indexing markers are consistent and correctly placed.
- [ ] Markers (assisting lines, difference, trend, highlighting, reference, annotation, scale band, outlier) are consistent.
- [ ] Numbers, currencies, units, and dates follow the organizational formats.
- [ ] The page survives grayscale and color-vision checks.
