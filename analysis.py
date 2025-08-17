# analysis.py — Marimo interactive notebook
# Author contact: 24f2007002@ds.study.iitm.ac.in
# This notebook demonstrates variable relationships with interactive controls.
# Data-flow notes are included in each cell explaining dependencies.

import marimo as mo

app = mo.App(width="medium")


@app.cell
# Cell 1: Imports & setup
# ↓ Provides: np, pd, plt (used by later cells)
# No upstream dependencies.
def _():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    return np, pd, plt


@app.cell
# Cell 2: UI controls (widgets)
# ↓ Provides: n_slider (sample size), noise_slider (noise std dev)
# No upstream dependencies; downstream cells observe .value of these widgets.
def _(mo):
    n_slider = mo.ui.slider(50, 1000, value=200, label="Sample size n")
    noise_slider = mo.ui.slider(0.0, 2.0, value=0.5, step=0.1, label="Noise σ")
    mo.hstack([n_slider, noise_slider])  # display widgets side-by-side
    return n_slider, noise_slider


@app.cell
# Cell 3: Generate synthetic data based on widget state
# Depends on: np (from Cell 1), n_slider & noise_slider (from Cell 2)
# ↓ Provides: n, sigma, x, y (used by fitting & plotting)
def _(np, n_slider, noise_slider):
    n = int(n_slider.value)
    sigma = float(noise_slider.value)
    # Seed depends on n so re-running with different n changes the sample deterministically
    rng = np.random.default_rng(42 + n)
    x = np.linspace(0, 10, n)
    y = 2.0 * x + 3.0 + rng.normal(0.0, sigma, size=n)
    return n, sigma, x, y


@app.cell
# Cell 4: Create DataFrame & fit simple linear model
# Depends on: pd, np (Cell 1), x, y (Cell 3)
# ↓ Provides: df, slope, intercept (used by summary & plot)
def _(pd, np, x, y):
    df = pd.DataFrame({"x": x, "y": y})
    slope, intercept = np.polyfit(x, y, 1)
    return df, slope, intercept


@app.cell
# Cell 5: Dynamic markdown summary reacting to slider state
# Depends on: mo, n, sigma (Cell 3), slope, intercept, df (Cell 4)
# ↓ Provides: corr (optional metric), summary_md (rendered)
def _(mo, n, sigma, slope, intercept, df):
    corr = float(df["x"].corr(df["y"]))
    summary_md = mo.md(
        f"""
### Relationship Summary
- **n** = `{n}`, **σ** = `{sigma:.2f}`
- Fitted line: **y = {slope:.2f}·x + {intercept:.2f}**
- Pearson **r** = `{corr:.3f}`

> Tip: Drag the sliders above to see the fit and correlation update live.
"""
    )
    summary_md
    return corr, summary_md


@app.cell
# Cell 6: Plot scatter and fitted line
# Depends on: plt (Cell 1), x, y (Cell 3), slope, intercept (Cell 4)
# ↓ Provides: fig (for completeness)
def _(plt, x, y, slope, intercept):
    fig, ax = plt.subplots()
    ax.scatter(x, y, alpha=0.6)
    ax.plot(x, slope * x + intercept, linewidth=2)
    ax.set(title="Linear relationship with noise", xlabel="x", ylabel="y")
    fig
    return fig


@app.cell
# Cell 7: Provenance / data-flow diagram (simple text)
# Depends on: mo
# Purely documentary to satisfy self-documenting requirement.
def _(mo):
    mo.md(
        """
**Data Flow**
```
[Widgets: n, σ] --> [Generate x,y] --> [DataFrame & Fit] --> [Summary Markdown, Plot]
```
- `n_slider`, `noise_slider` control sample size and noise.
- Changing sliders invalidates downstream cells and recomputes dependent results.
- Email: 24f2007002@ds.study.iitm.ac.in (for contact / audit trail)
"""
    )


if __name__ == "__main__":
    # Run with:  marimo run analysis.py
    app.run()

