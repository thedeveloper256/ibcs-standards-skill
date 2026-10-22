# Power BI Implementation Guide

Illustrative patterns for Power BI Desktop and the Power BI service. The format pane, theme schema, and visual capabilities change between versions; validate every snippet in the version you deploy. Hex values are non-normative starter tokens; IBCS does not prescribe exact color codes. Keep them consistent within the organization.

## What the tool does natively

Power BI natively supports:

- column, bar, line, combo, scatter, and waterfall visuals;
- a zero-based value axis (set the axis minimum to 0);
- solid fills, transparency, and border options on many visuals;
- conditional formatting of color, font color, and background by measure or rule;
- data labels and custom label formats;
- tables and matrices with measures, conditional formatting, and custom number formats;
- small multiples on several core visuals;
- theme JSON for data colors, fonts, and some visual style defaults;
- accessibility features (alt text, tab order, high-contrast themes).

Power BI does **not** natively provide, on the core column/bar visual:

- per-series hatch or pattern fills;
- reliable per-series outline-only columns (the fill can be made transparent, but that is not the same as a true hollow column with an independent border, and border controls are limited);
- per-series bar widths within one visual;
- native IBCS scenario fills (solid/outlined/hatched) as a built-in formatting option.

## IBCS mapping

| IBCS element | Native Power BI approach | Fidelity |
|---|---|---|
| AC solid dark | Solid fill `#4D4D4D` | Native. |
| PY solid light | Solid fill `#BFBFBF` | Native. |
| PL/BU outlined | Transparent fill + border, or an SVG/custom visual | Partial/native border; true outline-only is limited. |
| FC outlined + hatched | SVG/HTML/custom visual; no native hatch on core visuals | Workaround required. |
| Absolute measure width (2/3) | Spacing/gap controls approximate category width; per-series width is limited | Approximate. |
| Relative measure width (1/3) | Separate visual or custom visual; pins are not a native chart type | Workaround required. |
| Variance green/red/blue | Conditional formatting by a color measure | Native. |
| Zero baseline | Y-axis minimum = 0 | Native. |
| Scale band | Reference line/band or a shape overlay | Workaround. |
| Small multiples with same scale | Small multiples + fixed axis min/max | Native, with care. |
| Table bars | Data bars or SVG in a table/custom visual | Partial. |
| Sparklines | Native sparklines in matrices (where available) or custom visual | Version-dependent. |

## Limitations and workarounds

### Pattern fills and outlines

The core column/bar visual accepts a solid color and limited border/transparency settings. It does not expose a hatch pattern per series, and transparency is not a true outline-only fill.

Workarounds, in order of fidelity:

1. **SVG/HTML custom visual.** Draw the bars as inline SVG: `fill="none" stroke="#4D4D4D"` for plan, and `fill="url(#hatch)"` with an SVG `<pattern>` for forecast. Render the SVG through an HTML/SVG-capable custom visual. You control stroke widths, hatch spacing, and labels. You lose some native interactivity and must build axes/labels yourself.
2. **A custom visual that explicitly supports IBCS fills.** Some vendor visuals advertise pattern fills or IBCS styles. Verify the current version and the actual rendering before relying on the claim; vendor claims are not IBCS certification.
3. **Layered native visuals.** A transparent-fill column with a border can approximate an outline, and a second visual can carry a pattern image. This is fragile and rarely worth it for a production page.
4. **Deneb/Vega-Lite.** Outline-only bars are straightforward (`fill: null`, `stroke: ...`). Hatch patterns need an SVG pattern or layered marks; test the renderer. This is a custom-visual path, not a native one.

### Per-series widths

Native column/bar visuals use one gap/width setting for the series. You cannot give AC a 2/3 width and a relative-variance pin a 1/3 width inside one native visual. Use separate visuals or a custom visual; do not fake the distinction with spacing that changes the category axis.

### Small multiples

Set a fixed axis minimum and maximum for the shared scale. Do not rely on automatic scaling across panels, which can give each panel a different range. Verify the small-multiple settings in the current version.

### Tables and matrices

Conditional formatting can color font/background by measure, but it cannot draw a hatch pattern in a cell. For an IBCS variance table with outlined/hatched cells, use a custom visual or generate the table as SVG/HTML. For ordinary tables, use measures and conditional font colors.

### Theme JSON

Theme JSON can set data colors and some visual defaults, but it cannot create pattern fills. Use it for the palette, fonts, and axis defaults; use a custom visual or SVG for the reserved fills.

