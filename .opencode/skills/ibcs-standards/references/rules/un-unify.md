# UNIFY — Apply Semantic Notation

UNIFY covers all aspects of applying semantic notation. Similar content should look similar; what looks the same should mean the same. If the content is not the same, it should not look the same.

IBCS v2.0 aligns the notation rules with ISO 24896 “Notation for business reporting.” ISO 24896 defines normative requirements; IBCS provides explanations, design rules, and examples for practical application.

**Source:** IBCS v2.0, pages 24–67.

## UN 1 — Unify terminology

Terms are the non-visual part of business communication. Standardize terms, abbreviations, number formats, units, and dates across reports, dashboards, and presentations.

### UN 1.1 — Unify terms and abbreviations

**Requirement.** Use unambiguous language and a corporate glossary to unify terms and abbreviations.

**Why.** Different terms for the same concept force readers to translate; a glossary removes that effort and prevents different translations in international organizations.

**Apply.** Compile and explain all terms and abbreviations in an easily accessible glossary. Include definitions and, for international organizations, translations. Define short abbreviations for column headers (e.g., `A/R` for Accounts Receivable) and longer abbreviations for row headers (e.g., `Acc. Receiv.`).

**Exceptions / limits.** None stated in v2.0.

**Audit.** Are all recurring terms and abbreviations defined and used consistently?

**See also.** UN 1.2, UN 3.2, UN 3.3.

**Source.** p. 25.

### UN 1.2 — Unify numbers, units, and dates

**Requirement.** Standardize number formats, currency and physical units, and date notation within the organization.

**Why.** Consistent formats improve legibility and avoid unnecessary cognitive effort.

**Apply.** Use one number format: a narrow blank space as the thousand delimiter (`1 234`) and either a comma or a point as the decimal sign (`1,23` or `1.23`, per ISO 80000-1). Limit charts to three digits and tables to four; use currency and metric prefixes. Use one negative format, either `-123` or `(123)`. Do not put a plus sign on positive values unless they are variances. Use ISO 4217 three-letter currency codes (`EUR`, `CHF`, `USD`, `GBP`) and avoid special currency symbols when multiple currencies appear. Use lowercase single-letter metric prefixes (`k`, `m`, `b`) for monetary values. Use SI units for physical quantities. Use ISO 8601 dates (`YYYY-MM-DD`).

**Exceptions / limits.** SI permits either a comma or a point as the decimal sign. Organizations may use local abbreviations if they are consistent.

**Audit.** Are number, unit, currency, and date formats identical across the report?

**See also.** SI 5.2, UN 3.3.

**Source.** p. 26–27.

## UN 2 — Unify text elements

Text elements describe visuals for better comprehension. ISO 24896 defines requirements for descriptive text elements (titles, legends, labels, footnotes) and explanatory text elements (key messages, annotations).

### UN 2.1 — Unify key messages

**Requirement.** Place the key message in the same position and layout across all reports.

**Why.** A consistent position lets the audience recognize the message immediately.

**Apply.** Choose a standard position, usually at the top of the page above the title or to the right of the title in landscape layouts. Keep the wording, typography, and alignment consistent within the organization.

**Exceptions / limits.** The exact position may depend on the reporting type, but it must remain consistent within an organization.

**Audit.** Is the key message always in the same place and format?

**See also.** SA 3.2, SA 4.3.

**Source.** p. 27–28.

### UN 2.2 — Unify titles and subtitles

**Requirement.** Titles identify the content of pages and visuals completely, using only descriptive language. Page titles have three lines: reporting unit (who), business measure(s) (what), and time period(s), scenario(s), and variance(s) (when).

**Why.** A complete, consistent title lets readers identify the content without reading the whole page; evaluation belongs in the key message, not the title.

**Apply.** Put the reporting unit and filters in line 1, the measure(s) and unit in line 2, and the time/scenario/variance in line 3. Write measures in bold and units in regular font. Use `&` when scenario categories together make up one continuous time series (for example, `Jan 2024–Dec 2026, AC & FC`) and “and” when multiple scenarios are presented for all periods (`AC and PY`). Put page titles at the upper left, under the key message; if space is tight, place them at the same height, preferably left of the message. Use subtitles only when a page has multiple visuals; a subtitle identifies the visual or segment and the categories that differ, and sits above the visual.

**Exceptions / limits.** On screen pages, responsive layouts may combine the three lines with a pipe (`|`). The exact position may vary by organization but must be consistent.

**Audit.** Does the title identify who, what, and when without evaluating? Are subtitles used only where needed?

**See also.** UN 2.3, SA 3.2.

**Source.** p. 28–33.

### UN 2.3 — Unify the position of legends and labels

**Requirement.** Integrate legends into charts where possible, write legends and labels horizontally, and position them consistently by chart type. Position data labels next to their visual components.

