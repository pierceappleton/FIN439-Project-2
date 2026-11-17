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

Not recorded yet (TODO).

- Command:
- First failure:
- Elapsed time:
- Where the result was:

## Fix pushed

README now has the clone step, a folder note, the verify command and the expected result, and the wrong `project-2` folder reference is removed. A `.gitignore` keeps `.venv/` out of the repository. Commit: 45c87ce. My partner reran from the fixed README with no errors.

## Decision line

TODO: one line (adopt, allocate to, rebalance, pilot or reject) with the condition that would reverse it.

## Reflect

1. What the cold run found that I could not see:
2. What I will not touch before the deadline:
