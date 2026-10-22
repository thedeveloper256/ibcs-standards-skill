# Audit Checklist

Use this checklist to review an existing page, dashboard, report, or presentation. Work in passes. Do not polish a page whose integrity is broken.

**Source:** IBCS v2.0, pages 16–156, organized by the SUCCESS principles.

## 1. Severity model

| Severity | Definition | Examples | Action |
|---|---|---|---|
| **Critical** | An integrity failure that makes the visual misleading or untrustworthy. | Truncated axis, clipped bar, inconsistent scales for the same unit without a scaling marker, area/volume distortion, misleading map colors, unequal class widths, hidden inflation/currency impact that changes the conclusion. | Stop the review. Fix before any semantic or styling comment. |
| **Major** | A semantic or composition failure that changes interpretation. | Wrong scenario fill, wrong variance sign/color, missing reference, non-MECE structure, wrong chart type, missing key message, descriptive title replaced by a takeaway. | Fix in the same review cycle. |
| **Minor** | Clutter, redundancy, density, or polish that slows reading but does not change the conclusion. | Decorative frames, gridlines, repeated words, oversize fonts, wasted margins, unnecessary labels. | Fix after critical and major issues. |

## 2. Integrity pass (critical)

- [ ] **CH 1.1** — Does every value axis start at zero? If not, is this an indexed chart with small deviations from 100%, labels at the 100% line, and a documented exception?
- [ ] **CH 1.2** — Is any value axis logarithmic? If so, is the purpose relative growth across orders of magnitude, is the audience familiar, and is the axis clearly marked?
- [ ] **CH 1.3** — Do ordered classes (histogram bins) have identical widths?
- [ ] **CH 2.1** — Is any column, bar, area, or component clipped, broken, or truncated?
- [ ] **CH 2.2** — If a creative 2D/3D scaling solution is used, is it proportional and truthful, and clearly not a misleading area/volume encoding?
- [ ] **CH 3.1** — If area encodes a value, is the **area** (not diameter or height) proportional? Would a linear comparison be clearer?
- [ ] **CH 3.2** — If volume encodes a value, is the **volume** (not diameter or surface area) proportional? Would a linear comparison be clearer?
- [ ] **CH 3.3** — Are colored map areas used only for area-related measures? If not, is there a genuine geospatial need with point/symbol encoding?
- [ ] **CH 4.1** — Do charts of the same unit share the same scale? If not, is the difference clearly marked?
- [ ] **CH 4.2** — Are charts sized to their data rather than squeezed onto a scale that hides small values?
- [ ] **CH 4.3** — Where scales differ, is a consistent scale band or other scaling marker present?
- [ ] **CH 4.4** — Is an unimportant outlier marked rather than allowed to compress the whole chart?
- [ ] **CH 4.5** — Is a magnifying glass clearly linked and consistent in units with the main chart?
- [ ] **CH 5.1** — Is the inflation impact shown or explained where it could distort a time series?
- [ ] **CH 5.2** — Is the currency impact shown or explained where it could distort a time series?

**Stop condition:** if any of CH 1.1–CH 5.2 fails, do not spend time on colors, fonts, or layout until it is fixed.

## 3. Semantic pass (major)

### 3.1 Terminology and formats

- [ ] **UN 1.1** — Are terms and abbreviations defined and used consistently? Is there a glossary?
- [ ] **UN 1.2** — Are numbers, currencies, physical units, and dates formatted consistently? Are charts limited to three digits and tables to four? Is there one negative format, and no plus sign on non-variances?

### 3.2 Text elements

- [ ] **UN 2.1** — Is the key message in a consistent position and layout?
- [ ] **UN 2.2** — Is the page title descriptive and three-line (who / what / when)? Are measures bold and units regular? Are subtitles used only for multiple visuals?
- [ ] **UN 2.3** — Are legends and labels horizontal, integrated where possible, and consistently positioned by chart type?
- [ ] **UN 2.4** — Are annotations consistently designed and linked to the content they explain?
- [ ] **UN 2.5** — Are footnotes at the bottom and used for definitions, sources, and retrieval dates?

### 3.3 Dimensions and scenarios

