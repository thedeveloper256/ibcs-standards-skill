# Python Implementation Guide

Illustrative patterns for matplotlib and plotly. APIs and rendering behavior vary by version; verify against the installed version and test the exported medium (screen, PDF, PNG). Hex values are non-normative starter tokens; IBCS does not prescribe exact color codes. Keep them consistent within the organization.

## What the tool does natively

**matplotlib** supports:

- zero-based axes (`ax.set_ylim(bottom=0)`);
- bar/column widths (`width`), including per-bar widths;
- outline-only patches (`facecolor='none'`, `edgecolor=...`);
- hatch patterns (`hatch='///'`, `hatch='...'`, `hatch='xxx'`);
- per-bar colors, edge colors, and line widths;
- line charts, scattergrams, and bubble charts;
- waterfall-style bars via `bottom=`;
- tables via `ax.table` or a separate table library;
- small multiples via `plt.subplots(..., sharex=True, sharey=True)`;
- PDF/SVG/PNG export.

**plotly** supports:

- zero-based axes (`range=[0, max]` or `autorange` with `rangemode='tozero'`);
- bar widths and gap control;
- outlined bars via transparent fill plus marker line;
- pattern fills via `marker.pattern` (support and export behavior vary by version and renderer);
- waterfall traces (`go.Waterfall`);
- subplots and small multiples (`make_subplots`);
- interactive labels and hover text;
- HTML export and static image export (static export needs Kaleido or an equivalent renderer).

## IBCS mapping

| IBCS element | matplotlib | plotly |
|---|---|---|
| AC solid dark | `color='#4D4D4D'` | `marker_color='#4D4D4D'` |
| PY solid light | `color='#BFBFBF'` | `marker_color='#BFBFBF'` |
| PL/BU outlined | `facecolor='none', edgecolor='#4D4D4D', linewidth=1.2` | `marker=dict(color='rgba(0,0,0,0)', line=dict(color='#4D4D4D', width=1.2))` |
| FC outlined + hatched | `facecolor='white', edgecolor='#4D4D4D', hatch='///'` | `marker=dict(pattern=dict(shape='/', fgcolor='#4D4D4D', bgcolor='white'), line=dict(color='#4D4D4D', width=1.2))` |
| Absolute measure width | `width=0.66` of category | `width=0.66` (category units) |
| Relative measure width | `width=0.33` | `width=0.33` |
| Variance green/red/blue | explicit color list | explicit `marker_color` list |
| Zero baseline | `ax.set_ylim(bottom=0)` | `yaxis=dict(rangemode='tozero')` |
| Scale band | `ax.axhspan(0, band, color=..., alpha=...)` | `fig.add_hrect(...)` |
| Outlier marker | custom marker/annotation | custom marker symbol/annotation |
| Small multiples | `plt.subplots(..., sharey=True)` | `make_subplots(..., shared_yaxes=True)` |

**Rule of thumb:** encode every semantic distinction explicitly. Do not rely on a library default palette or on automatic axis limits.

## Limitations and workarounds

- **Hatch color:** matplotlib ties hatch color to `edgecolor` (and sometimes a global `hatch.color`). If you need a different hatch and border color, use `matplotlib.rc_context` or draw a second outline patch. Test the export.
- **Hatch density:** controlled by repeating characters (`/`, `//`, `///`). Hatch line width is a global rcParam (`hatch.linewidth`), not a per-artist property.
- **Per-series widths:** matplotlib supports different widths per call/bar, but a single `bar` call with an array of widths can make legends and grouping awkward. Draw series separately and build the legend manually.
- **Plotly patterns:** `marker.pattern` support depends on plotly version and renderer; static image exporters may not render patterns. Always inspect the exported PDF/PNG, not only the browser preview.
- **Plotly waterfall:** the built-in waterfall is convenient but its automatic totals/connectors may not match IBCS exactly. You can build a manual waterfall with `go.Bar` and `base=` for full control.
- **Tables:** `ax.table` is functional but typographically limited. For publication-quality tables, generate HTML or use a dedicated table renderer.
- **Fonts:** a non-default font may not embed correctly in PDF. Verify embedding and fallback behavior.
- **Color management:** screen RGB and print CMYK can shift. Test the final output and keep contrast.

## Code or configuration

### matplotlib: three-tier sales page skeleton

