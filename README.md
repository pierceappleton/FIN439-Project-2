# Project 2: Meridian Foundation Allocation Tool

## Result without running anything

[output/baseline-output.md](output/baseline-output.md) holds the executed baselines, mandate verdicts and stress run. Decision memo: [docs/decision-memo.md](docs/decision-memo.md). Validation record: [docs/validation-record.md](docs/validation-record.md).

## Run it

Windows PowerShell, Python 3.12 or later. Clone into any folder you can write to (your home folder works; `cd $HOME\Desktop` fails if your Desktop is inside OneDrive). The repo is private, so sign in to GitHub first.

```powershell
cd $HOME
git clone https://github.com/pierceappleton/FIN439-Project-2.git
cd FIN439-Project-2
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python run_baseline.py
.\.venv\Scripts\python tests/verify.py
.\.venv\Scripts\python -m streamlit run app.py
```

Expected: the constrained mix is 60 / 0 / 0 / 40 (BIL / IEF / LQD / VT) and passes the mandate, `verify.py` prints `All checks passed.`, and the app opens at http://localhost:8501.

`run_baseline.py` prints the result and rewrites `output/baseline-output.md`. The Streamlit app lets you move the objective, reserve minimum, cost allowance, 36-month window and each return estimate, and shows a PASS or FAIL per mandate rule.

## Files

| File | Role |
|---|---|
| `portfolio.py` | Risk engine from Labs 14 and 15: estimates, covariance, grid search |
| `analysis.py` | Baselines, per-rule mandate verdict, stress run, stop condition |
| `app.py` | Streamlit app |
| `run_baseline.py` | One command that produces the visible output |
| `data/prices.csv` | 60 monthly adjusted prices (BIL, IEF, LQD, VT), Oct 2021 to Sep 2026, Yahoo download 2026-10-20; provenance in `data/prices-sources.json` |
| `tests/verify.py` | Checks the saved baseline numbers still reproduce |
| `docs/` | Memo, validation record, cold-run notes, data card |

## Mandate (from Lab 13)

Fictional education foundation, $100M, seven-year horizon, annual rebalancing, CPI + 4% net over rolling five years (modeled as 6.5% nominal return, CPI 2.5% being an estimate). Long-only and fully invested, at least 3% in BIL or IEF, 90% liquid within five days. The calendar-year loss limit is undefined and requires CIO clarification, so it is never marked pass.

## Known gaps

See the TODO list in [docs/validation-record.md](docs/validation-record.md).
