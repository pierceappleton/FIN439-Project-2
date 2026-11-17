# Validation and AI Use

AI use: Claude assisted with code and drafting; the analysis and decision are mine. Education, not investment advice.

## Baseline and mandate check

Reproduce with `python run_baseline.py`; saved result in [output/baseline-output.md](../output/baseline-output.md). Checks: `python tests/verify.py`.

## Stress run

Window, estimates (each asset +/-1 point), costs (0.25% and 0.50%) and constraints are in the same output file. Stop condition: infeasible, or any weight moves more than 20 points under one change.

## Locked Changed-Input Record

Write this yourself, **before AI help and before the run**, then commit and push. Commit hash goes in the record.

| Field | Entry |
|---|---|
| Timestamp / commit | TODO |
| Load-bearing input | TODO (example: VT return estimate, or cost allowance) |
| Old value -> new value, with units | TODO (example: 11.05% per year -> 9.05% per year) |
| Expected direction of decision numbers | TODO |
| Expected effect on the decision | TODO |

After the run (AI closed):

| Field | Entry |
|---|---|
| Before output / after output | TODO |
| Decision changed? | TODO |
| Why prediction matched or not | TODO |

## AI output I checked

TODO: one AI output, the check I did, and whether I accepted, qualified, corrected or rejected it.

## Unresolved items (TODO)

- Point-in-time signal and [data card](data-card.md)
- Second-baseline rationale (inverse volatility used; confirm it is the one you want)
- Loss-limit definition from the CIO
- Videos 1 to 3 and transcripts
