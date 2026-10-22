# Source and License

## Full citation

*International Business Communication Standards (IBCS) Version 2.0*. Rolf Hichert and Jürgen Faisst. IBCS Media, Hilden, 2026. ISBN 978-3-9821414-4-2. 169 pages. Version date: 2026-07-02. Licensed under CC BY-SA 4.0.

The source covers 35 top-level rules and 105 sub-rules across SIMPLIFY, UNIFY, CHECK, SAY, STRUCTURE, EXPRESS, and CONDENSE.

## Attribution and derivative-work notice

This skill is an independent derivative summary based on IBCS v2.0. It is not a verbatim reproduction, not a full-text mirror, and not a substitute for the official source for legal or certification purposes.

**Changes:**

- condensed and reorganized the standards for closed-book agent use;
- rewrote rule explanations in original language;
- added implementation guidance for Python, Power BI, Excel, and HTML/JS;
- added worked examples, a page-spec template, an audit checklist, and a completeness map;
- did not reproduce figures;
- did not reproduce ISO 24896 text.

This work is licensed under CC BY-SA 4.0. See `LICENSE`.

**No endorsement:** This skill is not affiliated with, endorsed by, or certified by the IBCS Association, the authors, or ISO. “IBCS” refers to the standard; no trademark claim is made.

## ISO caveat

IBCS v2.0 aligns its notation with ISO 24896 “Notation for business reporting.” ISO 24896 defines normative requirements; IBCS provides explanations, design rules, examples, and extensions. This skill summarizes the IBCS material and does **not** reproduce the ISO standard. It does not provide legal advice, certification, or a compliance guarantee.

Where the source defers a topic, the skill says **“not specified in v2.0”** and does not invent a normative rule. Deferred topics include:

- comprehensive measure-type notation beyond absolute/relative;
- visualization of adjustment analyses;
- visualization of selecting in structure analyses;
- specific notation for area charts;
- specific notation for boxplot/range charts;
- specific notation for charts with two value axes;
- additional scaling visualizations beyond scale bands.

## Source page map

| Section | Pages |
|---|---|
| Introduction and definitions | iii–xiv |
| NOTATION | 15 |
| SIMPLIFY | 16–23 |
| UNIFY | 24–67 |
| CHECK | 68–75 |
| COMPOSITION | 77 |
| SAY | 78–86 |
| STRUCTURE | 87–95 |
| EXPRESS | 96–142 |
| CONDENSE | 143–156 |
| Table of figures | 157–161 |
| Terms and references | 163–166 |
| Further resources | 167–169 |

## Verification instructions

The verification harness is a **project-level** tool. It lives at `scripts/verify_skill.py` in the project root, not inside the skill folder; the closed-book content does not depend on it.

1. Run the structural harness from the project root:

   ```powershell
   python scripts/verify_skill.py
   ```

   Expected: `PASS`, with 105 mapped IDs, all rule entries present, all router targets existing, and valid JSON.

2. Count headings per rule file:

   - SI 14
   - UN 18
   - CH 15
   - SA 14
   - ST 14
   - EX 14
   - CO 16

3. Spot-check random rules against the source PDF: title, Requirement, exception, and source page.

4. Confirm that every deferred topic is labeled “not specified in v2.0” and that no local convention is presented as normative.

5. Confirm that tool guides label version-dependent snippets and do not claim native support that does not exist.

## Changelog

| Date | Version | Change |
|---|---|---|
| 2026-10-20 | 1.0 | Initial closed-book skill: framework, glossary, 105 rule entries, semantic notation, chart/table catalog, composition playbook, five worked examples, audit checklist, completeness map, four implementation guides, templates, license, and verification harness. |
| 2026-10-20 | 1.1 | Closed-book evaluation refactor: valid-ID range table, mandatory source-page citations, no-invented-quantification rule, shared-legend reminder; consistency fixes for zero-baseline guidance, title conjunction, cross tables, variance fill/hue, Example 1 timing, Example 2 arithmetic/table, Example 5 North-level bridge, Python geometry/N/A, and Power BI denominator guard; 20-rule spot check and four fresh-context reviews. |
