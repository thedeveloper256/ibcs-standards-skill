# CHECK — Ensure Visual Integrity

CHECK covers all aspects of ensuring visual integrity in reporting. Ensuring visual integrity means presenting information in the most truthful and easily understood way by avoiding misleading visuals.

This chapter covers avoiding manipulated axes and visual components, using the same scales, and showing data adjustments.

**Source:** IBCS v2.0, pages 68–75.

## CH 1 — Avoid manipulated axes

Charts serve as a means to visually compare numerical values. Manipulated axes defeat this purpose of explaining actual interrelations.

### CH 1.1 — Avoid truncated axes

**Requirement.** Value axes should generally start at zero. Do not use a “cut” axis that begins above zero unless the indexed-data exception applies.

**Why.** A truncated axis makes the visual difference between columns or bars appear much larger than the numerical difference. The chart then conveys a message that does not correspond to the underlying values.

**Apply.** Set the value-axis minimum to zero. If the interesting variation is small relative to the absolute level, use a variance chart with a zero line, an indexed chart under the exception below, or a separate detail view. A non-zero axis on a line chart is **not** an explicit v2.0 exception; if an organization uses one, label it clearly and treat it as an editorial choice, not an IBCS rule.

**Exceptions / limits.** Indexed data with only small deviations from 100% may use a non-zero axis so the deviations can be seen. In that case, position the category labels at the 100% line to prevent misinterpretation. The exception does not license a truncated axis on an ordinary absolute-value column chart.

**Audit.** Does the value axis start at zero? If not, is this an indexed chart used under the documented exception, with labels at 100%?

**See also.** CH 2.1, EX 4.2.

**Source.** p. 68.

### CH 1.2 — Avoid logarithmic axes

**Requirement.** Avoid logarithmic value axes.

**Why.** Audiences perceive bars and columns as largely proportional and linear, especially when they share a common baseline. A logarithmic axis therefore produces a visual impression that differs from the numerical values.

**Apply.** Use a linear axis. If values span several orders of magnitude, consider sizing charts to the data (CH 4.2), scaling markers (CH 4.3), magnifying glasses (CH 4.5), or separate charts.

**Exceptions / limits.** A logarithmic axis can be justified when the analytical purpose is to show relative growth and values span several orders of magnitude. Even then, use it with caution, only when the audience is familiar with it, and clearly indicate that the axis is logarithmic.

**Audit.** Is the axis logarithmic? If so, is the purpose relative growth across orders of magnitude, is the audience familiar, and is the axis clearly marked?

**See also.** CH 4.2, CH 4.3, CH 4.5.

**Source.** p. 69.

### CH 1.3 — Avoid different class sizes

**Requirement.** When categories represent ordered classes, such as age groups in a histogram, use class sizes of identical width.

**Why.** Unequal class widths make the area or length of a bar reflect both the class width and the value, so true visual comparability is impossible.

**Apply.** Use equal-width bins (for example, ten-year age classes). If the source data uses unequal bins, regroup it into equal bins or show a density measure and explain the transformation.

**Exceptions / limits.** None stated in v2.0. A histogram with unequal bins is not a like-for-like comparison.

**Audit.** Do all ordered classes have the same width?

**See also.** EX 1.1.

**Source.** p. 69.

## CH 2 — Avoid manipulated visual components

Displaying values differing by orders of magnitude can be challenging. Use creative solutions instead of clipping visual components or cutting value axes.

### CH 2.1 — Avoid clipped visual components

**Requirement.** Do not clip, break, or truncate columns, bars, or other visual components.

**Why.** Clipped components, such as broken columns, make visual comparisons impossible and therefore mislead the audience.

**Apply.** Use an unbroken component at a true scale. If a value is too large for the chart, change the chart size, use a scale band, an outlier marker, a magnifying glass, or a separate chart instead of breaking the component.

**Exceptions / limits.** No source exception. Outlier markers (CH 4.4) are a separate rule for an unimportant extreme value, not a clipped component.

**Audit.** Is any column, bar, or area broken or clipped?

**See also.** CH 1.1, CH 4.4.

**Source.** p. 70.

### CH 2.2 — Use creative solutions for challenging scaling issues

**Requirement.** Use creative visual components to compare extreme values instead of clipping components or truncating axes.

**Why.** Values that differ by orders of magnitude can still be compared if the visual construction preserves proportionality while giving the small values enough space.

