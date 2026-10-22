# Chart and Table Catalog

This catalog is the working selection guide for IBCS visuals. It covers the chart families in v2.0, their anatomy and use conditions, the table taxonomy, and the table-vs-chart decision.

**Source:** IBCS v2.0, pages 96–142. The chart selection matrix is conceptual; v2.0 defers specific notation for area charts, boxplot/range charts, and charts with two value axes.

## 1. Selection matrix

| Analytical question | Data shape | Preferred visual | Avoid |
|---|---|---|---|
| How did one measure develop over time? | One series, few periods | Single column | Pie, gauge |
| What is the temporal pattern or seasonality? | One or more series, many points | Line chart | Stacked columns with many periods |
| How is a total composed over time? | Multiple series, same sign | Stacked column | Pie, 3D |
| How does actual compare with a reference over time? | Primary + reference scenario | Grouped column, scenario triangle | Two separate charts with different scales |
| How large is the relative variance over time? | Primary + reference scenario | Horizontal pin | Full-width columns for percentages |
| What changed a stock measure between two dates? | Stock at two points + contributions | Growth waterfall | Clustered columns without bridge |
| What explains a variance between periods/scenarios over time? | Flow at two periods/scenarios + contributions | Horizontal variance waterfall | Pie, stacked column without bridge |
| How do categories compare in one period? | One series, structure dimension | Single bar, sorted | Pie, radar |
| How is a total composed across categories? | Multiple series, same sign | Stacked bar | Pie, 3D |
| How does a category compare with a reference? | Primary + reference scenario | Grouped bar, scenario triangle | Two separate charts with different scales |
| How large is the relative variance by category? | Primary + reference scenario | Vertical pin | Full-width bars for percentages |
| What is the calculation from a base to a result? | Base, contributions, subtotals, result | Calculation waterfall | Table-only calculation, 3D |
| What explains a structure variance? | Two structures/scenarios + contributions | Vertical variance waterfall | Pie, stacked bar without bridge |
| Which categories are small and numerous? | Many structure categories | Single bar + remainder bar | Unreadable axis with every category |
| Is there a relationship between two measures? | Two value axes | Scattergram | Dual-axis column/line without explanation |
| Is there a relationship among three measures? | Two value axes + size | Bubble chart | 3D bubbles without correct area |
| How do I look up exact values? | Precise numbers | Table | Chart with dense labels |
| How did values develop over time, precisely? | Time columns + measure/structure rows | Time series table | Chart-only when lookup is the purpose |
| How do scenarios and variances compare, precisely? | Scenario + variance columns + rows | Variance table | Pie, gauge |
| How do two structure dimensions intersect? | Structure columns + structure rows | Cross table | 3D chart |
| How do several analyses combine? | Multiple column/row types | Combined table | Unrelated page fragments |

## 2. Horizontal charts (time series)

### Single column

- **Purpose:** Show the temporal development of one data series.
- **Anatomy:** Horizontal category axis with period labels; one column per period extending from the axis; columns in front of the axis; legend in the title; data labels above positive columns and below negative columns; column width 2/3 of category width for absolute measures (1/3 for relative).
- **Use when:** One series, a modest number of periods, and the absolute level or change is the message.
- **Avoid when:** There are many periods and the pattern matters more than individual values (use a line chart); the measure is a relative variance (use a horizontal pin).
- **Variants:** Negative columns; indexed values; annotated extrema.
- **Source:** p. 99–100.

### Stacked column

- **Purpose:** Show the composition of a total over time.
- **Anatomy:** Horizontal category axis; columns divided into segments for each data series; scenario notation on the lowest segment; upper segments in gray shades; legends at the far left or right, vertically centered in the segments; segment labels inside segments; total label above/below the column; most important series on the axis.
- **Use when:** Multiple series, all values have the same sign, and the total and its composition both matter.
- **Avoid when:** Values have mixed signs; there are too many series or their values vary too much (more than five series works only with little variation); precise comparison of small segments is needed.
- **Variants:** 100% stacked columns for shares; stacked columns with an outline/hatch for plan/forecast upper segments.
- **Source:** p. 100–101.

### Grouped column

