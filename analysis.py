"""Project 2 analysis layer: baselines, mandate verdicts, stress run.

Built on portfolio.py (the Lab 14/15 engine). Decimal units throughout.
"""
from pathlib import Path

import portfolio as p

PRICES = Path(__file__).resolve().parent / "data" / "prices.csv"
RESERVE = {"BIL", "IEF"}      # reserve-eligible: cash / Treasuries
OBJECTIVE = 0.065             # CPI 2.5% (modeling estimate) + 4%
RESERVE_MIN = 0.03            # 4 quarterly payouts of $0.75M on $100M
STOP_SHIFT_PTS = 20.0         # stop rule: largest weight shift above this


def load(last_36=False, path=PRICES):
    return p.estimate_from_csv(path, last_36)


def verdict(weights, sleeves, objective=OBJECTIVE, reserve_min=RESERVE_MIN, cost=0.0):
    """Per-rule pass/fail for one weight vector. Returns (rows, all_pass)."""
    ret = p.expected_return(weights, sleeves) - cost
    reserve = sum(w for w, s in zip(weights, sleeves) if s[0] in RESERVE)
    rows = [
        ("Fully invested (sum = 100%)", abs(sum(weights) - 1) < 1e-9),
        ("Long-only (no weight < 0)", min(weights) >= -1e-12),
        (f"Net return >= {objective:.1%}", ret + 1e-12 >= objective),
        (f"Reserve (BIL+IEF) >= {reserve_min:.0%}", reserve + 1e-12 >= reserve_min),
        ("Liquid within 5 days >= 90%", True),  # all four are daily-traded ETFs
    ]
    return rows, all(ok for _, ok in rows)


def portfolios(sleeves, corr, objective=OBJECTIVE, reserve_min=RESERVE_MIN, cost=0.0):
    """Equal weight, inverse volatility (2nd baseline) and the constrained search."""
    net = [(n, r - cost, v) for n, r, v in sleeves]
    cov = p.covariance_matrix(net, corr)
    found = p.search(net, corr, objective, reserve_min, RESERVE)
    out = {"Equal weight": p.equal_weights(net),
           "Inverse volatility": p.inverse_volatility_weights(net)}
    if found:
        out["Constrained min-vol"] = list(found["weights"])
    result = {}
    for name, w in out.items():
        rows, ok = verdict(w, sleeves, objective, reserve_min, cost)
        result[name] = dict(weights=w, ret=p.expected_return(w, net),
                            vol=p.portfolio_volatility(w, cov), rules=rows, passes=ok)
    return result, found


def stress(objective=OBJECTIVE, reserve_min=RESERVE_MIN):
    """Re-run the constrained search under one change at a time."""
    full, fcorr, _ = load(False)
    last, lcorr, _ = load(True)
    base = p.search(full, fcorr, objective, reserve_min, RESERVE)
    cases = [("Window: last 36 months", last, lcorr, objective, reserve_min)]
    for i, (name, r, v) in enumerate(full):
        for d in (-0.01, 0.01):
            s = list(full)
            s[i] = (name, r + d, v)
            cases.append((f"Estimate: {name} return {d:+.0%}", s, fcorr, objective, reserve_min))
    for c in (0.0025, 0.005):
        s = [(n, r - c, v) for n, r, v in full]
        cases.append((f"Costs: {c:.2%} annual drag", s, fcorr, objective, reserve_min))
    cases.append(("Constraint: reserve minimum 10%", full, fcorr, objective, 0.10))
    cases.append(("Constraint: objective 7.0%", full, fcorr, 0.07, reserve_min))
    rows = []
    for label, s, c, obj, rm in cases:
        r = p.search(s, c, obj, rm, RESERVE)
        shift = p.largest_weight_change(base, r)
        stop = r is None or (shift is not None and shift > STOP_SHIFT_PTS)
        rows.append(dict(case=label, result=r, shift=shift, stop=stop))
    return base, rows
