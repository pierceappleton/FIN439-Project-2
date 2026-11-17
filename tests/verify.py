"""Run from project-2: python tests/verify.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import analysis as a

sleeves, corr, meta = a.load()
res, found = a.portfolios(sleeves, corr)
assert meta["prices"] == 60 and meta["returns"] == 59, meta
assert [round(w * 100) for w in found["weights"]] == [60, 0, 0, 40]
assert res["Constrained min-vol"]["passes"]
assert not res["Equal weight"]["passes"] and not res["Inverse volatility"]["passes"]
base, rows = a.stress()
last = next(r for r in rows if r["case"].startswith("Window"))
assert round(last["shift"]) == 25 and last["stop"]
print("All checks passed.")
