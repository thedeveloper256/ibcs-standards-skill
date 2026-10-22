# HTML/JS Implementation Guide

Illustrative patterns for browser-rendered reports: CSS, SVG, ECharts, D3, Chart.js, and Vega-Lite. Library APIs and pattern support vary by version; verify in the target browser and in print/PDF. Hex values are non-normative starter tokens; IBCS does not prescribe exact color codes. Keep them consistent within the organization.

## What the tool does natively

Browser-based rendering supports:

- CSS borders and backgrounds, including repeating gradients for hatching;
- inline SVG, including `<pattern>` definitions for precise hatch spacing;
- ECharts: bars, lines, scatter, custom series, decal patterns, and responsive layout;
- D3: complete control over SVG shapes, patterns, scales, axes, and labels;
- Chart.js: bars, lines, scatter, responsive layout, and canvas rendering;
- Vega-Lite: declarative marks, scales, facets (small multiples), and zero-based scales;
- accessible HTML tables with headers, captions, and ARIA;
- print styles via `@media print`.

There is no single “IBCS mode” in these libraries. You must encode the semantics explicitly.

## IBCS mapping

| IBCS element | CSS/SVG | ECharts | D3 | Chart.js | Vega-Lite |
|---|---|---|---|---|---|
| AC solid dark | `fill: #4D4D4D` | `itemStyle.color` | `fill` | `backgroundColor` | `color` |
| PY solid light | `fill: #BFBFBF` | `itemStyle.color` | `fill` | `backgroundColor` | `color` |
| PL/BU outlined | `fill: none; stroke: #4D4D4D` | `itemStyle.color: transparent`, `borderColor`, `borderWidth` | `fill: none; stroke` | `backgroundColor: transparent`, `borderColor`, `borderWidth` | `fill: null`, `stroke` |
| FC outlined + hatched | SVG `<pattern>` or CSS repeating gradient | `decal` + border | SVG `<pattern>` | CanvasPattern + border | SVG pattern (or custom Vega) |
| Absolute width 2/3 | CSS width / SVG rect width | `barWidth: '66%'` | scale band width × 0.66 | `barPercentage`/`categoryPercentage` | `size` / band scale |
| Relative width 1/3 | CSS/SVG thinner element | `barWidth: '33%'` | scale band × 0.33 | custom | `size` |
| Zero baseline | scale domain starts at 0 | `yAxis.min: 0` | `y.domain([0, max])` | `beginAtZero: true` | `"scale": {"zero": true}` |
| Variance colors | per-element class/fill | `itemStyle.color` callback | per-datum fill | per-datum color | `color` encoding |
| Small multiples | CSS grid | multiple chart instances | multiple `<svg>` | multiple canvases | `facet` |

## Limitations and workarounds

- **Chart.js patterns:** no native hatch. Create an offscreen canvas, draw the hatch, create a `CanvasPattern` with `ctx.createPattern`, and assign it to `backgroundColor`. Test at device pixel ratio and in print.
- **ECharts patterns:** `decal` patterns are supported in recent versions; exact appearance and export support vary. For precise control, use an SVG pattern or a custom series.
- **Vega-Lite patterns:** pattern fills are not a simple built-in mark property. Use SVG defs or a custom Vega spec; otherwise use solid/outline and accept the limitation.
- **SVG in print:** patterns can alias or disappear at small sizes. Use a pattern size that survives the final print resolution and test the PDF.
- **Responsive layout:** a chart that looks right on a wide screen may clip labels on a narrow one. Define breakpoints and test the smallest supported width.
- **Canvas accessibility:** charts drawn on `<canvas>` are not readable by screen readers. Provide an accessible table or a text summary.
- **Color management:** browser RGB and print CMYK differ; do not rely on subtle hue differences.

## Code or configuration

### CSS hatch and outline

```css
.ibcs-plan {
  fill: none;
  stroke: #4d4d4d;
  stroke-width: 1.2;
}

.ibcs-forecast {
  fill: url(#hatch);
  stroke: #4d4d4d;
  stroke-width: 1.2;
}

.ibcs-hatch-css {
  border: 1.2px solid #4d4d4d;
  background-image: repeating-linear-gradient(
    45deg,
    #4d4d4d 0,
    #4d4d4d 1px,
    transparent 1px,
    transparent 6px
  );
}
```

### SVG pattern

```html
<svg width="240" height="120" role="img" aria-labelledby="chart-title chart-desc">
  <title id="chart-title">Plan and forecast columns</title>
  <desc id="chart-desc">Plan is outlined; forecast is outlined and hatched.</desc>
  <defs>
    <pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse"
             patternTransform="rotate(45)">
      <line x1="0" y1="0" x2="0" y2="6" stroke="#4d4d4d" stroke-width="1.2"/>
    </pattern>
  </defs>
  <rect x="20" y="20" width="60" height="80" fill="none"
        stroke="#4d4d4d" stroke-width="1.2"/>
  <rect x="120" y="20" width="60" height="80" fill="url(#hatch)"
        stroke="#4d4d4d" stroke-width="1.2"/>
</svg>
```

### ECharts: zero baseline, widths, labels, and decal

