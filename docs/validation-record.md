# Validation Record

## Baseline and mandate check

Reproduce with `python run_baseline.py`; saved result in [output/baseline-output.md](../output/baseline-output.md). Checks: `python tests/verify.py`.

## Stress run

Window, estimates (each asset +/-1 point), costs (0.25% and 0.50%) and constraints are in the same output file. Stop condition: infeasible, or any weight moves more than 20 points under one change.

## Locked Changed-Input Record

### Prediction (human-written, committed unchanged before the rerun)

**Changed-Input Prediction Commitment:**

* Scenario Tested: Increasing the annual cost allowance from 1.00% to 1.50% per year, holding the 8.50% objective, 1.00% reserve minimum, last-36-month window, and asset return estimates unchanged.
* Expected Impact on Allocation: Allocation will remain unchanged because the annual cost allowance applies a uniform annual return deduction across all asset classes without introducing separate trading transaction costs or altering the relative covariance and return structure that drives the optimizer's weights.
* Expected Impact on Performance & Mandate Verdicts: Estimated net return will decrease (referring to the new allocation selected by the optimizer), while volatility will stay roughly unchanged due to fixed underlying asset proportions and risk parameters.
* Recommendation Verdict: Recommendation will remain to reject live allocation because this cost sensitivity test measures fee drag rather than resolving the core governance gaps, missing mandate rules (like the undefined calendar-year loss limit), lack of CIO sign-off, or the previously triggered stress stop.

Commit hash of this prediction: recorded in the table below after the commit.

| Field | Entry |
|---|---|
| Timestamp / commit | Prediction committed 2026-11-17 18:20 -05:00 in the commit titled `Record annual cost prediction before rerun`, before the rerun |
| Load-bearing input | Annual cost allowance |
| Old value -> new value, with units | 1.00% per year -> 1.50% per year (objective 8.50%, reserve minimum 1.00%, last-36-month window held fixed) |
| Expected direction of decision numbers | See the prediction above: allocation unchanged, net return down, volatility roughly unchanged |
| Expected effect on the decision | Recommendation stays reject |

## After the run

The test was executed from the committed engine. Same code as the app (`analysis.portfolios` with `last_36=True`, objective 8.5%, reserve 1%). Only the cost allowance changed.

- Before output: [output/changed-input-before-cost-1.00.md](../output/changed-input-before-cost-1.00.md)
- After output: [output/changed-input-after-cost-1.50.md](../output/changed-input-after-cost-1.50.md)

| Constrained min-vol | Before (1.00%) | After (1.50%) |
|---|---|---|
| Weights BIL / IEF / LQD / VT (%) | 65 / 0 / 0 / 35 | 60 / 0 / 0 / 40 |
| Net return | 8.92% | 9.22% |
| Volatility | 4.12% | 4.70% |
| Mandate | PASS | PASS |

Equal weight (7.13% -> 6.63%) and inverse volatility (3.61% -> 3.11%) still FAIL on return. The before run matches my earlier app screenshot.

| Field | Entry |
|---|---|
| Decision changed? | No. The recommendation stays reject live allocation. The constrained mix still passes the return and reserve rules, and the calendar-year loss limit and the 36-month stop trigger are untouched. |
| Why prediction matched or not | The reject verdict matched. The allocation, net return and volatility predictions were wrong. Allocation moved 5 points from BIL into VT, net return rose from 8.92% to 9.22%, and volatility rose from 4.12% to 4.70%. |

**Why.** The cost allowance is not only a uniform deduction that leaves the choice unchanged. The objective is a net-return constraint, so subtracting 0.5 points from every asset's return makes the old 65/35 mix fall short (65/35 would net about 8.43%, below 8.5%). The optimizer then had to move to the next 5-point grid step, 60/40, which has more VT, so it clears the objective with room to spare (9.22%) and carries more risk. The net return rose because of the 5-point grid and the binding constraint, not because costs help. My prediction treated the allocation as independent of the cost input and missed that the constraint binds.

## Unresolved items (TODO)

- Point-in-time signal and [data card](data-card.md)
- Second-baseline rationale (inverse volatility used; confirm it is the one you want)
- Loss-limit definition from the CIO
- Videos 1 to 3 and transcripts
