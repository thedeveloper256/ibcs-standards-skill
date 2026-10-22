# EXPRESS — Choose Proper Visualization

EXPRESS covers all aspects of choosing the proper visualization in reporting. Proper visualization means that charts and tables help identify interesting facts in statistics and quickly convey compelling stories.

This chapter covers using the correct types of charts and tables, replacing inappropriate visualizations and representations, adding comparisons, and explaining causes.

**Source:** IBCS v2.0, pages 96–142.

## EX 1 — Use appropriate visuals

Choosing the appropriate visual is of prime importance for comprehension. Use tables when looking up data: they have high information density, are clear and honest, do not try to highlight, and typically do not try to prove a key message. Charts are used to convey a key message; the selection of data, chart type, and highlighting is what makes the difference. Charts conveying key messages cannot be replaced by tables.

### EX 1.1 — Use appropriate chart types

**Requirement.** Choose the chart type that fits the analytical question and the data shape. Use horizontal category axes for time series, vertical category axes for structure analyses, and two value axes for x-y relationships.

**Why.** Each chart type supports a different comparison. Using a type that does not match the question hides the pattern or creates a false one.

**Apply.** Use the following families.

**Horizontal charts (time series).**

- **Single column:** one column per period or point in time for one data series. Columns sit in front of the category axis; positive values are labeled above, negative below. The column width encodes the measure type (2/3 of category width for absolute measures, 1/3 for relative measures).
- **Stacked column:** columns divided into segments for multiple data series. Use only when all values have the same sign. Position the most important series directly on the axis. More than five series works only when their values vary little. Apply scenario notation to the lowest segment and gray shades above.
- **Grouped column:** overlapping columns for a primary scenario (AC or FC) and a reference scenario (PY or PL), with the reference behind the primary. The reference may be a triangle instead of a second column. A third scenario can use a triangle.
- **Horizontal pin:** a very thin column for a relative variance over time, with a head showing the primary scenario. Color by impact.
- **Growth waterfall:** base and total columns for a stock measure at different points in time, with contribution columns for increases and decreases in between.
- **Variance waterfall:** base and total columns for a flow measure at different periods and/or scenarios, with contribution columns for period/scenario variances.
- **Line chart:** one or more lines over time. Prefer it when the pattern (trend, seasonality) matters or when there are many data points. Do not use it for a few values, because a line implies a continuum. Lines cannot be stacked; use an area chart for stacked data, although v2.0 has no specific area-chart notation. More than three intersecting lines usually becomes a spaghetti chart.
- **Other horizontal charts:** boxplot/range charts and area charts. V2.0 has no specific notation concept; derive it from column and line charts.

**Vertical charts (structure analyses).**

- **Single bar:** one bar per structure category for one period or point in time. Positive labels to the right, negative to the left.
- **Stacked bar:** bars divided into segments for multiple data series. Use only when all values have the same sign; more than five series works only with little variation.
- **Grouped bar:** overlapping bars for a primary and a reference scenario, with the reference behind the primary; a triangle may replace the reference bar.
- **Vertical pin:** a very thin bar for a relative variance by structure category, with a head showing the primary scenario.
- **Calculation waterfall:** base and total bars for base and result measures (for example, sales and EBIT), with contribution bars for additions and subtractions in a calculation scheme. Intermediate subtotals are possible. There is no horizontal equivalent.
- **Vertical variance waterfall:** base and total bars for values at different periods and/or scenarios, with contribution bars for structure variances.
- **Remainder bar:** a bar accumulating the smallest categories that cannot be shown individually, separated from the other bars by a wider gap. Exclude it from averaging, ranking, and selecting.
- **Other vertical charts:** vertical boxplot/range charts, with no specific notation concept yet. Avoid lines and areas in vertical charts because they imply a continuum that structure analyses do not have.

**Charts with two value axes.**

- **Scattergram:** points positioned in a two-dimensional coordinate system.
- **Bubble chart (portfolio chart):** bubbles instead of points; bubble area shows a third measure. A fourth dimension can be shown with pie segments inside the bubbles.
- **Other two-value-axis charts:** for example, a continuous horizontal timeline or columns/bars of variable width. V2.0 has no specific notation rules; derive them from column, bar, and line charts.

**Exceptions / limits.** V2.0 explicitly defers specific notation for area charts, boxplot/range charts, and charts with two value axes. Do not invent normative rules; state that the notation is derived.

**Audit.** Does the chart family match the analytical question and the data shape? Are the axes oriented according to UN 3.3 and UN 3.4?