- **Purpose:** Compare a primary scenario (AC or FC) with a reference scenario (PY or PL) over time.
- **Anatomy:** Horizontal category axis; two overlapping columns per category, reference behind primary; primary in the foreground; reference left or right according to creation date; the third scenario can use a reference scenario triangle; otherwise like a single column.
- **Use when:** The comparison of two scenarios at each period is the message.
- **Avoid when:** More than two or three scenarios would make the overlap unreadable; a variance tier would communicate the difference better.
- **Variants:** Primary column with reference triangles instead of two columns; grouped columns plus a variance tier.
- **Source:** p. 101–102.

### Horizontal pin

- **Purpose:** Show relative variances over time.
- **Anatomy:** Horizontal category axis; one very thin pin per period; pin length = relative variance; pin color green/red by impact; pin head filled to show the primary scenario; labels above positive pins, below negative pins; pin in the foreground.
- **Use when:** The message is the relative variance (`ΔPL%`, `ΔPY%`) and a full column would overemphasize the magnitude.
- **Avoid when:** The absolute variance is the message (use variance columns); the denominator is negative or meaningless (use `N/A`).
- **Variants:** Pins with reference axis outline; pins with annotation references.
- **Source:** p. 102–103.

### Growth waterfall

- **Purpose:** Explain the change in a stock measure between two or more points in time.
- **Anatomy:** Horizontal category axis; base and total columns for the stock measure at each date; contribution columns between them for increases and decreases; contribution columns start at the end value of the preceding column; assisting lines connect the end of a column to the beginning of the next.
- **Use when:** The bridge from one stock level to another is the message (for example, headcount or accounts receivable).
- **Avoid when:** The measure is a flow (use a variance waterfall); the contributions are not additive or not known.
- **Variants:** More than two base/total points; detailed contribution grouping.
- **Source:** p. 103–104.

### Variance waterfall (horizontal)

- **Purpose:** Explain period or scenario variances for a flow measure.
- **Anatomy:** Horizontal category axis; base and total columns for a flow measure at different periods and/or scenarios; contribution columns for the variances; assisting lines connect successive columns; same components as single columns.
- **Use when:** The bridge from plan to actual, previous year to actual, or one period to another is the message.
- **Avoid when:** The measure is a stock (use a growth waterfall); the contributions are not additive.
- **Variants:** Plan-to-actual bridge; previous-year-to-actual bridge; period-to-period bridge.
- **Source:** p. 104.

### Line chart

- **Purpose:** Show temporal patterns, trends, and seasonality, especially with many data points.
- **Anatomy:** Horizontal category axis; one or more lines with markers; line thickness/color/markers carry meaning; legend in the title for one series, at the line end or near the line for multiple series; labels at peaks above and valleys below, selectively.
- **Use when:** The pattern matters, the series has many points, or multiple series need to show positive and negative values.
- **Avoid when:** There are only a few values (a line implies a continuum); more than three or four lines intersect (use small multiples); the data are stacked (use an area chart, but v2.0 has no specific area notation).
- **Variants:** Selective labels; indexed lines; multiple lines with semantic colors; line-plus-column overlays.
- **Source:** p. 105–106.

### Other horizontal charts

- **Area chart:** A filled chart for stacked data or continuous accumulation. V2.0 has **no specific notation concept**; derive it from column and line notation and state the derivation.
- **Boxplot (range chart):** Shows a distribution or range. V2.0 has **no specific notation concept**; derive it from column notation.
- **Source:** p. 106.

## 3. Vertical charts (structure analyses)

### Single bar

- **Purpose:** Compare one data series across structure categories in one period or point in time.
- **Anatomy:** Vertical category axis with structure labels; one bar per category extending from the axis; bars in front of the axis; legend in the title; positive labels to the right, negative to the left; bar width 2/3 of category width for absolute measures (1/3 for relative).
- **Use when:** The comparison across countries, products, divisions, or other structure categories is the message.
- **Avoid when:** Time is the main dimension (use a horizontal chart); there are too many categories to read (use a remainder bar).
- **Variants:** Sorted bars; bars with highlighting; bars with remainder.
- **Source:** p. 107–108.

### Stacked bar

- **Purpose:** Show the composition of a total across structure categories.
- **Anatomy:** Vertical category axis; bars divided into segments; legends above the top bar or below the bottom bar, horizontally centered; segment labels inside; total label to the right of positive bars / left of negative bars; most important series at the axis.
- **Use when:** Multiple series, all values have the same sign, and composition matters.
- **Avoid when:** Mixed signs; too many series; values vary too much.
- **Variants:** 100% stacked bars; stacked bars with plan/forecast notation.
- **Source:** p. 108–109.

