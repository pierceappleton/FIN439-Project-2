"""Project 2 app. Run: python -m streamlit run app.py"""
import streamlit as st

import analysis as a

st.set_page_config(page_title="Meridian allocation", layout="wide")
st.title("Meridian Foundation allocation tool")
st.caption("AI use: built with Claude assistance; the analysis and decision are mine. "
           "Education, not investment advice.")

objective = st.sidebar.number_input("Objective (%)", value=a.OBJECTIVE * 100, step=0.1) / 100
reserve_min = st.sidebar.number_input("Reserve minimum (%)", 0.0, 100.0, a.RESERVE_MIN * 100) / 100
cost = st.sidebar.number_input("Annual cost allowance (%)", 0.0, 5.0, 0.0, 0.05) / 100
last_36 = st.sidebar.toggle("Last 36 monthly returns", value=False)

try:
    sleeves, corr, meta = a.load(last_36)
    st.write(f"Prices {meta['start']} to {meta['end']}: {meta['returns']} monthly returns. "
             "Historical arithmetic estimates, not forecasts.")
    edited = []
    for col, (n, r, v) in zip(st.columns(len(sleeves)), sleeves):
        edited.append((n, col.number_input(f"{n} return (%)", value=r * 100, step=0.5,
                                           key=f"{n}-{last_36}") / 100, v))
    res, found = a.portfolios(edited, corr, objective, reserve_min, cost)
    if found is None:
        st.warning("No mix on the 5-point grid meets the objective and reserve rule.")
    for col, (name, r) in zip(st.columns(len(res)), res.items()):
        col.subheader(name)
        col.table({"Asset": [s[0] for s in edited],
                   "Weight (%)": [f"{w * 100:.1f}" for w in r["weights"]]})
        col.metric("Net return", f"{r['ret']:.2%}")
        col.metric("Volatility", f"{r['vol']:.2%}")
        col.markdown("**Mandate: " + ("PASS" if r["passes"] else "FAIL") + "**")
        for rule, ok in r["rules"]:
            col.write(("✅ " if ok else "❌ ") + rule)
        col.write("⚠️ Calendar-year loss limit: requires CIO clarification")
    st.header("Stress run")
    base, rows = a.stress(objective, reserve_min)
    st.table([{"Case": r["case"],
               "Weights (BIL/IEF/LQD/VT %)": " / ".join(f"{w * 100:.0f}" for w in r["result"]["weights"])
               if r["result"] else "infeasible",
               "Shift (pts)": "n/a" if r["shift"] is None else f"{r['shift']:.0f}",
               "Stop?": "STOP" if r["stop"] else "no"} for r in rows])
    st.caption(f"Stop condition: infeasible, or any weight moves more than {a.STOP_SHIFT_PTS:.0f} points.")
except ValueError as e:
    st.error(f"Input error: {e}")
