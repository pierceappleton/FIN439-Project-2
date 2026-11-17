"""One command that produces the visible result: python run_baseline.py
Writes output/baseline-output.md (readable on GitHub without running anything)."""
from datetime import date
from pathlib import Path

import analysis as a

NAMES = ("BIL", "IEF", "LQD", "VT")


def fmt_w(w):
    return " / ".join(f"{x * 100:.0f}" for x in w)


def main():
    sleeves, corr, meta = a.load()
    res, _ = a.portfolios(sleeves, corr)
    out = ["# Baseline output", "",
           f"Education, not investment advice. Prices: {meta['start']} to {meta['end']} "
           f"({meta['returns']} monthly returns). Objective {a.OBJECTIVE:.1%}, "
           f"reserve minimum {a.RESERVE_MIN:.0%}. Run date {date.today()}.", "",
           f"Weights order: {' / '.join(NAMES)} (%).", "",
           "| Portfolio | Weights | Return | Volatility | Mandate |", "|---|---|---:|---:|---|"]
    for name, r in res.items():
        failed = [k for k, ok in r["rules"] if not ok]
        out.append(f"| {name} | {fmt_w(r['weights'])} | {r['ret']:.2%} | {r['vol']:.2%} | "
                   f"{'PASS' if r['passes'] else 'FAIL: ' + '; '.join(failed)} |")
    out += ["", "Calendar-year loss limit (S9): requires CIO clarification, never a pass.", "",
            "## Stress run (constrained min-vol, one change at a time)", "",
            "| Case | Weights | Shift (pts) | Stop? |", "|---|---|---:|---|"]
    base, rows = a.stress()
    out.append(f"| Base (all months) | {fmt_w(base['weights'])} | 0 | no |")
    for r in rows:
        w = fmt_w(r["result"]["weights"]) if r["result"] else "infeasible"
        s = "n/a" if r["shift"] is None else f"{r['shift']:.0f}"
        out.append(f"| {r['case']} | {w} | {s} | {'STOP' if r['stop'] else 'no'} |")
    out += ["", f"Stop condition: no feasible mix, or any weight moves more than "
                f"{a.STOP_SHIFT_PTS:.0f} points under one change."]
    text = "\n".join(out) + "\n"
    (Path(__file__).parent / "output" / "baseline-output.md").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