### Grouped bar

- **Purpose:** Compare a primary scenario with a reference scenario across structure categories.
- **Anatomy:** Vertical category axis; two overlapping bars per category, reference behind primary; primary in the foreground; reference above or below according to creation date; a third scenario can use a reference triangle.
- **Use when:** The category-level scenario comparison is the message.
- **Avoid when:** More than two or three scenarios would be unreadable; a variance pin tier would be clearer.
- **Variants:** Primary bar with reference triangles; grouped bars plus a variance tier.
- **Source:** p. 109–110.

### Vertical pin

- **Purpose:** Show relative variances by structure category.
- **Anatomy:** Vertical category axis; one very thin bar per category; pin length = relative variance; color green/red by impact; pin head filled to show the primary scenario; labels to the right of positive pins, left of negative pins; pin in the foreground.
- **Use when:** The relative variance by category is the message.
- **Avoid when:** The absolute variance is the message (use bars); the denominator is negative or meaningless (use `N/A`).
- **Variants:** Pins with reference axis outline; pins with annotation references.
- **Source:** p. 110–111.

### Calculation waterfall

- **Purpose:** Explain a calculation from a base measure to a result measure.
- **Anatomy:** Vertical category axis; base and total bars for base and result measures; contribution bars for additions and subtractions in the calculation scheme; intermediate subtotal bars for complex schemes; each bar starts at the end of the preceding bar; assisting lines connect successive bars.
- **Use when:** A P&L, cost build-up, or other calculation scheme is the message.
- **Avoid when:** The relationship is not additive; a table alone would be clearer for exact lookup.
- **Variants:** P&L waterfall; cost waterfall; multi-subtotal calculation.
- **Source:** p. 111–112.

### Variance waterfall (vertical)

- **Purpose:** Explain structure variances between two periods or scenarios.
- **Anatomy:** Vertical category axis; base and total bars for values at different times/scenarios; contribution bars for structure categories; assisting lines connect successive bars.
- **Use when:** The category contributions to a total variance are the message.
- **Avoid when:** The measure is a stock (use a growth waterfall); contributions are not additive.
- **Variants:** Plan-to-actual structure bridge; previous-year-to-actual structure bridge.
- **Source:** p. 112.

### Remainder bar

- **Purpose:** Keep a structure analysis exhaustive when there are too many categories to display.
- **Anatomy:** A single bar accumulating the smallest categories that cannot be shown individually; sorted by descending size; separated from the other bars by a wider gap; labeled “Rest of…” or equivalent; excluded from averaging, ranking, and selecting.
- **Use when:** Many structure categories and the smallest ones are not individually important.
- **Avoid when:** Every category matters or the remainder would hide a material item.
- **Variants:** Remainder row/column in a table.
- **Source:** p. 113.

### Other vertical charts

- **Vertical boxplot (range chart):** V2.0 has **no specific notation concept**; derive it from standard bar notation.
- **Lines and areas in vertical charts:** Avoid them; they imply a continuum that structure analyses do not have.
- **Source:** p. 113.

## 4. Charts with two value axes

### Scattergram

- **Purpose:** Show the relationship between two measures.
- **Anatomy:** Two value axes; points positioned in a two-dimensional coordinate system; labels or annotations for notable points; axes scaled and labeled clearly.
- **Use when:** Correlation, clustering, or outlier position is the message.
- **Avoid when:** One-dimensional comparison would answer the question; exact values are needed (use a table).
- **Variants:** Quadrant lines; trend line; labeled clusters.
- **Source:** p. 113–114.

### Bubble chart (portfolio chart)

- **Purpose:** Show a relationship among three measures.
- **Anatomy:** Two value axes; bubbles positioned by two measures; bubble **area** encodes the third measure; bubbles labeled; a fourth dimension can be shown with pie segments inside the bubbles.
- **Use when:** Portfolio position and relative size are the message.
- **Avoid when:** The third measure is better compared with bars; bubble areas are not proportional; too many overlapping bubbles.
- **Variants:** Bubble pie chart; quadrant portfolio.
- **Source:** p. 114.

### Other two-value-axis charts

- **Status:** V2.0 has **no specific notation rules** for charts with two value axes. Derive the notation from columns, bars, and lines.
- **Examples:** Continuous horizontal timeline; columns or bars of variable width.
- **Source:** p. 114–115.

## 5. Table taxonomy

### Table types