```js
const option = {
  grid: { left: 48, right: 24, top: 24, bottom: 32 },
  xAxis: { type: 'category', data: months, axisTick: { show: false } },
  yAxis: { type: 'value', min: 0, name: 'EUR m' },
  series: [
    {
      name: 'PL',
      type: 'bar',
      data: plan,
      barWidth: '66%',
      itemStyle: {
        color: 'transparent',
        borderColor: '#4d4d4d',
        borderWidth: 1.2
      }
    },
    {
      name: 'FC',
      type: 'bar',
      data: forecast,
      barWidth: '66%',
      itemStyle: {
        color: '#ffffff',
        borderColor: '#4d4d4d',
        borderWidth: 1.2,
        decal: {
          symbol: 'rect',
          dashArrayX: [1, 0],
          dashArrayY: [2, 5],
          color: '#4d4d4d'
        }
      },
      label: { show: true, position: 'top' }
    }
  ]
};
```

ECharts `decal` support and exact options depend on version; test the exported image/PDF. For a pin chart, use a very small `barWidth` and a separate scatter series for the head.

### Chart.js: zero baseline and canvas hatch

```js
function hatchPattern(ctx, color = '#4d4d4d', size = 6) {
  const canvas = document.createElement('canvas');
  canvas.width = size;
  canvas.height = size;
  const p = canvas.getContext('2d');
  p.strokeStyle = color;
  p.lineWidth = 1;
  p.beginPath();
  p.moveTo(0, size);
  p.lineTo(size, 0);
  p.stroke();
  return ctx.createPattern(canvas, 'repeat');
}

const ctx = document.getElementById('sales').getContext('2d');
new Chart(ctx, {
  type: 'bar',
  data: {
    labels: months,
    datasets: [
      {
        label: 'PL',
        data: plan,
        backgroundColor: 'transparent',
        borderColor: '#4d4d4d',
        borderWidth: 1.2
      },
      {
        label: 'FC',
        data: forecast,
        backgroundColor: hatchPattern(ctx),
        borderColor: '#4d4d4d',
        borderWidth: 1.2
      }
    ]
  },
  options: {
    scales: {
      y: { beginAtZero: true, title: { display: true, text: 'EUR m' } }
    },
    plugins: { legend: { position: 'top' } }
  }
});
```

### D3: pattern and zero baseline

```js
const svg = d3.select('#chart').append('svg')
  .attr('width', width).attr('height', height);

const defs = svg.append('defs');
const hatch = defs.append('pattern')
  .attr('id', 'hatch')
  .attr('width', 6).attr('height', 6)
  .attr('patternUnits', 'userSpaceOnUse')
  .attr('patternTransform', 'rotate(45)');
hatch.append('line')
  .attr('x1', 0).attr('y1', 0).attr('x2', 0).attr('y2', 6)
  .attr('stroke', '#4d4d4d').attr('stroke-width', 1.2);

const y = d3.scaleLinear().domain([0, d3.max(data, d => d.value)]).nice()
  .range([height - margin.bottom, margin.top]);
```

### Vega-Lite: zero baseline and facets

```json
{
  "mark": {"type": "bar", "stroke": "#4d4d4d", "strokeWidth": 1.2},
  "encoding": {
    "x": {"field": "month", "type": "ordinal", "axis": {"labelAngle": 0}},
    "y": {"field": "value", "type": "quantitative", "scale": {"zero": true}},
    "color": {"field": "scenario", "type": "nominal"},
    "column": {"field": "region", "type": "nominal"}
  }
}
```

Pattern fills are not a simple native Vega-Lite mark property; use SVG defs or a custom Vega spec if hatching is required.

### Accessible table

```html
<table>
  <caption>Net sales by region, EUR m, FY2026 actual vs plan</caption>
  <thead>
    <tr>
      <th scope="col">Region</th>
      <th scope="col">AC</th>
      <th scope="col">PL</th>
      <th scope="col">ΔPL</th>
      <th scope="col">ΔPL%</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">North</th>
      <td>38.2</td>
      <td>42.0</td>
      <td>−3.8</td>
      <td>−9.0%</td>
    </tr>
  </tbody>
</table>
```

### Print styles

```css
@media print {
  body { background: #fff; color: #000; }
  .no-print { display: none; }
  .chart { break-inside: avoid; }
  a[href]::after { content: " (" attr(href) ")"; }
}
```

## Accessibility

- Use semantic HTML tables with `<caption>`, `<th scope="col">`, and `<th scope="row">`.
- Give charts a text alternative: a summary sentence, a data table, or both.
- Use `role="img"` and `aria-labelledby`/`aria-describedby` for SVG.
- Keep focus order logical; make interactive controls keyboard-accessible.
- Do not rely on color; include signs, labels, and patterns.
- Test with a screen reader, keyboard only, high contrast, and a color-vision simulator.
- Respect `prefers-reduced-motion`; disable nonessential animation.

## Verification checklist

- [ ] Every value axis starts at zero unless the indexed-data exception applies.
- [ ] Bar widths reflect measure type: 2/3 for absolute, 1/3 or thinner for relative/pins.
- [ ] AC, PY, PL/BU, and FC fills are correct; hatch renders in print/PDF.
- [ ] Variance signs, labels, colors, and `N/A` behavior match UN 4.1.
- [ ] Small multiples share type and scale.
- [ ] The chart has an accessible name and a data alternative.
- [ ] The table has a caption, scoped headers, and units.
- [ ] Keyboard and screen-reader navigation work.
- [ ] Print styles avoid clipping and background loss.
- [ ] The page survives grayscale and color-vision checks.