**Why.** Standard positions reduce eye movement and speed comprehension.

**Apply.** For single column/bar charts, put the legend in the title. For stacked columns, place legends to the left of the leftmost column or the right of the rightmost column. For stacked bars, center legends above the top bar or below the bottom bar. For line charts, place legends at the line end or close to the line. For charts with two value axes, use external legends next to symbols or integrate them near typical points/bubbles. Put data labels above or below columns, right or left of bars, and outside variance columns/bars in the direction of change. Use leader lines if a label cannot sit next to its component.

**Exceptions / limits.** Assisting lines may be needed when a legend cannot be placed next to its segment.

**Audit.** Are legends and labels horizontal, integrated where possible, and consistently positioned?

**See also.** SI 5.1, SI 5.3, UN 5.1.

**Source.** p. 33–38.

### UN 2.4 — Unify annotations

**Requirement.** Design annotations consistently, integrate them into the visual where possible, and link them to the relevant values or positions with annotation references.

**Why.** Annotations that point directly to the content establish context and speed comprehension.

**Apply.** Use a consistent annotation style and reference design. Place numbered annotations in free areas and link each to the part of the page it explains.

**Exceptions / limits.** Slides shown during a presentation may rely on the speaker instead of annotations; written reports and dashboards need them.

**Audit.** Are annotations consistently designed and linked to the content they explain?

**See also.** SA 4.5, UN 5.1.

**Source.** p. 38–39.

### UN 2.5 — Unify footnotes

**Requirement.** Place footnotes at the bottom of the page and use them for definitions, sources, retrieval dates, and other credibility details.

**Why.** Footnotes make the content verifiable without cluttering the visual.

**Apply.** Use a consistent footnote style and position. Include footnotes in written reports, handouts, and dashboards; presentation slides that support a speaker may omit them, but written material must include them.

**Exceptions / limits.** None stated in v2.0.

**Audit.** Are footnotes present where needed and consistently placed at the bottom?

**See also.** SA 4.4.

**Source.** p. 39.

## UN 3 — Unify dimensions

Data can be viewed from perspectives called dimensions: measures, scenarios, time, and structure. Consistent notation lets readers recognize the type of information without relying on labels.

### UN 3.1 — Unify measures

**Requirement.** Distinguish absolute measures from relative measures by visual weight. Absolute columns and bars use two-thirds of the category width; relative measures use one-third. Basic measures use thick lines; relative measures use thin lines at 50% of the thick line.

**Why.** Readers can recognize the measure type from the visual pattern, without reading every label.

**Apply.** For absolute measures, set column/bar width to 2/3 of the category width, leaving 1/3 as space. For relative measures, use half the absolute width, i.e. 1/3 of the category. Use a thick line for a basic measure and a thin line (50%) for a relative measure. A ratio with the same unit in numerator and denominator is expressed in percent; a share has the same absolute measure in numerator and denominator.

**Exceptions / limits.** The standard notes that a comprehensive notation for other measure types (value/volume, flow/stock, desirable/undesirable impact) is a future topic.

**Audit.** Do column/bar widths and line thicknesses match the measure type?

**See also.** UN 4.1, EX 1.1.

**Source.** p. 40–42.

### UN 3.2 — Unify scenarios

**Requirement.** Encode scenario types by fill: actual/measured data solid dark; earlier measured periods solid light in a scenario comparison; plan/budget fictitious data outlined; forecast expected data outlined and hatched. Use consistent abbreviations: `AC`, `PY`, `PL`, `BU`, `FC`.

**Why.** Readers must recognize measured, planned, and expected data without relying on labels.

**Apply.** Use a solid dark fill for actual data and a lighter solid fill for previous periods when comparing measured data from different periods. Use an outlined area for plan/budget; the outline suggests the area will “fill up” when the data materializes. Use an outlined area with dark hatch stripes for forecast; the stripe color matches measured data. In stacked columns/areas and multi-line charts, apply the scenario notation to the lowest segment and fill upper segments with different gray shades; add an outline or hatch when those upper segments are planned or forecast. Use scenario notation on the axis to show the reference scenario in variance charts.

**Exceptions / limits.** In a time series with multiple periods, there is no need to color previous periods with a lighter fill. Exact color codes are not prescribed; keep them consistent.

**Audit.** Do the fills and abbreviations match the scenario type?

**See also.** UN 4.1, `semantic-notation.md`.

**Source.** p. 42–46.

### UN 3.3 — Unify time periods, use horizontal axes

**Requirement.** Present time on horizontal axes, moving from left to right; in tables, present time in columns. Use consistent abbreviations for periods and points in time, and differentiate period types with category widths.

**Why.** A consistent time direction and notation make trends recognizable and comparable.