**Apply.** Use two- or three-dimensional components only when their geometry is constructed so that the encoded measure remains proportional and the comparison stays truthful. Examples include nested or segmented containers, detail views, and magnifying glasses. Explain the construction.

**Exceptions / limits.** This rule is distinct from CH 3.1 and CH 3.2. Two- and three-dimensional components are allowed here only as a deliberate scaling solution, not as a way to make areas, diameters, or volumes encode values misleadingly.

**Audit.** Does the creative component preserve a truthful, explainable relationship between the visual and the values? Is it clearly not a misleading area/volume representation?

**See also.** CH 3.1, CH 3.2, CH 4.5.

**Source.** p. 70.

## CH 3 — Avoid misleading representations

Graphical representations are misleading if the visual impression for the observer differs from the underlying values.

### CH 3.1 — Use correct area comparisons, prefer linear ones

**Requirement.** If areas of circles, icons, or emblems represent data, the area must be proportional to the underlying value. Prefer linear comparisons such as columns and bars.

**Why.** Perception is misled when values are encoded by the diameter of a circle or the height of an icon while the reader interprets the visible area. Even a correct area encoding is harder to judge than a linear length.

**Apply.** Prefer columns, bars, or other linear encodings. If an area encoding is unavoidable, calculate the radius from the value (`radius ∝ √value`) so the area is proportional, and label the values.

**Exceptions / limits.** None stated in v2.0. Correct area encoding is permitted but not preferred.

**Audit.** If area encodes a value, is the area (not the diameter or height) proportional to the value? Would a linear comparison be clearer?

**See also.** CH 3.2, CH 2.2.

**Source.** p. 71.

### CH 3.2 — Use correct volume comparisons, prefer linear ones

**Requirement.** If volumes of spheres, cubes, or other three-dimensional components represent data, the volume must be proportional to the underlying value. Prefer linear comparisons.

**Why.** Even when volume is correctly encoded, people find it hard to perceive volume accurately. Encoding values by diameter or surface area is outright misleading.

**Apply.** Prefer columns, bars, or other linear encodings. If a 3D component is unavoidable, construct it so volume is proportional to value, label the values, and explain the construction.

**Exceptions / limits.** None stated in v2.0. Correct volume encoding is permitted but not preferred.

**Audit.** If volume encodes a value, is the volume (not the diameter or surface area) proportional to the value? Would a linear comparison be clearer?

**See also.** CH 3.1, CH 2.2.

**Source.** p. 71.

### CH 3.3 — Avoid misleading colored areas in maps

**Requirement.** Do not use colored map areas to represent non-area-related figures such as market share or return on sales. Use colored areas only for area-related data such as precipitation per square meter or population density.

**Why.** A colored region implies that the entire area shares the value, and larger regions dominate the visual impression even when they are not more important. For non-area data this misleads.

**Apply.** Replace the map with a bar chart, a table, or another suitable chart unless there is a genuine geospatial need. If a map is necessary, position columns or bars of identical scale at the relevant locations, or use point-positioned pie charts for a few locations, as allowed by the exception to EX 2.1.

**Exceptions / limits.** Colored areas are appropriate for area-related measures. Point-positioned pie charts are a narrow exception for a few locations; they do not make colored area maps acceptable for non-area data.

**Audit.** Does the map color encode an area-related measure? If not, is there a genuine geospatial need, and is the encoding point- or symbol-based?

**See also.** EX 2.1, EX 1.1.

**Source.** p. 72.

## CH 4 — Use the same scales

Proper visual comparison requires identical scales for identical measure units, or a clear indication of the difference. If possible, use a consistent scaling concept for the entire reporting.

### CH 4.1 — Use identical scale for the same unit

**Requirement.** When presenting more than one chart of the same unit on one page, use identical scales.

**Why.** Different scales for the same unit make equal values look different and destroy comparability.

**Apply.** Set the same value-axis minimum, maximum, and intervals for charts of the same unit. If the values differ greatly, keep the scale and change the chart size or use scaling markers rather than silently changing the scale.

**Exceptions / limits.** In extreme situations identical scales may not be desirable. In those exceptional cases, use scaling markers (CH 4.3, UN 5.2) to make the difference explicit.

**Audit.** Do all charts with the same unit share the same scale? If not, is the difference clearly marked?

**See also.** CH 4.2, CH 4.3, UN 5.2.

**Source.** p. 72.