**See also.** UN 3.3, UN 3.4, EX 1.2, `chart-and-table-catalog.md`.

**Source.** p. 96–115.

### EX 1.2 — Use appropriate table types

**Requirement.** Choose the table type that fits the analytical purpose, and design columns and rows with consistent, recognizable types.

**Why.** Tables are for looking up precise values. Recognizable column and row types let the reader find the value and understand its role without re-reading the whole table.

**Apply.** Use these table types:

- **Time series table:** time columns with measure rows or structure rows, for time-series analysis.
- **Variance table:** scenario columns and variance columns with measure rows or structure rows, for scenario analysis.
- **Cross table:** structure columns with structure rows, for structure analysis.
- **Combined table:** more than one column type and/or row type, side by side or nested, for multiple analyses.

Use these column types:

- **Row header column:** the row names, usually at the far left; keep texts short; separate it from numeric columns with a wider gap.
- **Scenario column:** AC, PY, PL, BU, or FC data; use the same width for all scenario columns and follow the scenario order in UN 4.1.
- **Variance column:** absolute (`ΔPL`, `ΔPY`) or relative (`ΔPL%`, `ΔPY%`) variances.
- **Time column:** periods or points in time, ordered left to right.
- **Measure column:** measures such as sales, headcount, or equity; use glossary abbreviations in headers; separate intermediate results with a wider gap.
- **Structure column:** categories of a structure dimension such as countries or products.
- **Of which column:** details of an aggregated column that do not total to it; use a smaller font or narrower width, place it to the right of the mother column, and do not separate it from the mother column.
- **Remainder column:** accumulated smaller categories such as “Other cost”; keep the normal gap within the measure group.
- **Percent of column:** important data as a share of a given total, such as a P&L line as a percentage of sales; smaller font and narrower width are appropriate.
- **Totals column:** totals of a group, placed to the right of the group; consistent design, bold or light-gray fill.
- **Hierarchical column:** multiple levels; separate parents with wider gaps; place parent columns to the right of their children.
- **Nested column:** one column type repeats within every column of another type; separate the resulting groups with wider gaps.

Use these row types:

- **Column header row:** column names at the top; may use two or more rows and abbreviated text.
- **Measure row:** measures such as sales, cost, or profit; separate final or intermediate result rows with solid lines and consistent bold/light-gray design.
- **Structure row:** categories of a structure dimension.
- **Of which row:** details of an aggregated row that do not total to it; place the aggregated row above the “of which” rows, use a smaller height/font, do not separate it with a horizontal line, and right-align its header.
- **Remainder row:** accumulated smaller categories such as “Rest of world”; exclude it from averaging, ranking, and selecting.
- **Percent of row:** a share of a given total, such as gross profit as a percentage of sales; smaller font, italic, or smaller height.
- **Totals row:** totals of a group, placed below the group and separated by a solid line; consistent bold/light-gray design.
- **Hierarchical row:** multiple levels; separate parents with wider gaps and place parent rows below their children.
- **Nested row:** one row type repeats within every row of another type; separate the resulting groups with wider gaps.

**Layout rules.** Use identical widths for columns of the same type, independent of header text length. Right-align numeric columns and their headers; left-align text columns and their headers. Use very light or omitted vertical lines, and white gaps to separate columns: a narrow gap within a type, a wider gap between groups. Use identical row heights within a row type and light horizontal lines where they help. Put time periods, scenarios, and variances in columns, not rows.

**Exceptions / limits.** “One-dimensional tables” without row headers are lists and are not covered as tables. Combined tables may use nested or hierarchical structures.

**Audit.** Does the table type match the analytical purpose? Are column/row types visually recognizable and consistently aligned?

**See also.** EX 1.1, ST 5.2, `chart-and-table-catalog.md`.

**Source.** p. 115–135.

## EX 2 — Replace inappropriate chart types

Inappropriate charts make it hard to perceive the key message. Replace them with chart types better suited to the question.

### EX 2.1 — Replace pie and ring charts

**Requirement.** Replace pie and ring charts with bar charts, stacked columns, or another suitable comparison.

**Why.** Pie and ring charts are circular divisions of a total into sectors. They allow only one-dimensional analyses, make precise comparison hard, and seldom reveal an interesting insight. Bars and stacked columns compare proportions more clearly.

**Apply.** Use sorted bars for part-to-whole comparisons, or stacked columns for composition over time. A pie may be retained only for the point-positioned map exception described below, with two or three values.

