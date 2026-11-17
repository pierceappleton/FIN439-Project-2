# Validation and AI Use

AI use: Claude assisted with code and drafting; the analysis and decision are mine. Education, not investment advice.

## Baseline and mandate check

Reproduce with `python run_baseline.py`; saved result in [output/baseline-output.md](../output/baseline-output.md). Checks: `python tests/verify.py`.

## Stress run

Window, estimates (each asset +/-1 point), costs (0.25% and 0.50%) and constraints are in the same output file. Stop condition: infeasible, or any weight moves more than 20 points under one change.

## Locked Changed-Input Record

Write this yourself, **before AI help and before the run**, then commit and push. Commit hash goes in the record.

### Prediction (human-written, committed unchanged before the rerun)

**Changed-Input Prediction Commitment:**

* Scenario Tested: Increasing the annual cost allowance from 1.00% to 1.50% per year, holding the 8.50% objective, 1.00% reserve minimum, last-36-month window, and asset return estimates unchanged.
* Expected Impact on Allocation: Allocation will remain unchanged because the annual cost allowance applies a uniform annual return deduction across all asset classes without introducing separate trading transaction costs or altering the relative covariance and return structure that drives the optimizer's weights.
* Expected Impact on Performance & Mandate Verdicts: Estimated net return will decrease (referring to the new allocation selected by the optimizer), while volatility will stay roughly unchanged due to fixed underlying asset proportions and risk parameters.
* Recommendation Verdict: Recommendation will remain to reject live allocation because this cost sensitivity test measures fee drag rather than resolving the core governance gaps, missing mandate rules (like the undefined calendar-year loss limit), lack of CIO sign-off, or the previously triggered stress stop.

Commit hash of this prediction: recorded in the table below after the commit.

| Field | Entry |
|---|---|
| Timestamp / commit | See the commit hash below (prediction committed before the rerun) |
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
