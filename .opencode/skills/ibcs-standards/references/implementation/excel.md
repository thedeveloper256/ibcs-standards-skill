# Excel Implementation Guide

Illustrative patterns for Microsoft Excel (Microsoft 365 and recent perpetual versions). Menu names, chart capabilities, and pattern options vary by version and platform; verify in the version you use. Hex values are non-normative starter tokens; IBCS does not prescribe exact color codes. Keep them consistent within the organization.

## What the tool does natively

Excel natively supports:

- column, bar, line, combo, scatter, and waterfall charts (waterfall in newer versions);
- a zero-based value axis via **Format Axis** → **Bounds** → **Minimum**;
- solid fills, no fill, borders, and pattern fills on many chart elements;
- data labels with custom number formats and label positions;
- tables with custom number formats, borders, and conditional formatting;
- small multiples in Microsoft 365 for some chart types, or separate charts aligned manually;
- pattern fills in cells (Format Cells → Fill → Pattern Style);
- data bars in cells (conditional formatting).

The core chart engine has important limits for IBCS:

- **Per-series bar/column width:** Excel's **Gap Width** applies to the whole chart, not to individual series. You cannot make AC 2/3 width and a relative pin 1/3 width in one native chart.
- **Outline-only columns:** possible by setting the series fill to **No Fill** and adding a border, but the border applies to the series and may not survive every chart type/export cleanly.
- **Hatch:** pattern fill is available for many chart elements, but the available patterns and their scaling are limited; it is not a precise SVG hatch. Test print/PDF output.
- **True pins:** no native pin chart; use a very narrow column/bar series, or shapes/error bars.
- **Small multiples:** version-dependent; manual alignment is often needed.

## IBCS mapping

| IBCS element | Native Excel approach | Fidelity |
|---|---|---|
| AC solid dark | Solid fill `#4D4D4D` | Native. |
| PY solid light | Solid fill `#BFBFBF` | Native. |
| PL/BU outlined | No Fill + solid border | Native, with care. |
| FC outlined + hatched | Pattern fill + border; choose a diagonal pattern | Approximate; pattern scale/spacing limited. |
| Absolute measure width (2/3) | Gap Width approximate; per-series width not available | Approximate. |
| Relative measure width (1/3) | Separate chart or narrow series; pins need a workaround | Workaround. |
| Variance green/red/blue | Per-point fills or conditional formatting | Native. |
| Zero baseline | Axis Minimum = 0 | Native. |
| Scale band | Shape overlay or a stacked area/column helper series | Workaround. |
| Small multiples | Microsoft 365 feature or aligned separate charts | Version-dependent. |
| Table bars | Data bars or shape overlays | Partial. |

## Limitations and workarounds

- **Different widths per series:** separate the series into different charts, or use shapes layered over a plot area. Do not use Gap Width tricks that move the category axis.
- **Outline and hatch on the same series:** set **Fill → No Fill**, then **Border → Solid line**; for hatch, use **Fill → Pattern fill** and a border. The pattern is drawn by Excel, not by an SVG; check its density at final print size.
- **Negative values and labels:** use **Outside End** labels and a custom format with an explicit sign. Verify that negative labels do not collide with the category axis.
- **Axis scaling:** set Minimum 0 and a fixed Maximum where charts must match. Do not use "Auto" for small multiples.
- **Tables:** remove vertical borders, right-align numbers, and use custom number formats. Excel's gridlines are not a substitute for table structure.
- **Data bars:** a cell data bar can approximate a table bar, but its scale is per cell/range and can mislead. Use a fixed minimum/maximum and label the values.
- **Waterfall:** Excel's waterfall chart is convenient but its automatic totals/connectors may not match IBCS. A stacked-column bridge with invisible base series gives more control.
- **Exports:** pattern fills and borders may render differently in PDF or when copied to PowerPoint. Test the final artifact.

## Code or configuration

### Zero-based axis (UI)

1. Select the value axis.
2. **Format Axis** → **Axis Options**.
3. **Bounds** → **Minimum** = `0`.
4. Set **Maximum** to a fixed value when charts must share a scale.
5. **Units** → set a consistent major unit.
6. **Tick Marks** and **Labels** → adjust or remove where direct labels suffice.

### Zero-based axis (VBA)

```vb
Sub SetZeroBaseline()
    Dim cht As Chart
    Set cht = ActiveChart
    If cht Is Nothing Then Exit Sub
    cht.Axes(xlValue).MinimumScale = 0
    cht.Axes(xlValue).HasMajorGridlines = False
End Sub
```

### Number formats

```text
#,##0;(#,##0)                 ' one negative format, no plus on positives
+#,##0;-#,##0;0               ' variance labels: explicit plus/minus
0.0%;-0.0%;0.0%               ' percentages
```

Use one decimal sign and one thousands delimiter consistently. Do not mix `1,234.5` and `1.234,5` in the same report.

### Outline-only series (UI)

1. Select the series.
2. **Format Data Series** → **Fill** → **No Fill**.
3. **Border** → **Solid line** → color `#4D4D4D`, width about `1.2 pt`.
4. Add data labels; set **Label Position** → **Outside End**.

### Hatched forecast (UI)

1. Select the forecast series.
2. **Format Data Series** → **Fill** → **Pattern fill**.
3. Choose a diagonal pattern (for example, light upward diagonal).
4. Set **Foreground** to `#4D4D4D` and **Background** to white.
5. **Border** → **Solid line** → `#4D4D4D`, about `1.2 pt`.
6. Check the pattern at print size; Excel patterns can look dense or moiré.

### Small multiples

- Use **Insert** → **Small Multiples** if your Excel version offers it for the chart type; otherwise duplicate the chart for each category.
- Set the same **Minimum**, **Maximum**, and **Major unit** on every value axis.
- Align chart areas and plot areas precisely; use the same category order.
- Put one shared legend and one shared title on the page, not one per panel.

### Table layout

- Remove vertical borders; use whitespace and alignment.
- Right-align numbers and headers; left-align text.
- Put totals below the group and bold them; separate with a solid line.
- Use **Format Cells** → **Number** → **Custom** for the report format.
- Use **Conditional Formatting** for variance font colors, but keep the sign as the primary cue.

**Version note:** the exact menu path and pattern availability vary by Excel version and platform. The snippets are illustrative; record a macro or verify in the target version.

## Accessibility

- Add alt text to charts and images.
- Use sufficient contrast; do not put light gray text on white.
- Do not rely on color; keep signs, labels, and data values.
- Test in grayscale and with a color-vision simulator.
- Use real tables for tabular data, with header rows and units.
- Check the printed/PDF version for clipped labels and pattern artifacts.

## Verification checklist

- [ ] The value axis minimum is 0 unless the indexed-data exception applies.
- [ ] Charts of the same unit share the same scale.
- [ ] AC, PY, PL/BU, and FC fills are correct; hatch is tested in print/PDF.
- [ ] Variance signs, colors, and number formats match UN 4.1.
- [ ] Per-series width limitations are handled without misleading spacing.
- [ ] Table numbers are right-aligned; vertical lines are removed; totals are placed correctly.
- [ ] Small multiples share scale and alignment.
- [ ] The page survives grayscale and color-vision checks.
- [ ] Alt text and a data alternative exist.
