# Baseline output

Education, not investment advice. Prices: 2021-10-01 to 2026-09-01 (59 monthly returns). Objective 6.5%, reserve minimum 3%. Run date 2026-11-17.

Weights order: BIL / IEF / LQD / VT (%).

| Portfolio | Weights | Return | Volatility | Mandate |
|---|---|---:|---:|---|
| Equal weight | 25 / 25 / 25 / 25 | 3.01% | 7.55% | FAIL: Net return >= 6.5% |
| Inverse volatility | 87 / 6 / 4 / 3 | 3.37% | 1.37% | FAIL: Net return >= 6.5% |
| Constrained min-vol | 60 / 0 / 0 / 40 | 6.61% | 6.05% | PASS |

Calendar-year loss limit (S9): requires CIO clarification, never a pass.

## Stress run (constrained min-vol, one change at a time)

| Case | Weights | Shift (pts) | Stop? |
|---|---|---:|---|
| Base (all months) | 60 / 0 / 0 / 40 | 0 | no |
| Window: last 36 months | 85 / 0 / 0 / 15 | 25 | STOP |
| Estimate: BIL return -1% | 50 / 0 / 0 / 50 | 10 | no |
| Estimate: BIL return +1% | 70 / 0 / 0 / 30 | 10 | no |
| Estimate: IEF return -1% | 60 / 0 / 0 / 40 | 0 | no |
| Estimate: IEF return +1% | 60 / 0 / 0 / 40 | 0 | no |
| Estimate: LQD return -1% | 60 / 0 / 0 / 40 | 0 | no |
| Estimate: LQD return +1% | 60 / 0 / 0 / 40 | 0 | no |
| Estimate: VT return -1% | 55 / 0 / 0 / 45 | 5 | no |
| Estimate: VT return +1% | 65 / 0 / 0 / 35 | 5 | no |
| Costs: 0.25% annual drag | 55 / 0 / 0 / 45 | 5 | no |
| Costs: 0.50% annual drag | 50 / 0 / 0 / 50 | 10 | no |
| Constraint: reserve minimum 10% | 60 / 0 / 0 / 40 | 0 | no |
| Constraint: objective 7.0% | 50 / 0 / 0 / 50 | 10 | no |

Stop condition: no feasible mix, or any weight moves more than 20 points under one change.