**Exceptions / limits.** A pie chart can be useful when market sizes or shares for one period must be allocated to regions on a map, because a pie can be positioned at a specific point. This is an exception to EX 2.1 and must not be generalized to ordinary pie dashboards.

**Audit.** Is the pie or ring chart the best available comparison? If retained, is it a point-positioned map exception with at most two or three values?

**See also.** CH 3.3, EX 1.1.

**Source.** p. 136.

### EX 2.2 — Replace gauges, speedometers

**Requirement.** Replace gauges and speedometers with simpler forms such as bars or columns.

**Why.** Gauges make accurate visual comparison difficult, use excessive space for a single value, and often emphasize design over information.

**Apply.** Use a bar or column with a clear target and a labeled deviation. If a gauge is retained, apply semantic coloring to the current deviation from the target, not to bandwidths of desirable and undesirable values.

**Exceptions / limits.** A gauge may be valid only when all of the following hold: it shows real-time data for monitoring rather than analysis; semantic coloring highlights the current deviation from a target; the target and the interpretation of the deviation are immediately clear. Even then, use it only when an alternative would communicate the deviation less effectively.

**Audit.** Is the gauge necessary for real-time monitoring with a clear target and semantic deviation? If not, replace it.

**See also.** EX 2.5, `semantic-notation.md`.

**Source.** p. 136–137.

### EX 2.3 — Replace radar and funnel charts

**Requirement.** Replace radar (net, spider) charts and funnel charts with bar charts or other suitable comparisons.

**Why.** Radar charts have no advantage over bars and many weaknesses; they are useful only for two-dimensional analyses or when the circular arrangement itself has meaning, which is rare in business reporting. Funnel charts mislead when the displayed area does not correspond to the numerical values.

**Apply.** Use bars for category comparisons. If a radar chart is retained, restrict it to a genuine two-dimensional analysis (for example, young–old versus rich–poor) or a meaningful circular arrangement (for example, compass directions). If a funnel is retained, ensure its area is proportional to the values and label them.

**Exceptions / limits.** Radar: two-dimensional analyses or meaningful circular arrangements. Funnel: only when the shape encodes a real process and its area is proportional; otherwise replace it.

**Audit.** Does the radar chart have a genuine two-dimensional or circular meaning? Does the funnel area correspond to the values?

**See also.** CH 3.1, EX 1.1.

**Source.** p. 137–138.

### EX 2.4 — Replace spaghetti charts

**Requirement.** Replace a chart with more than three or four intersecting lines with several smaller charts (small multiples), one line each.

**Why.** A spaghetti chart is more confusing than small multiples, particularly when the reader is evaluating the shape or trend of each line.

**Apply.** Use small multiples with the same scale. If the reader must compare exact heights across lines, a spaghetti chart may be unavoidable; in that case, use filtering or highlighting to reduce the number of visible lines.

**Exceptions / limits.** Exact height comparison across several lines may justify keeping the lines. Interactive filtering can also make a spaghetti chart workable.

**Audit.** Are more than three or four lines intersecting? If so, would small multiples communicate the trend more clearly?

**See also.** CO 5.1, EX 1.1.

**Source.** p. 138.

### EX 2.5 — Replace traffic lights

**Requirement.** Replace traffic lights with bars or another analog representation, except when the figure is binary or the decision depends only on compliance with a threshold.

**Why.** Traffic lights contain little information per area and represent no more than three states.

**Apply.** Use bars, table bars, or a labeled status. If a traffic light is retained, make it a status indicator, not an analytical chart, and use no more than two or three states.

**Exceptions / limits.** A traffic light may be appropriate when the figure is binary (“yes or no”) or the primary objective is to indicate compliance or non-compliance with a defined target or threshold and the magnitude of the deviation is irrelevant to the decision.

**Audit.** Is the figure binary or threshold-compliance only? If not, replace the traffic light.

**See also.** CO 4.4, EX 2.2.

**Source.** p. 138–139.

## EX 3 — Replace inappropriate representations

From a perceptual perspective, avoid representations that require time-consuming analysis or additional explanation, especially merely conceptual representations and all forms of text, including bullet lists.

### EX 3.1 — Prefer quantitative representations

**Requirement.** Prefer quantitative representations such as charts, photos, or maps to conceptual illustrations that require explanation, such as box-and-arrow diagrams or process flows.

**Why.** Audiences understand charts and pictures faster than conceptual diagrams, and time is limited.

**Apply.** Use a quantitative chart when the point is a comparison or a magnitude. For a one-hour presentation, use no more than three or four conceptual representations, and only when they are essential for comprehension.