```python
import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
ac = np.array([9.8, 10.1, 10.6, 10.9, 11.2, 11.4, 10.9, 10.5, 11.0, 10.6, 10.2, 11.2])
pl = np.array([10.2, 10.4, 10.9, 11.1, 11.5, 11.8, 11.3, 11.0, 11.4, 11.2, 11.0, 12.8])
# Illustrative monthly path: totals match Example 1 (AC 128.4, PL 134.6), but the Q4/H2 path is not identical.
x = np.arange(len(months))
abs_var = ac - pl
# NaN = N/A: skip the pin and label it N/A; do not plot a misleading 0%.
rel_var = np.full_like(ac, np.nan, dtype=float)
np.divide(ac - pl, pl, out=rel_var, where=pl > 0)
rel_var *= 100

fig, (ax1, ax2, ax3) = plt.subplots(
    3, 1, figsize=(12, 7), sharex=True,
    gridspec_kw={"height_ratios": [3.2, 1.4, 1.0]}, constrained_layout=True
)

# Primary tier: grouped columns, each 2/3 category width, reference behind.
w = 0.66
ax1.bar(x + 0.08, pl, width=w, facecolor="none", edgecolor="#4D4D4D",
        linewidth=1.2, label="PL", zorder=2)
ax1.bar(x - 0.08, ac, width=w, color="#4D4D4D", label="AC", zorder=3)
ax1.set_ylim(bottom=0)
ax1.set_ylabel("EUR m")
ax1.legend(frameon=False, ncol=2, loc="upper left")
ax1.spines[["top", "right"]].set_visible(False)

# Secondary tier: absolute variance, same width as base.
colors = ["#00B050" if v > 0 else "#C00000" if v < 0 else "#0070C0" for v in abs_var]
ax2.bar(x, abs_var, width=w, color=colors)
ax2.axhline(0, color="#4D4D4D", linewidth=0.8)
ax2.set_ylabel("ΔPL")

# Tertiary tier: relative variance pins.
# Pin body = impact hue; pin head = minuend scenario fill (solid dark for AC).
pin_colors = ["#00B050" if v > 0 else "#C00000" if v < 0 else "#0070C0" for v in rel_var]
ax3.bar(x, rel_var, width=0.10, color=pin_colors)
ax3.scatter(x, rel_var, marker="s", s=18, color="#4D4D4D", zorder=3)
ax3.axhline(0, color="#4D4D4D", linewidth=0.8)
ax3.set_ylabel("ΔPL%")
ax3.set_xticks(x, months)
for xi, v in zip(x, rel_var):
    if np.isnan(v):
        ax3.annotate("N/A", (xi, 0), ha="center", va="bottom", fontsize=7)

for ax in (ax1, ax2, ax3):
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(length=0)

fig.savefig("sales-three-tier.pdf", bbox_inches="tight")
```

### matplotlib: outline and hatch

```python
ax.bar(x, plan, width=0.66, facecolor="none",
       edgecolor="#4D4D4D", linewidth=1.2, label="PL")
ax.bar(x, forecast, width=0.66, facecolor="white",
       edgecolor="#4D4D4D", linewidth=1.2, hatch="///", label="FC")
```

### matplotlib: waterfall bridge

```python
labels = ["PL", "Volume", "Price", "Mix", "AC"]
values = [134.6, -4.8, 1.1, -2.5, 128.4]
# A negative contribution starts at the prior total and runs down to the new total.
bottoms = [0, 134.6, 129.8, 130.9, 0]
colors = ["#FFFFFF", "#C00000", "#00B050", "#C00000", "#4D4D4D"]
edges = ["#4D4D4D", "#C00000", "#00B050", "#C00000", "#4D4D4D"]
ax.bar(labels, values, bottom=bottoms, width=0.66,
       color=colors, edgecolor=edges, linewidth=1.2)
ax.axhline(0, color="#4D4D4D", linewidth=0.8)
```

### plotly: outlined and hatched bars

```python
import plotly.graph_objects as go

fig = go.Figure()
fig.add_bar(
    x=months, y=pl, name="PL",
    marker=dict(color="rgba(0,0,0,0)", line=dict(color="#4D4D4D", width=1.2))
)
fig.add_bar(
    x=months, y=forecast, name="FC",
    marker=dict(
        pattern=dict(shape="/", fgcolor="#4D4D4D", bgcolor="white"),
        line=dict(color="#4D4D4D", width=1.2)
    )
)
fig.update_layout(barmode="group", bargap=0.34)
fig.update_yaxes(rangemode="tozero", title="EUR m")
fig.show()
```

### plotly: built-in waterfall (verify IBCS fit)

```python
import plotly.graph_objects as go

labels = ["PL", "Volume", "Price", "Mix", "AC"]
measure = ["absolute", "relative", "relative", "relative", "total"]
values = [134.6, -4.8, 1.1, -2.5, 128.4]
fig = go.Figure(go.Waterfall(
    x=labels, measure=measure, y=values,
    connector={"line": {"color": "#808080"}},
    increasing={"marker": {"color": "#00B050"}},
    decreasing={"marker": {"color": "#C00000"}},
    totals={"marker": {"color": "#4D4D4D"}},
))
fig.update_yaxes(rangemode="tozero", title="EUR m")
fig.show()
```

### Small multiples

```python
fig, axes = plt.subplots(2, 3, figsize=(14, 6), sharex=True, sharey=True)
for ax, region in zip(axes.flat, regions):
    ax.bar(x, ac[region], width=0.66, color="#4D4D4D")
    ax.bar(x, pl[region], width=0.66, facecolor="none", edgecolor="#4D4D4D")
    ax.set_ylim(0, vmax)
    ax.set_title(region, loc="left")
```

**Version note:** the snippets are illustrative. Check the installed matplotlib/plotly version, the renderer, and the export format. A snippet that works in a notebook may render differently in PDF or PNG.

## Accessibility

- Do not rely on green/red alone; keep signs, labels, and position as redundant cues.
- Test the grayscale version and a color-vision simulation.
- Keep text contrast high; avoid light gray labels on white.
- Use a minimum font size that remains legible in the final print size.
- Add alt text or a data table for non-visual access.
- Avoid animation and interaction-only information for static reports.

## Verification checklist

- [ ] Every value axis starts at zero unless the indexed-data exception applies.
- [ ] Absolute bars/columns use 2/3 category width; relative bars/pins use 1/3 or thinner.
- [ ] AC, PY, PL/BU, and FC are visually distinct (solid dark, solid light, outlined, outlined + hatched).
- [ ] Variance signs, labels, and colors match UN 4.1.
- [ ] Negative denominators show `N/A`, not a computed percentage.
- [ ] Small multiples share type and scale.
- [ ] The page survives grayscale and color-vision checks.
- [ ] The exported PDF/PNG matches the on-screen version.
- [ ] Labels and legends do not overlap or clip.