**Apply.** Use `YYYY-MM-DD` for dates and `YYYY-MM`, `YYYY-Qn`, or `YYYY` for periods. Use a leading full stop for the first day of a period (`.2026`, `.Jun`) and a trailing full stop for the last day (`2026.`, `Jun.`). Use two full stops for a span (`Jan..Mar`), not an ellipsis. Make longer periods wider on the category axis (e.g., a year wider than a quarter, a quarter wider than a month), and keep the allocation consistent at least across a page.

**Exceptions / limits.** Other local abbreviations are acceptable if used consistently.

**Audit.** Is time horizontal and left-to-right, with consistent period abbreviations and widths?

**See also.** UN 2.2, UN 4.2, SI 5.2.

**Source.** p. 46–48.

### UN 3.4 — Unify structure dimensions, use vertical axes

**Requirement.** Display structure dimensions on vertical category axes, with horizontal category labels. Reserve horizontal category axes for time.

**Why.** Vertical structure axes make categories easier to read and let the audience recognize structure analyses instantly.

**Apply.** Put regions, products, organizational units, and other structure categories on the vertical axis, sorted according to the analysis. Keep labels horizontal. Use custom symbols or pictograms only when they help differentiate structure dimensions.

**Exceptions / limits.** Some statistical representations on interval or cardinal scales, such as bell curves, may require a horizontal axis.

**Audit.** Are structure categories on a vertical axis with horizontal labels?

**See also.** UN 4.3, EX 1.1.

**Source.** p. 48–49.

## UN 4 — Unify analyses

ISO 24896 defines requirements for scenario, time-series, and structure analyses. IBCS adds adjustment analyses.

### UN 4.1 — Unify scenario analyses

**Requirement.** Analyze scenarios by comparing them and by calculating absolute and relative variances. Use consistent signs, abbreviations, colors, widths, and axis notation.

**Why.** Without a standard encoding, readers cannot tell what is compared, whether a variance is good or bad, or which scenario is the reference.

**Apply.** Arrange scenarios of different periods in temporal ascending order. For the same period, order scenarios by creation date. Use scenario labels (`AC`, `PY`, `PL`, `FC`) rather than year labels, and state the time period in the title, legend, or column header. Visualize comparisons with overlapping grouped columns/bars or scenario triangles; keep `AC` and `FC` in the foreground.

For absolute variances, use `Δ` plus the subtrahend: `ΔPL` for AC-PL or FC-PL, `ΔPY` for AC-PY or FC-PY. If it is unclear whether AC or FC is compared to plan, write `AC-PL` or `FC-PL`. Put `+` on positive variances. Variance columns/bars use the same width and scale as the base columns/bars. Color desirable impacts bright green, undesirable impacts dark red, and neutral/ambiguous impacts blue. If color is unavailable, use light gray for green, dark gray for red, and medium gray for blue; for color deficiency, blue-green can replace green. Apply the scenario notation to the fill to show the minuend: solid for AC, hatched for FC, outlined if PL is the minuend. Apply the reference scenario to the axis: outline (two parallel lines) for PL/BU, solid light for PY. Put labels outside the variance components in the direction of increase/decrease.

For relative variances, use `ΔPL%` for `(AC-PL)/PL*100` or `(FC-PL)/PL*100`, and `ΔPY%` for `(AC-PY)/PY*100` or `(FC-PY)/PY*100`; if ambiguous, write `(AC-PL)%` or `(FC-PL)%`. Put `+` on positive values. Display them as thin columns (vertical pins) or thin bars (horizontal pins). Color them green/red/blue by impact; use the same grayscale fallbacks. Put labels outside the pin in the direction of change. Add a head marker to show the minuend and apply the reference scenario to the axis. Use percentage points (`pp`) for the absolute variance of a ratio, e.g. AC 50% − PL 40% = +10 pp. Use `N/A` when a relative variance cannot be interpreted, such as a positive value compared to a negative denominator.

**Exceptions / limits.** IBCS does not prescribe exact color codes; keep them consistent. A relative variance with a negative denominator is `N/A`, not a mathematically computed percentage.

**Audit.** Are variances labeled with the correct sign, reference, and percentage/percentage-point notation? Are colors and fills semantically correct?

**See also.** UN 3.1, UN 3.2, `semantic-notation.md`.

**Source.** p. 49–55.

### UN 4.2 — Unify time series analyses

**Requirement.** Use consistent notation for year-to-date (YTD), year-to-go (YTG), moving, and indexed analyses.

**Why.** Readers need to recognize the analysis type from the label or marker.

