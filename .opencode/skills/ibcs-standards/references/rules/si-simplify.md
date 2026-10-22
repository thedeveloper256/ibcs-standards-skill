# SIMPLIFY — Avoid Clutter

SIMPLIFY covers all aspects of avoiding clutter in reporting. Avoiding clutter means removing components and characteristics that are redundant, distracting, or merely decorative. Erasing redundant data-ink and non-data-ink with reason maximizes the share of data-ink (the data-ink ratio).

Many SIMPLIFY rules become obsolete when a report is built with the IBCS notation in UNIFY. They remain necessary for revising existing reporting.

**Source:** IBCS v2.0, pages 16–23.

## SI 1 — Avoid unnecessary elements

Completely avoid elements, such as pictures, backgrounds, and logos, that do not contribute to the comprehension of reporting.

### SI 1.1 — Avoid cluttered layouts

**Requirement.** Avoid layout elements that lack meaning and merely conform to corporate design or personal taste.

**Why.** They consume space and attention without contributing to comprehension.

**Apply.** Strip decorative panels, ornamental shapes, background images, and logos that do not carry analytical meaning. Keep only elements that help the reader understand the data.

**Exceptions / limits.** None stated in v2.0.

**Audit.** Does every element on the page contribute to understanding? If not, remove it.

**See also.** SI 1.2, SI 2.1.

**Source.** p. 16.

### SI 1.2 — Avoid colored or filled backgrounds

**Requirement.** Present numbers and labels in black on a white or plain background. Avoid background colors and patterns behind text and data.

**Why.** Any background color or pattern reduces contrast and makes text harder to read.

**Apply.** Use a plain background for the page and for chart/table areas. If a fill is needed to group content, keep it light and keep text off the fill.

**Exceptions / limits.** None stated in v2.0.

**Audit.** Are numbers and labels placed on a plain, high-contrast background?

**See also.** SI 2.2.

**Source.** p. 16–17.

### SI 1.3 — Avoid animation and transition effects

**Requirement.** Avoid animated slides and transition effects when the animation has no meaning and does not support the message.

**Why.** Meaningless motion distracts and confuses the audience.

**Apply.** Keep visuals static. If animation is used at all, use it only to reveal a meaningful change or sequence and remove it when the page is printed or read asynchronously.

**Exceptions / limits.** None stated in v2.0.

**Audit.** Does the animation support the message? If not, remove it.

**See also.** CO 4.5.

**Source.** p. 17.

## SI 2 — Avoid decorative styles

Simplify visualizations to facilitate and accelerate comprehension. Whereas SI 1 removes entire layout elements, SI 2 finds the simplest suitable style for visual components.

### SI 2.1 — Avoid frames, shades, and pseudo-3D without meaning

**Requirement.** Avoid frames, shadows, and pseudo-3D effects that convey no meaning.

**Why.** They make comprehension harder and can create a false visual impression.

**Apply.** Use flat, unframed visual components. Do not use bevels, drop shadows, gradients, or 3D perspective unless the effect encodes an analytical dimension.

**Exceptions / limits.** None stated in v2.0.

**Audit.** Does the frame, shade, or 3D effect carry meaning? If not, remove it.

**See also.** CH 3.2.

**Source.** p. 17–18.

### SI 2.2 — Avoid decorative colors

**Requirement.** Use color only to convey analytical meaning, never for decoration.

**Why.** If color is decorative in one place, using it for meaning elsewhere becomes ambiguous.

**Apply.** Start from a neutral base. Reserve hues for scenarios, variances, highlights, and other analytical distinctions, and keep each hue's meaning consistent across the report.

**Exceptions / limits.** None stated in v2.0. Exact color codes are not prescribed; keep them consistent within an organization.

**Audit.** Does every color have a defined analytical meaning?

**See also.** UN 3.2, UN 4.1.

**Source.** p. 18.

### SI 2.3 — Avoid decorative fonts

**Requirement.** Use simple, neutral, legible fonts. Reserve bold, italic, and other styles for semantic distinctions.

**Why.** Decorative fonts reduce readability, slow perception, and distract from content.

**Apply.** Use a straight sans-serif font without ornaments, widely available and legible at small sizes. Avoid serif fonts for chart text, handwritten or playful fonts, display fonts, and fonts with shadows, outlines, or unusual proportions. Use bold for totals or measures and italic for distinctions such as percentage-of rows.

**Exceptions / limits.** Serif fonts may be used for continuous flow text over multiple lines.

**Audit.** Are fonts simple, legible, and used semantically?

**See also.** UN 2.2, EX 1.2.

**Source.** p. 18–19.

## SI 3 — Replace with cleaner layout

Using a cleaner method of visualization decreases the amount of ink necessary to convey a message.

### SI 3.1 — Replace grid lines and value axes with data labels

**Requirement.** Use integrated data labels so that value axes, tick marks, and gridlines become superfluous.

