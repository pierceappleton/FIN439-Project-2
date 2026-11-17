# Changed-input test: annual cost allowance 1.50%

Settings: objective 8.50%, reserve minimum 1.00%, cost allowance 1.50% per year, last 36 monthly returns (2023-09-01 to 2026-09-01). Education, not investment advice.

Weights order: BIL / IEF / LQD / VT (%).

| Portfolio | Weights | Net return | Volatility | Mandate |
|---|---|---:|---:|---|
| Equal weight | 25.0 / 25.0 / 25.0 / 25.0 | 6.63% | 5.88% | FAIL: Net return >= 8.5% |
| Inverse volatility | 92.8 / 3.0 / 2.5 / 1.7 | 3.11% | 0.61% | FAIL: Net return >= 8.5% |
| Constrained min-vol | 60.0 / 0.0 / 0.0 / 40.0 | 9.22% | 4.70% | PASS |

Stress table (8.5% objective, 1% reserve; cost rows are the app's fixed 0.25%/0.50% cases):

| Case | Weights | Shift (pts) | Stop? |
|---|---|---:|---|
| Window: last 36 months | 70 / 0 / 0 / 30 | 40 | STOP |
| Estimate: BIL return -1% | 30 / 0 / 0 / 70 | 0 | no |
| Estimate: BIL return +1% | 35 / 0 / 0 / 65 | 5 | no |
| Estimate: IEF return -1% | 30 / 0 / 0 / 70 | 0 | no |
| Estimate: IEF return +1% | 30 / 0 / 0 / 70 | 0 | no |
| Estimate: LQD return -1% | 30 / 0 / 0 / 70 | 0 | no |
| Estimate: LQD return +1% | 30 / 0 / 0 / 70 | 0 | no |
| Estimate: VT return -1% | 20 / 0 / 0 / 80 | 10 | no |
| Estimate: VT return +1% | 40 / 0 / 0 / 60 | 10 | no |
| Costs: 0.25% annual drag | 30 / 0 / 0 / 70 | 0 | no |
| Costs: 0.50% annual drag | 25 / 0 / 0 / 75 | 5 | no |
| Constraint: reserve minimum 10% | 30 / 0 / 0 / 70 | 0 | no |
| Constraint: objective 7.0% | 50 / 0 / 0 / 50 | 20 | no |