### CH 4.2 — Size charts to given data

**Requirement.** Adapt the physical size of charts to the magnitude of their data when using identical scales would otherwise make small values unreadable.

**Why.** A chart of small values can use the same scale as a chart of large values if it is physically smaller; the scale stays comparable while the small values remain visible.

**Apply.** Keep the same units per centimeter or per pixel across charts, and vary the chart's height or width according to the data range. Align the charts on a common baseline.

**Exceptions / limits.** None stated in v2.0. If chart size cannot vary, use scaling markers.

**Audit.** Are charts sized so that identical scales remain readable across different magnitudes?

**See also.** CH 4.1, CH 4.3.

**Source.** p. 73.

### CH 4.3 — Use scaling markers if necessary

**Requirement.** Use scaling markers, such as scale bands, when charts of the same unit use different scales.

**Why.** A scale band gives the reader a common numerical reference across charts and prevents false comparisons.

**Apply.** Draw a scale band that indicates the same numerical height, typically a power of ten, in every chart. Follow the semantic design in UN 5.2: a line parallel to the category axis at the same numerical height, with a light fill between the line and the axis.

**Exceptions / limits.** Scaling markers are a fallback for unavoidable scale differences; identical scales (CH 4.1) remain the default.

**Audit.** Where scales differ, is a consistent scaling marker present and explained?

**See also.** CH 4.1, UN 5.2.

**Source.** p. 73.

### CH 4.4 — Use outlier markers if necessary

**Requirement.** Use outlier markers for values that are very large compared with the other values and unimportant for the business message, so the chart does not have to be scaled to the outlier.

**Why.** Scaling a whole chart to an unimportant outlier compresses the informative values and hides the real pattern.

**Apply.** Mark the outlier in the semantic notation described in UN 5.3: omit the pin head and add a triangle pointing in the direction of growth. Keep the rest of the chart on a readable scale and label the outlier if needed.

**Exceptions / limits.** Do not use an outlier marker for a value that is important to the message. If the outlier matters, change the scale or use a different chart.

**Audit.** Is the outlier unimportant to the message, clearly marked, and excluded from the scale without hiding its existence?

**See also.** UN 5.3, CH 2.1.

**Source.** p. 73–74.

### CH 4.5 — Use magnifying glasses

**Requirement.** Use a “magnifying glass” to zoom into a part of a chart on a larger scale when the main chart's scale hides relevant detail.

**Why.** A detail view preserves the overview while making small but important differences visible.

**Apply.** Mark the area to be zoomed with an appropriate marker and link it to a second chart that shows the same area at a larger scale. Keep the units and labels consistent between the two views.

**Exceptions / limits.** None stated in v2.0. Do not use a magnifying glass to disguise a truncated axis in the main chart.

**Audit.** Is the zoomed area clearly marked and linked, and does the detail view preserve the same units and semantics?

**See also.** CH 1.1, CH 4.2.

**Source.** p. 74.

## CH 5 — Show data adjustments

For longer time series, currency and inflationary effects can bias the visual impression, hiding the real development of business.

### CH 5.1 — Show the impact of inflation

**Requirement.** Make inflation effects transparent when they could distort the interpretation of a time series.

**Why.** Nominal growth can hide a decline in real terms. Without an adjustment, readers may attribute price-driven growth to volume or performance.

**Apply.** Show the nominal and inflation-adjusted series, or annotate the adjustment clearly. State the price index and base period. Use consistent notation for the adjusted series.

**Exceptions / limits.** Short time series or periods with negligible inflation may not need an adjustment; state that choice if it could affect interpretation.

**Audit.** Does the page show or explain the inflation impact where it matters?

**See also.** CH 5.2, UN 4.4.

**Source.** p. 74.

### CH 5.2 — Show the currency impact

**Requirement.** Make currency effects transparent when they could distort the interpretation of a time series.

**Why.** Exchange-rate movements can create or hide growth in reported currency, especially in international reporting.

**Apply.** Show the reported-currency and constant-currency series, or annotate the adjustment clearly. State the exchange-rate basis and the conversion method. Keep the adjustment consistent across the page.

**Exceptions / limits.** Reports entirely in one currency with no material exchange-rate exposure may not need an adjustment; state that choice if it could affect interpretation.

**Audit.** Does the page show or explain the currency impact where it matters?

**See also.** CH 5.1, UN 4.4.

**Source.** p. 75.
