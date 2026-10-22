# Benchmark Summary

Development evaluation of the `ibcs-standards` skill for closed-book use. These results are not a certification and do not guarantee correctness on every reporting task.

## Method

- **Baseline:** five general subagents received only the task prompt. They had no access to the skill or the source PDF.
- **With skill:** five fresh general subagents received the same prompts and could read only `.opencode/skills/ibcs-standards/`. They were forbidden to read the PDF, design spec, plan, or evaluation workspace.
- **Grading:** each answer was checked against task-specific assertions for rule IDs, notation, signs, colors, widths, layout, and tool limitations.
- **Current run:** iteration 3, after the final consistency fixes. Five tasks, one run per configuration.

## Results

| Task | Baseline | With skill | Current |
|---|---:|---:|---:|
| 0 — Rule retrieval | 4/10 (40%) | 10/10 (100%) | **7/10 (70%)** |
| 1 — Page design | 4/9 (44%) | 8/9 (89%) | **9/9 (100%)** |
| 2 — Audit | 4/10 (40%) | 10/10 (100%) | **10/10 (100%)** |
| 3 — Encoding | 2/8 (25%) | 8/8 (100%) | **8/8 (100%)** |
| 4 — Tool implementation | 6/8 (75%) | 8/8 (100%) | **8/8 (100%)** |

**Aggregate: 94.0% with skill vs 44.9% baseline, delta +0.49.**

## Notes

- Task 1 now scores 9/9; the earlier shared-legend omission is resolved.
- Task 0’s current answer was concise and omitted percentage points, `N/A`, and the full grayscale fallback triad. The skill contains those details in `SKILL.md` and `semantic-notation.md`; this is an answer-completeness variance, not a missing rule.
- No invented rule IDs appeared in the current run.
- The structural harness passes: 35 top-level rules, 105 sub-rules, 105 mapped IDs, exact counts, no encoding corruption.

## Reproduce

From the repository root:

```powershell
python scripts/verify_skill.py
```

The full evaluation workspace is intentionally excluded from this clean repository.