- [ ] **UN 3.1** — Do absolute measures use 2/3 category width and relative measures 1/3? Are lines thick vs thin (50%)?
- [ ] **UN 3.2** — Are scenario fills correct: AC solid dark, PY solid light, PL/BU outlined, FC outlined + hatched? Are abbreviations consistent? In stacked charts, is notation on the lowest segment and are upper segments gray?
- [ ] **UN 3.3** — Is time horizontal and left-to-right? Are period abbreviations consistent? Do category widths reflect period length?
- [ ] **UN 3.4** — Are structure categories on a vertical axis with horizontal labels?

### 3.4 Analyses

- [ ] **UN 4.1** — Are scenario comparisons ordered correctly? Are absolute variances labeled `ΔPL`/`ΔPY` or explicit `AC-PL`/`FC-PL`? Are relative variances `ΔPL%`/`ΔPY%`? Are signs, `+`, colors, widths, pin heads, axis references, percentage points, and `N/A` correct?
- [ ] **UN 4.2** — Are YTD, YTG, moving, MAT/MAA, and temporal indexing marked consistently?
- [ ] **UN 4.3** — Are structure averaging, ranking, selecting, indexing, and normalizing marked consistently? Is selecting correctly described as not specified in v2.0?
- [ ] **UN 4.4** — Are adjustment analyses shown and explained? Is the visualization gap acknowledged?

### 3.5 Markers

- [ ] **UN 5.1** — Are assisting lines/areas, difference markers, trend arrows, highlighting ellipses, reference arrowheads, and annotation references consistent?
- [ ] **UN 5.2** — Are scale bands used and designed consistently where scales differ?
- [ ] **UN 5.3** — Are outliers marked consistently, with the pin head omitted and a triangle in the growth direction?

## 4. Message and structure pass (major)

### 4.1 SAY

- [ ] **SA 1.1** — Is the reporting goal explicit: inform, explain, or decide?
- [ ] **SA 1.2** — Is the audience known: knowledge, expectations, objections, cultural context?
- [ ] **SA 2.1** — Does the introduction map the situation with accepted facts?
- [ ] **SA 2.2** — Is the complication or problem explicit and relevant?
- [ ] **SA 2.3** — Is there a clear question from the audience's perspective?
- [ ] **SA 3.1** — Is the key message a complete sentence, clearly a detection, explanation, or suggestion?
- [ ] **SA 3.2** — Is the key message first, then supported? If delayed, is there a negative/cultural reason?
- [ ] **SA 4.1** — Is the message supported by facts, figures, charts, tables, or images?
- [ ] **SA 4.2** — Are words precise, with quantities, comparisons, periods, and sources rather than vague qualifiers?
- [ ] **SA 4.3** — Is the message visually highlighted with consistent markers?
- [ ] **SA 4.4** — Are sources named? Are they in the written report/handout/dashboard?
- [ ] **SA 4.5** — Are annotations linked to the content they explain?
- [ ] **SA 5.1** — Does a presentation repeat the key message and avoid “Thank you for your attention”? Does a written report avoid mechanical repetition?
- [ ] **SA 5.2** — Does the conclusion state the decision, consequences, and next step?

### 4.2 STRUCTURE

- [ ] **ST 1.1** — Are items in a group of the same type?
- [ ] **ST 1.2** — Are statements in a list of the same type?
- [ ] **ST 1.3** — Is the wording grammatically consistent, especially in lists?
- [ ] **ST 1.4** — Are visualizations consistent in layout, color, form, and font?
- [ ] **ST 2.1** — Do reporting chapters/sections avoid overlapping content?
- [ ] **ST 2.2** — Are business measures on one level mutually exclusive, without double-counting?
- [ ] **ST 2.3** — Are structure categories at the same level mutually exclusive?
- [ ] **ST 3.1** — Are all important arguments included?
- [ ] **ST 3.2** — Are structures exhaustive, with a remainder where needed?
- [ ] **ST 4.1** — Is deductive reasoning valid, with accepted premises?
- [ ] **ST 4.2** — Is inductive reasoning homogeneous, non-overlapping, and exhaustive?
- [ ] **ST 5.1** — Is the reporting structure visible through outlines, tabs, dashboards, or summaries?
- [ ] **ST 5.2** — Is the table hierarchy visible in both columns and rows?
- [ ] **ST 5.3** — Is the structure of notes visible and linked?

## 5. Visual choice pass (major)