| Type | Purpose | Structure |
|---|---|---|
| **Time series table** | Time-series analysis | Time columns + measure rows or structure rows. |
| **Variance table** | Scenario analysis | Scenario columns + variance columns + measure rows or structure rows. |
| **Cross table** | Structure analysis | Structure columns + structure rows. |
| **Combined table** | Multiple analyses | More than one column type and/or row type, side by side or nested. |

### Column types

| Column type | Content | Design |
|---|---|---|
| **Row header** | Row names | Usually far left; short texts; wider gap before numbers. |
| **Scenario** | AC, PY, PL, BU, FC | Same width for all scenario columns; order per UN 4.1. |
| **Variance** | `ΔPL`, `ΔPY`, `ΔPL%`, `ΔPY%` | Same width/scale as base where applicable; sign and color semantics. |
| **Time** | Periods or points in time | Temporal order left to right. |
| **Measure** | Sales, headcount, equity | Glossary abbreviations; wider gap after intermediate results. |
| **Structure** | Countries, products, divisions | Categories of a structure dimension. |
| **Of which** | Details of an aggregate that do not total to it | Smaller font/narrower width; right of mother column; not separated from it. |
| **Remainder** | Accumulated smaller categories | Normal gap within the group; label “Other…”. |
| **Percent of** | Share of a given total | Smaller/narrower; state the base. |
| **Totals** | Totals of a group | Right of group; bold/light-gray; consistent. |
| **Hierarchical** | Multiple levels | Wider gaps; parent columns right of children. |
| **Nested** | One type repeats within another | Wider gaps between groups. |

### Row types

| Row type | Content | Design |
|---|---|---|
| **Column header** | Column names | Top; may use multiple lines; abbreviate. |
| **Measure** | Sales, cost, profit | Result rows separated by solid lines; bold/light-gray. |
| **Structure** | Countries, products, divisions | Categories of a structure dimension. |
| **Of which** | Details of an aggregate that do not total to it | Aggregate above; smaller/lighter; no horizontal line; right-aligned header. |
| **Remainder** | Accumulated smaller categories | Normal row height; label “Rest of…”; exclude from averaging/ranking/selecting. |
| **Percent of** | Share of a given total | Smaller font, italic, or smaller height. |
| **Totals** | Totals of a group | Below group; solid line; bold/light-gray. |
| **Hierarchical** | Multiple levels | Parent rows below children; wider gaps. |
| **Nested** | One type repeats within another | Wider gaps between groups. |

### Layout rules

- Use identical widths for columns of the same type, independent of header text length.
- Right-align numeric columns and their headers; left-align text columns and their headers. Combined column headers may be centered or left-aligned for legibility.
- Use very light or omitted vertical lines; use white vertical lines or gaps. A narrow gap separates columns of the same type; a wider gap separates groups.
- Use identical row heights within a row type.
- Use light horizontal lines where they increase legibility; use solid lines to separate results and totals.
- Put time periods, scenarios, and variances in columns, not rows.
- Place totals columns to the right of their group and totals rows below their group.
- Place parent columns to the right of child columns and parent rows below child rows.
- Place “of which” columns/rows adjacent to the aggregate, visually subordinate, and not totalling to it.
- Exclude remainder categories from averaging, ranking, and selecting.

## 6. Table vs chart

| Need | Use a table | Use a chart |
|---|---|---|
| Look up an exact value | Yes | No |
| Compare magnitudes at a glance | No | Yes |
| Show a pattern, trend, or distribution | No | Yes |
| Convey a key message | Usually no | Yes |
| Present many precise values with context | Yes | No |
| Show composition and part-to-whole | A table can list shares | Stacked bars/columns are faster |
| Prove a specific numeric claim | Yes, with the relevant cells | A chart can show the pattern, but not the precision |

Tables have high information density, are clear and honest, and do not compete with charts. Charts are inherently selective and are used to convey a message. A chart conveying a key message cannot be replaced by a table; a table needed for lookup should not be replaced by a chart with dense labels.

## 7. Deferred and derived notation

The following have **no complete specific notation concept in v2.0**:

- Area charts.
- Boxplot/range charts.
- Charts with two value axes.
- Selecting in structure analyses.
- A comprehensive measure-type notation beyond absolute/relative.
- Visualization of adjustment analyses.
- Additional scaling visualizations beyond scale bands.

For these, derive a consistent treatment from the closest specified chart and say that the derivation is not a normative IBCS rule.
