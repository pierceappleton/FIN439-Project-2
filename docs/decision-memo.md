# Decision Memo: Meridian Foundation

AI use: Claude assisted with code and drafting; the analysis and decision are mine. Education, not investment advice.

## Decision line (draft, rewrite in your own words)

**Pilot** 60% BIL / 40% VT as a starting allocation (range roughly 50 to 70% BIL), **reverse** if a forward-looking return estimate for VT cannot be supported independently of this sample, or if the client defines a loss limit this mix breaches.

## Evidence (from [output/baseline-output.md](../output/baseline-output.md))

| Portfolio | Weights BIL/IEF/LQD/VT | Return | Volatility | Mandate |
|---|---|---:|---:|---|
| Equal weight | 25/25/25/25 | 3.01% | 7.55% | Fail: return |
| Inverse volatility | 87/6/4/3 | 3.37% | 1.37% | Fail: return |
| Constrained min-vol | 60/0/0/40 | 6.61% | 6.05% | Pass |

Prices Oct 2021 to Sep 2026 (59 monthly returns), objective 6.5%, reserve minimum 3%.

## Why the decision is fragile

- Last-36-month window moves the mix to 85/0/0/15, a 25-point shift, which trips the stop condition.
- A 0.5% annual cost drag moves 10 points into VT; a 1-point VT estimate change moves 5 points.
- The 6.61% return is an arithmetic historical estimate (VT 11.05% annualized) over a window that includes a strong equity run, not a forecast.

## Triggers to monitor

TODO: name the monitors (VT estimate vs. independent forecast, realized net return vs. CPI + 4% over rolling five years, reserve share, cost allowance) and the reversal trigger.

## Open items

Calendar-year loss limit requires CIO clarification. Turnover and costs need a real allowance. Point-in-time signal still to add (see [data card](data-card.md)).