- [ ] **EX 1.1** — Does the chart family match the analytical question and data shape? Are horizontal axes used for time and vertical axes for structure? Are two-value-axis charts handled with the deferred-notation caveat?
- [ ] **EX 1.2** — Does the table type match the purpose? Are column and row types recognizable, aligned, and consistently spaced? Are time/scenario/variance in columns?
- [ ] **EX 2.1** — Are pie/ring charts replaced? If retained, is this the point-positioned map exception with two or three values?
- [ ] **EX 2.2** — Are gauges/speedometers replaced? If retained, is this real-time monitoring with semantic current-deviation coloring, a clear target, and no better alternative?
- [ ] **EX 2.3** — Are radar/funnel charts replaced unless they have a genuine two-dimensional/circular meaning or a proportional process shape?
- [ ] **EX 2.4** — Are spaghetti charts replaced with small multiples unless exact height comparison requires the lines?
- [ ] **EX 2.5** — Are traffic lights replaced unless the figure is binary or threshold-compliance only?
- [ ] **EX 3.1** — Are quantitative representations preferred? Are conceptual diagrams limited to three or four per hour and only when essential?
- [ ] **EX 3.2** — Are text slides avoided, with text in the handout or spoken?
- [ ] **EX 4.1** — Are meaningful scenarios added?
- [ ] **EX 4.2** — Are absolute and relative variances added with standard notation?
- [ ] **EX 5.1** — Are tree structures used to show assumptions and calculated measures?
- [ ] **EX 5.2** — Are clusters used to reveal patterns in large data?
- [ ] **EX 5.3** — Are correlations shown with suitable rankings/comparisons, without implying causation?

## 6. Density and clutter pass (minor)

- [ ] **SI 1.1** — Are meaningless layout elements removed?
- [ ] **SI 1.2** — Are colored/filled backgrounds removed from behind numbers and labels?
- [ ] **SI 1.3** — Are meaningless animations/transitions removed?
- [ ] **SI 2.1** — Are frames, shadows, and pseudo-3D effects removed unless meaningful?
- [ ] **SI 2.2** — Is color used only for analytical meaning?
- [ ] **SI 2.3** — Are fonts simple, legible, and semantically styled?
- [ ] **SI 3.1** — Are gridlines/value axes replaced by data labels where possible?
- [ ] **SI 3.2** — Are vertical table lines replaced by right-alignment and gaps?
- [ ] **SI 4.1** — Are superfluous words such as “sum” and “total” removed?
- [ ] **SI 4.2** — Are obvious terms such as “chart” and “trend” removed?
- [ ] **SI 4.3** — Are repeated words removed from labels and headers?
- [ ] **SI 5.1** — Are labels for small values avoided unless discussed?
- [ ] **SI 5.2** — Are long numbers shortened to three digits in charts and four in tables?
- [ ] **SI 5.3** — Are unnecessary labels removed, keeping extrema and significant points?
- [ ] **CO 1.1** — Are fonts free of oversize?
- [ ] **CO 1.2** — Are visual components small and legible?
- [ ] **CO 1.3** — Are visuals as small as legibility allows?
- [ ] **CO 2.1** — Are page margins narrow?
- [ ] **CO 2.2** — Is empty space reduced while preserving useful whitespace?
- [ ] **CO 3.1** — Are enough data points shown to reveal the pattern?
- [ ] **CO 3.2** — Are useful dimensions added?
- [ ] **CO 4.1** — Are overlay charts used only where they remain legible; would multi-tier be better?
- [ ] **CO 4.2** — Are multi-tier charts aligned on the same category axis and correctly scaled?
- [ ] **CO 4.3** — Are extended charts aligned on the extended axis and scaled identically?
- [ ] **CO 4.4** — Are table bars, sparklines, and traffic lights correctly scaled and limited to their valid uses?
- [ ] **CO 4.5** — Are explanations embedded next to the content they explain?
- [ ] **CO 5.1** — Do small multiples share type and scale, with a readable count and an “Others” category if needed?
- [ ] **CO 5.2** — Are related charts genuinely related, consistently scaled, and is a ratio tree used for root causes?
- [ ] **CO 5.3** — Do chart–table combinations add supplementary information rather than duplicate it?
- [ ] **CO 5.4** — Are charts/tables in text pages close to the sentence they support and properly titled?

## 7. Common anti-patterns

