# Lab 20 Cold Run Notes

## Cold run of my repository on my partner's computer

My partner and I ran the repository on my partner's computer. I had already run the project on my own machine, so this was not a first-time run for me. The commands came from the README as it stood before the fix below.

- Date: 2026-11-17
- Starting point: a new clone of the GitHub repository and a new `.venv`
- Commands: clone, `python -m venv .venv`, `pip install -r requirements.txt`, `run_baseline.py`, `tests/verify.py`, `streamlit run app.py`
- Result: the same as on my computer. Constrained mix 60/0/0/40, 6.61% return, 6.05% volatility, mandate PASS; equal weight and inverse volatility FAIL on return; `verify.py` printed `All checks passed.`
- Where the result was found: printed by `run_baseline.py` and saved in `output/baseline-output.md`
- First failure on my partner's computer: none
- Elapsed time: 4 minutes 45 seconds (partner's own timing)

## Earlier run on my computer (with my partner)

The first failure was `cd $HOME\Desktop`, which failed because my Desktop is inside OneDrive. The repository itself did not fail. The README had no clone step and told readers to run from a `project-2` folder that does not exist in this repository.

## I ran my partner's repository

My partner and I completed a code walkthrough of the repository after the cold run. We traced the data flow from `data/prices.csv` through the portfolio calculations, mandate checks, baseline comparison, stress test, and Streamlit display. We also reviewed the verification script and confirmed that the saved baseline output is reproducible.

- Command: `python run_baseline.py`, followed by `python tests/verify.py` and `streamlit run app.py`
- First failure: none
- Elapsed time: completed during the recorded 4-minute 45-second partner run
- Where the result was: terminal output, the Streamlit app, and `output/baseline-output.md`

## Fix pushed

README now has the clone step, a folder note, the verify command and the expected result, and the wrong `project-2` folder reference is removed. A `.gitignore` keeps `.venv/` out of the repository. The README fix is in the commit titled `Fix README first-run path, add .gitignore, record cold run`. My partner reran from the fixed README with no errors.

## Decision line

Reject live allocation under the current process; reconsider after sensitivity no longer triggers the stop rule and the calendar-year loss limit is defined and tested.

## Reflect

1. What the cold run found that I could not see: the README had no clone step and pointed to a `project-2` folder that does not exist in the repository, and my Desktop path failed because it sits inside OneDrive. My partner's run, on their own computer, finished with no errors in 4 minutes 45 seconds after the README fix. (Draft from the recorded facts; rewrite in your own words.)
2. What I will not touch before the deadline: TODO (your answer)

## Six-minute code explanation

Completed with my partner. The walkthrough covered:

1. `portfolio.py` loads the monthly price data, calculates returns, volatility, covariance, and portfolio risk, then searches the 5-point allocation grid subject to the return and reserve constraints.
2. `analysis.py` compares equal-weight, inverse-volatility, and constrained minimum-volatility portfolios, applies the mandate rules, and runs one-change-at-a-time stress cases.
3. `run_baseline.py` runs the analysis and writes the visible baseline and stress results to `output/baseline-output.md`.
4. `app.py` exposes the objective, reserve, cost, time-window, and return-estimate inputs in Streamlit and displays each portfolio's mandate result.
5. `tests/verify.py` checks the expected constrained allocation and baseline pass/fail results.

The walkthrough ended with the partner run reproducing the expected 60/0/0/40 constrained mix and `All checks passed.`