## Code or configuration

### Theme JSON (illustrative)

```json
{
  "name": "IBCS starter",
  "dataColors": [
    "#4D4D4D",
    "#BFBFBF",
    "#00B050",
    "#C00000",
    "#0070C0",
    "#808080"
  ],
  "visualStyles": {
    "*": {
      "*": {
        "yAxis": [
          {
            "show": true,
            "start": 0
          }
        ],
        "xAxis": [
          {
            "show": true
          }
        ]
      }
    }
  }
}
```

Validate the schema in the current Power BI version. Theme keys are not a stable public contract across every visual.

### DAX measures

```dax
Sales AC = CALCULATE([Sales], 'Scenario'[Scenario] = "AC")
Sales PY = CALCULATE([Sales], 'Scenario'[Scenario] = "PY")
Sales PL = CALCULATE([Sales], 'Scenario'[Scenario] = "PL")
Sales FC = CALCULATE([Sales], 'Scenario'[Scenario] = "FC")

ΔPL = [Sales AC] - [Sales PL]
ΔPY = [Sales AC] - [Sales PY]
// Raw measure returns BLANK for a non-positive denominator; the label measure shows N/A.
ΔPL% = IF([Sales PL] <= 0, BLANK(), DIVIDE([ΔPL], [Sales PL]))

ΔPL% Label =
IF(
    [Sales PL] <= 0,
    "N/A",
    FORMAT([ΔPL%], "+0.0%;-0.0%;0.0%")
)

Variance Color =
SWITCH(
    TRUE(),
    [ΔPL] > 0, "#00B050",
    [ΔPL] < 0, "#C00000",
    "#0070C0"
)
```

For a cost measure, flip the impact before coloring:

```dax
Cost Impact = -1 * [ΔPL]
Cost Color =
SWITCH(
    TRUE(),
    [Cost Impact] > 0, "#00B050",
    [Cost Impact] < 0, "#C00000",
    "#0070C0"
)
```

### Conditional formatting

1. Select the visual or table cell.
2. Open **Format** → **Font color** or **Background color** → **Conditional formatting** (`fx`).
3. Choose **Field value** and select the color measure.
4. Check the result in grayscale and high-contrast mode.

### SVG outline and hatch (illustrative)

```html
<svg xmlns="http://www.w3.org/2000/svg" width="120" height="80" viewBox="0 0 120 80">
  <defs>
    <pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
      <line x1="0" y1="0" x2="0" y2="6" stroke="#4D4D4D" stroke-width="1.2"/>
    </pattern>
  </defs>
  <rect x="10" y="10" width="40" height="60" fill="none" stroke="#4D4D4D" stroke-width="1.2"/>
  <rect x="60" y="10" width="40" height="60" fill="url(#hatch)" stroke="#4D4D4D" stroke-width="1.2"/>
</svg>
```

Encode the SVG as a data URI or use an HTML/SVG-capable custom visual. Test scaling and print/PDF output; SVG text and patterns can render differently across exporters.

### Axis settings

- Select the visual → **Format** → **Y axis**.
- Set **Minimum** to `0`.
- Set **Maximum** to a fixed value for small multiples or comparable charts.
- Turn off gridlines where direct labels suffice.
- Use the same unit and number format across the page.

**Version note:** snippets are illustrative and may require adjustment. Check the current Power BI theme schema, visual capabilities, and custom-visual documentation.

## Accessibility

- Add alt text to every visual; describe the message and the key values, not just the chart type.
- Set a logical tab order.
- Do not rely on color alone; keep signs, labels, and position.
- Test the high-contrast theme and a color-vision simulation.
- Provide a table or downloadable data alternative for key visuals.
- Keep text large enough for the target screen and projector.

## Verification checklist

- [ ] The value axis starts at zero unless the indexed-data exception applies.
- [ ] AC, PY, PL/BU, and FC are visually distinct; no native pattern claim is made without a tested workaround.
- [ ] Variance signs, colors, and `N/A` behavior match UN 4.1.
- [ ] Same-unit charts and small multiples share a fixed scale.
- [ ] Tables show units and definitions; conditional formatting is not the only cue.
- [ ] The page works in grayscale and high contrast.
- [ ] Alt text, tab order, and a data alternative exist.
- [ ] Custom visual/vendor claims are verified in the deployed version.
- [ ] The published PDF/screen output matches the authoring view.