**Exceptions / limits.** Conceptual representations are appropriate when the concept itself is the message and cannot be shown quantitatively.

**Audit.** Is a conceptual diagram doing work that a chart or picture could do faster?

**See also.** EX 3.2, EX 5.1.

**Source.** p. 139.

### EX 3.2 — Avoid text slides in presentations

**Requirement.** Avoid all forms of text slides in live presentations.

**Why.** Text must be read and understood, which competes with listening. Seeing and hearing something at the same time improves recall, but a text slide is not a visual aid in the same sense as a chart.

**Apply.** Recite the text or put it in a handout. Keep projected visuals visual. Put lists and bullet points in the written handout, not on the screen.

**Exceptions / limits.** Specific texts being discussed, such as definitions or quotes, may be shown.

**Audit.** Is the slide asking the audience to read instead of listen? If so, move the text to the handout.

**See also.** EX 3.1, SA 4.5.

**Source.** p. 140.

## EX 4 — Add comparisons

Visual perception is strongly based on setting one perceived object in relation to another. Adding meaningful comparisons helps the eye evaluate faster.

### EX 4.1 — Add scenarios

**Requirement.** Add available scenarios such as plan and previous year as comparison references.

**Why.** A value alone has no context. Scenarios give the reader the reference needed to judge performance.

**Apply.** Add plan, previous year, forecast, or another meaningful scenario. Use the standardized scenario notation in UN 3.2 and the scenario comparison rules in UN 4.1.

**Exceptions / limits.** Add a scenario only when it is available and meaningful; a false or incomparable reference is worse than none.

**Audit.** Does the page include the comparison the audience needs, with the correct scenario notation?

**See also.** UN 3.2, UN 4.1, EX 4.2.

**Source.** p. 140.

### EX 4.2 — Add variances

**Requirement.** After adding scenarios, visualize the variances to make evaluation easier.

**Why.** The absolute difference and the relative difference are often the actual message; leaving the reader to subtract values mentally slows comprehension.

**Apply.** Add absolute variance columns/bars (`ΔPL`, `ΔPY`) and, where meaningful, relative variance pins (`ΔPL%`, `ΔPY%`). Use the sign, color, and percentage-point conventions in UN 4.1.

**Exceptions / limits.** A relative variance with a negative denominator is `N/A`. Do not add a variance that has no meaningful interpretation.

**Audit.** Are the variances shown with correct notation, sign, color, and scale?

**See also.** UN 4.1, CO 4.2.

**Source.** p. 141.

## EX 5 — Explain causes

Present data in a way that shows interrelations, causes, and dependencies. Extreme and deviant values often explain causes; context and detail increase credibility and comprehension.

### EX 5.1 — Show tree structures

**Requirement.** Show the assumptions or basic data behind an analysis in a tree structure of calculated measures.

**Why.** Showing how a result is built from its components makes the analysis more understandable and more convincing.

**Apply.** Arrange the calculation in a tree, with the result at the root and the components branching from it. Use consistent notation and scaling. See also CO 5.2.

**Exceptions / limits.** None stated in v2.0.

**Audit.** Does the tree make the calculation and its assumptions visible?

**See also.** CO 5.2, EX 5.3.

**Source.** p. 141.

### EX 5.2 — Show clusters

**Requirement.** Use clusters in two- or three-dimensional form to reveal patterns in large amounts of data.

**Why.** Clustering can expose groups and relationships that a table or a single series hides.

**Apply.** Use scattergrams or bubble charts with meaningful axes and a clear third dimension. Label clusters and explain the grouping.

**Exceptions / limits.** V2.0 has no specific notation rules for charts with two value axes; derive the notation from column, bar, and line charts and state the derivation.

**Audit.** Does the cluster reveal a real pattern, and is the grouping explained?

**See also.** EX 1.1, EX 5.3.

**Source.** p. 142.

### EX 5.3 — Show correlations

**Requirement.** When comparing several data series, show correlations through suitable rankings and comparisons.

**Why.** Correlations help the audience understand interrelations and patterns that isolated series do not reveal.

**Apply.** Use scattergrams, ranked bars, or other comparisons that make the relationship visible. Label the direction and strength of the relationship where relevant, and avoid implying causation from correlation alone.

**Exceptions / limits.** None stated in v2.0. Do not claim causation without evidence.

**Audit.** Is the correlation shown clearly, and is the interpretation distinguished from causation?

**See also.** EX 5.2, EX 1.1.

**Source.** p. 142.