| Symptom | Rule ID | Fix |
|---|---|---|
| Value axis starts above zero | CH 1.1 | Start at zero; use a variance chart or the indexed exception. |
| Bar or column is broken/clipped | CH 2.1 | Use an unbroken bar, scale band, outlier marker, or detail view. |
| Two same-unit charts use different scales | CH 4.1 | Use one scale; if unavoidable, add a scale band. |
| Bubble diameter, not area, encodes value | CH 3.1 | Use area-proportional bubbles or bars. |
| Map colors non-area data | CH 3.3 | Use bars or point symbols. |
| Unequal histogram bins | CH 1.3 | Use equal-width bins. |
| Inflation/currency effect hidden | CH 5.1/5.2 | Show or explain the adjustment. |
| Plan is solid dark | UN 3.2 | Outline plan/budget; solid dark is actual. |
| Forecast is solid | UN 3.2 | Outline + hatch forecast. |
| Positive variance lacks `+` | UN 4.1 | Add `+`; keep minus signs. |
| Variance color is reversed | UN 4.1 | Green desirable, red undesirable, blue neutral. |
| Relative variance computed on a negative denominator | UN 4.1 | Show `N/A`. |
| Ratio difference labeled `%` | UN 4.1 | Use percentage points (`pp`). |
| Title is a takeaway sentence | UN 2.2 | Use a descriptive three-line title; separate key message. |
| No key message | SA 3.2 | Add one complete-sentence message first. |
| Text slide | EX 3.2 | Replace with a chart or handout. |
| Pie chart with many slices | EX 2.1 | Sorted bars or stacked columns. |
| Gauge wall | EX 2.2 | Bars/columns with target and deviation. |
| Rainbow palette | SI 2.2 | Semantic palette; one meaning per color. |
| Gridlines everywhere | SI 3.1 | Direct labels; remove unnecessary gridlines. |
| Long numbers | SI 5.2 | Round; use k/m/b. |
| Small multiples with different scales | CO 5.1 / CH 4.1 | Identical scale; resize instead. |
| Sparklines individually scaled | CO 4.4 | Use proper scaling (e.g., indexed) or omit. |
| Remainder ranked among categories | EX 1.1 / ST 3.2 | Separate it and exclude it from ranking/averaging/selecting. |
| Structure not MECE | ST 2.1–2.3 / ST 3.1–3.2 | Remove overlaps; add missing arguments/remainder. |
| Units or currency missing | UN 1.2 | State the unit/currency in title or header. |
| Oversize fonts | CO 1.1 | Reduce to legible minimum. |
| Wasted margins | CO 2.1 | Narrow margins; use space for context. |

## 8. Triage rules

1. **Integrity before semantics before styling.** A beautiful page with a truncated axis is still wrong.
2. If there are multiple critical findings, fix the axis/scale/component integrity first; a later styling fix cannot compensate.
3. If the data do not reconcile, stop and reconcile before reviewing design.
4. If the scenario or variance reference is missing, fix the comparison before commenting on color.
5. If the key message is missing, do not rewrite the title as a substitute; add the message and keep the title descriptive.
6. After fixing a critical issue, re-check the whole page: a new scale or chart type can introduce new semantic problems.
7. Do not “fix” a misleading visual by changing the message to match the visual. Fix the visual.
8. Do not spend time on minor clutter while a major interpretation issue remains.

## 9. Stop conditions

Stop the review and escalate before continuing if:

- a value axis is truncated on an ordinary column/bar chart;
- same-unit charts use conflicting scales without a scaling marker;
- a component is clipped or a bar is broken;
- data reconciliation fails;
- the page hides a known inflation or currency effect that changes the conclusion;
- the scenario/variance reference is unknown;
- the chart type is structurally incapable of supporting the claimed comparison.

## 10. Findings report template

```markdown
1. [Critical] <finding> — <rule ID>. Evidence: <...>. Fix: <...>.
2. [Major] <finding> — <rule ID>. Evidence: <...>. Fix: <...>.
3. [Minor] <finding> — <rule ID>. Evidence: <...>. Fix: <...>.
```

For each finding, state:

- **Severity:** critical, major, or minor.
- **Location:** page, visual, axis, series, label, or text element.
- **Evidence:** the exact observation, value, or comparison.
- **Rule ID:** the IBCS rule that applies.
- **Fix:** the concrete change, with the expected result.
- **Residual risk:** what remains uncertain after the fix.

Order findings by severity, then by impact on the decision. Do not bury a critical axis issue under a list of font comments.
