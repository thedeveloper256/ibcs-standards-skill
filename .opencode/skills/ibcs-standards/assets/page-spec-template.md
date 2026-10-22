# Page Specification Template

Use this template before building a page. It is the output contract for a design task and the review sheet for an audit.

## Decision

- **Decision or action requested:**
- **Decision owner:**
- **Deadline or cadence:**
- **What happens if no decision is made:**

## Audience

- **Primary audience:**
- **Secondary audience:**
- **Knowledge level:**
- **Likely objections or disagreements:**
- **Cultural or sensitivity considerations:**

## Key message

Write one complete sentence:

`<Subject> <verb> <magnitude> <comparison> <time>, <consequence>.`

**Key message:**

**Message type:** detection / explanation / suggestion

**Evidence required:**

## Title

- **Line 1 — who (reporting unit / filters):**
- **Line 2 — what (measure(s), unit, analytical annotation):**
- **Line 3 — when (period(s), scenario(s), variance(s)):**

The title is descriptive. Do not put the conclusion in the title.

## Visual specification

- **Analytical question:**
- **Chart or table family:**
- **Why this family fits:**
- **Categories / dimensions:**
- **Series / scenarios:**
- **Axis orientation and ranges:**
- **Tiers, overlays, or small multiples:**
- **Data labels and legends:**
- **Sorting / ranking / selection:**
- **Layout and size:**

## Semantic encoding

- **AC fill:**
- **PY fill:**
- **PL/BU fill:**
- **FC fill:**
- **Absolute measure width/line weight:**
- **Relative measure width/line weight:**
- **Variance notation (`ΔPL`, `ΔPY`, `ΔPL%`, `ΔPY%`):**
- **Variance colors and grayscale fallback:**
- **Percentage points / `N/A` handling:**
- **Time markers (YTD/YTG/moving/indexing):**
- **Structure markers (averaging/ranking/selecting/indexing/normalizing):**
- **Other markers (scale band, outlier, trend arrow, annotation reference):**

## Text elements

- **Key message placement:**
- **Subtitles:**
- **Annotations (with references):**
- **Footnotes and sources:**
- **Definitions and plan version:**

## Integrity checks

- [ ] Value axes start at zero unless the indexed-data exception applies.
- [ ] No clipped or broken components.
- [ ] Same units use the same scale, or a scaling marker makes the difference explicit.
- [ ] Area/volume encodings are proportional, or replaced by linear encodings.
- [ ] Map colors are used only for area-related data.
- [ ] Ordered classes have equal widths.
- [ ] Inflation/currency adjustments are shown or explained where material.
- [ ] Scenario fills and variance signs/colors match the notation.
- [ ] Negative denominators show `N/A`.
- [ ] The page survives grayscale and color-vision checks.
- [ ] Data reconciles to the source.
- [ ] Titles are descriptive; the key message is separate.
- [ ] Sources and plan version are visible.
- [ ] The page is legible at its final size.

## Open trade-offs

- **What is intentionally omitted:**
- **What is approximated:**
- **Known deferred notation (area/boxplot/two-value-axis/selecting/adjustment):**
- **Residual risk:**
- **Follow-up data or design work:**
