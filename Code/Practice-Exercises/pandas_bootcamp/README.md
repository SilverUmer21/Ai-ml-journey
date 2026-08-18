# Pandas fundamentals bootcamp

Start here before project engineering. The notebook deliberately begins with `Series` and `DataFrame`, then moves to selection, cleaning, grouping, merging, encoding, and train/test preprocessing.

## Setup

From this directory in PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pandas scikit-learn jupyter
jupyter notebook pandas_fundamentals_offline.ipynb
```

If PowerShell blocks activation, activation is optional:

```powershell
.\.venv\Scripts\python.exe -m pip install pandas scikit-learn jupyter
.\.venv\Scripts\python.exe -m jupyter notebook pandas_fundamentals_offline.ipynb
```

## Learning rules

1. Read one concept cell.
2. Predict the result before running code.
3. Fill the TODO without asking AI for the finished line.
4. Run the check cell.
5. If stuck for 20 minutes, report expected behavior, actual behavior, exact error, attempts, and your hypothesis.
6. Ask for one hint, retry, and record the mistake in `STUCK_LOG.md`.

Do not move to project scaffolding until you can explain:

- Why a Series is one-dimensional and a DataFrame is two-dimensional.
- The difference between `.loc` and `.iloc`.
- Why preprocessing is fitted only on training data.
- What `groupby`, `merge`, missing-value handling, and one-hot encoding do.