**Apply.** Mark YTD values with an underscore prefix (`_Jun 2026`) and optionally add the first period (`January_June 2026`). Mark a YTD average with an underscore prefix and a consistently designed average marker. Mark the last date value of a stock measure with an underscore prefix and a trailing full stop (`_Jun 2026.`). Mark YTG values with an underscore suffix (`Jun 2026_`). Mark moving analyses with a tilde prefix (`~Jun 2026`); MAT is the moving annual total and MAA the moving annual average. Mark temporal indexing with a black arrowhead pointing right at the left of the index point, with `100%` or `100` written to its left; add an assisting horizontal line if helpful.

**Exceptions / limits.** The exact average glyph is not prescribed; use the organization's standard marker consistently.

**Audit.** Are YTD, YTG, moving, and indexed analyses marked consistently?

**See also.** UN 3.3, UN 5.1.

**Source.** p. 55–58.

### UN 4.3 — Unify structure analyses

**Requirement.** Use consistent notation for structural averaging, ranking, selecting, indexing, and normalizing.

**Why.** Consistent markers let readers recognize the analysis without reading the method.

**Apply.** Mark structural averages with a consistently designed average sign, appended or prefixed, and add an assisting line if needed. Mark rankings with an arrow (`country names↓`, `product sales↑`). Mark structural indexing with a black arrowhead near the index point and `100%` or `100` next to it. Mark structural normalizing with an assisting line representing 100% and a black arrowhead at one end, with `100%` or `100` next to the arrowhead.

**Exceptions / limits.** The visualization of selecting (top ten, quartiles, etc.) is deferred to a future ISO version. Do not invent a marker; describe the selection in text or use an accepted local convention.

**Audit.** Are structure analyses marked consistently, and is selecting handled without inventing a standard?

**See also.** UN 4.2, UN 5.1.

**Source.** p. 58–60.

### UN 4.4 — Unify adjustment analyses

**Requirement.** Use adjustment analyses to neutralize special effects such as currency, inflation, and seasonality, generally in conjunction with scenario analyses.

**Why.** Adjustments reveal root causes that raw values hide.

**Apply.** Recalculate the values of one scenario with correction factors from another, such as re-measuring actual sales at previous-year exchange rates. Show both the adjusted and unadjusted values and explain the adjustment. Use consistent labels for the adjustment type.

**Exceptions / limits.** A future ISO version may define a visualization concept for adjustment analyses. IBCS v2.0 does not prescribe one; do not invent a marker.

**Audit.** Are adjustments shown, explained, and clearly distinguished from the unadjusted values?

**See also.** CH 5.1, CH 5.2.

**Source.** p. 61.

## UN 5 — Unify markers

ISO 24896 defines requirements for markers that support the understanding of differences, trends, scale changes, and references.

### UN 5.1 — Unify highlighting markers

**Requirement.** Use consistently designed markers to highlight messages, differences, trends, values, references, and annotations.

**Why.** Consistent markers speed recognition and reduce interpretation effort.

**Apply.** Use assisting lines/areas to separate, group, or coordinate content. Use difference markers with two parallel lines projecting lengths and a marker between them; color green/red/blue by impact and add an arrowhead if direction matters. Use trend arrows from the first to the last period, with the arrowhead in the time direction and an optional method label such as `CAGR: 10.8%`; color by impact. Use a blue highlighting ellipse for a specific value. Use reference arrowheads close to the index or benchmark point, with the label (`100%`, `Market avg.`) next to it. Use paired annotation references to link annotations to content. Standardize and document any other markers.

**Exceptions / limits.** Exact marker shapes are not prescribed beyond the described patterns; keep them consistent.

**Audit.** Are highlighting markers consistently designed and semantically colored?

**See also.** UN 2.3, UN 2.4, UN 5.2.

**Source.** p. 61–66.

### UN 5.2 — Unify scaling markers

**Requirement.** Use scale bands to indicate reference values, scaling factors, and differences in scale.

**Why.** When charts use different scales, readers need an explicit reference to compare them correctly.

**Apply.** Position a line parallel to the category axis at the same numerical height in all charts, and fill the area between the scaling line and the category axis with a light color. Use the same band design across the page.

**Exceptions / limits.** A future ISO version may define additional scaling visualizations. IBCS v2.0 describes scale bands.

**Audit.** Are scaling markers present where scales differ, and are they consistent?

**See also.** CH 4.3, CO 5.2.

**Source.** p. 66–67.

### UN 5.3 — Unify outlier markers

**Requirement.** Use consistently designed outlier markers when a value is so large that it would distort the chart scale and is not important for the business message.

**Why.** Outlier markers preserve a readable scale while making clear that the full value is not shown.

**Apply.** Omit the pin head and add a triangle pointing in the direction of growth. Use the same marker design across reports. Label the value if needed.

**Exceptions / limits.** Do not use an outlier marker for a value that is important to the message; change the scale or use another visual instead.

**Audit.** Are outliers marked consistently and clearly separated from the visible scale?

**See also.** CH 4.4, `semantic-notation.md`.

**Source.** p. 67.