**Why.** Fewer non-data elements reduce clutter and speed reading.

**Apply.** Label the data directly. Keep gridlines only when reference points are missing, when there are many data series or points, or in small charts such as small multiples.

**Exceptions / limits.** Gridlines can be useful in charts with many series/points or in small multiples where labels would be too dense.

**Audit.** Are gridlines or value axes necessary given the data labels?

**See also.** UN 2.3, SI 5.3.

**Source.** p. 19–20.

### SI 3.2 — Avoid vertical lines by right-aligning data

**Requirement.** Omit avoidable table components. Avoid vertical lines by right-aligning numerical values and their column headers.

**Why.** Whitespace and alignment separate columns more cleanly than rules.

**Apply.** Right-align numbers and numeric headers; left-align text; use white gaps or very light lines only where structure demands them.

**Exceptions / limits.** None stated in v2.0.

**Audit.** Are vertical lines necessary, or would alignment and gaps suffice?

**See also.** EX 1.2.

**Source.** p. 20.

## SI 4 — Avoid redundancies

Avoiding redundant terms usually increases legibility. A certain amount of redundancy can help, such as repeating the time period in the chart title and the chart. Unnecessary redundancy impedes comprehension.

### SI 4.1 — Avoid superfluous words

**Requirement.** Omit complementary words such as “sum” and “total” when they add no meaning to the term they accompany.

**Why.** They make text elements harder to read without adding information.

**Apply.** Write “Europe,” not “Sum of Europe”; write “Sales,” not “Total sales,” when the context already makes the aggregation clear.

**Exceptions / limits.** Keep a word if it distinguishes a subtotal from a different concept, such as “Total assets” versus “Current assets.”

**Audit.** Does the word add information beyond the term itself?

**See also.** SI 4.2, SI 4.3.

**Source.** p. 20–21.

### SI 4.2 — Avoid obvious terms

**Requirement.** Omit terms that name something already shown, such as “chart analysis,” “development,” “comment,” “table,” “statistics,” “report,” “visualization,” “structure,” or “trend.”

**Why.** They restate the obvious and slow reading.

**Apply.** Remove the term. Let the visual and the title carry the meaning.

**Exceptions / limits.** None stated in v2.0.

**Audit.** Does the term tell the reader something not already visible or stated?

**See also.** SI 4.1.

**Source.** p. 21.

### SI 4.3 — Avoid repeated words

**Requirement.** Avoid repeating words in legends, category labels, and row headers, such as “division” in “division A, division B” or “2026” in “Q1 2026, Q2 2026.”

**Why.** Repeating a word in every label adds clutter without adding distinction.

**Apply.** Put the shared word in the header or axis title and list only the distinguishing parts: “Division” over “A, B, C”; “2026” over “Q1, Q2, Q3, Q4.”

**Exceptions / limits.** Repeat a word when omitting it would make a label ambiguous.

**Audit.** Is any word repeated unnecessarily across labels?

**See also.** UN 2.3.

**Source.** p. 21.

## SI 5 — Avoid distracting details

In addition to avoiding noise and redundancy, omit nonessential, distracting details.

### SI 5.1 — Avoid labels for small values

**Requirement.** Avoid data labels for small values unless the discussion explicitly addresses them. If labeling is necessary, use leader lines.

**Why.** Small labels are hard to position and rarely contribute to the key message.

**Apply.** Label only values that matter to the message. If a small value must be labeled, connect the label to the component with a leader line.

**Exceptions / limits.** Label a small value when it is the subject of the message or an annotation.

**Audit.** Does the small-value label help the message?

**See also.** SI 5.3, UN 2.3.

**Source.** p. 22.

### SI 5.2 — Avoid long numbers

**Requirement.** Limit numbers to no more than three digits in charts and four digits in tables. Use currency and metric prefixes to shorten them.

**Why.** Long numbers are hard to read, and the extra precision is seldom necessary for the message.

**Apply.** Round to meaningful units; use `k`, `m`, and `b` prefixes consistently; put the unit in the title or column header; use the same precision across a comparison.

**Exceptions / limits.** Tables may need four digits for exact lookup; keep the same format throughout the table.

**Audit.** Are numbers within the digit limit and consistently rounded?

**See also.** UN 1.2.

**Source.** p. 22.

### SI 5.3 — Avoid unnecessary labels

**Requirement.** In charts with many data points, omit data labels for points that are not extrema or otherwise significant, such as the current, first, or last value.

**Why.** Labeling every point creates clutter and hides the pattern.

**Apply.** Label maxima, minima, the current value, the first value, the last value, and values referenced by the key message. Leave the rest unlabeled.

**Exceptions / limits.** Label more points when exact lookup is the purpose of the table or chart.

**Audit.** Are labels limited to significant points?

**See also.** SI 5.1, UN 2.3.

**Source.** p. 22–23.
