# 🐼 Pandas Mastery Roadmap — Progress Tracker
> **Goal:** Master Pandas for AI/ML Engineering
> **Legend:** 🔴 Deep Understanding · 🟡 Working Knowledge · 🟢 Skim
> **Status:** ⬜ Not Started · 🔄 In Progress · ✅ Done

---

## HOW TO USE THIS FILE
- Upload this file at the start of every session
- Claude will read it, know exactly where you are, and continue from there
- After each session, Claude will give you an updated version to replace this one

---

## 📍 CURRENT POSITION
**Currently on:** Not started yet
**Next topic:** Level 1 — Topic 1: Why Pandas Exists
**Last session:** N/A

---

## LEVEL 1 — Understanding Pandas

| # | Topic | Priority | Status | Notes |
|---|-------|----------|--------|-------|
| 1 | Why Pandas Exists | 🔴 | ⬜ | NumPy limits, structured data, DataFrame mindset |
| 2 | Series | 🔴 | ⬜ | Index, values, vectorized ops, labeled NumPy array |
| 3 | DataFrame | 🔴 | ⬜ | Creating from dict/list/NumPy/CSV, rows/cols/index/dtypes |

---

## LEVEL 2 — Exploring Data

| # | Topic | Priority | Status | Notes |
|---|-------|----------|--------|-------|
| 4 | Reading Data | 🔴 | ⬜ | read_csv, read_excel, read_json + params |
| 5 | Inspecting Data | 🔴 | ⬜ | head/tail/info/describe/shape/dtypes/sample |
| 6 | Selecting Data | 🔴 | ⬜ | [], loc, iloc, at, iat — BIGGEST topic |

---

## LEVEL 3 — Filtering

| # | Topic | Priority | Status | Notes |
|---|-------|----------|--------|-------|
| 7 | Boolean Filtering | 🔴 | ⬜ | Conditions, isin, between, query, &/\|/~ |
| 8 | Missing Data | 🔴 | ⬜ | isna/fillna/dropna, imputation strategies, bias risk |

---

## LEVEL 4 — Data Cleaning

| # | Topic | Priority | Status | Notes |
|---|-------|----------|--------|-------|
| 9 | Cleaning Columns | 🔴 | ⬜ | Rename, strip, lowercase, dedup, drop, reset_index |
| 10 | Data Types | 🟡 | ⬜ | astype, to_datetime, category, numeric conversion |

---

## LEVEL 5 — Aggregation

| # | Topic | Priority | Status | Notes |
|---|-------|----------|--------|-------|
| 11 | Statistics | 🔴 | ⬜ | mean/median/mode/std/var/quantile/value_counts/nunique |
| 12 | GroupBy | 🔴 | ⬜ | groupby, agg, multiple aggregations — VERY important |
| 13 | Pivot Tables | 🟡 | ⬜ | pivot, pivot_table, cross-tab |

---

## LEVEL 6 — Transforming Data

| # | Topic | Priority | Status | Notes |
|---|-------|----------|--------|-------|
| 14 | Sorting | 🔴 | ⬜ | sort_values, sort_index, ascending, multi-col |
| 15 | Apply Functions | 🔴 | ⬜ | apply, map, lambda, when to use vectorization instead |
| 16 | String Operations | 🟡 | ⬜ | str.contains/replace/lower/upper/strip/split |
| 17 | Date & Time | 🟡 | ⬜ | to_datetime, dt.year/month/day/hour |

---

## LEVEL 7 — Combining Data

| # | Topic | Priority | Status | Notes |
|---|-------|----------|--------|-------|
| 18 | Merge | 🔴 | ⬜ | merge(), left/right/inner/outer joins |
| 19 | Concatenate | 🟡 | ⬜ | concat(), deprecated append |

---

## LEVEL 8 — Performance

| # | Topic | Priority | Status | Notes |
|---|-------|----------|--------|-------|
| 20 | Vectorization | 🔴 | ⬜ | Why loops/apply are slow, vectorized ops win |
| 21 | Memory Optimization | 🟢 | ⬜ | category dtype, smaller int types, memory_usage |

---

## LEVEL 9 — Exporting

| # | Topic | Priority | Status | Notes |
|---|-------|----------|--------|-------|
| 22 | Saving Data | 🟡 | ⬜ | to_csv, to_excel, to_json |

---

## LEVEL 10 — Visualization (Light)

| # | Topic | Priority | Status | Notes |
|---|-------|----------|--------|-------|
| 23 | Quick Plots | 🟢 | ⬜ | plot(), hist(), boxplot() — light touch only |

---

## 🏗️ PROJECTS

| # | Project | Unlocks After | Status | Notes |
|---|---------|--------------|--------|-------|
| P1 | Student Result Analyzer | Topics 1–3 | ⬜ | CSV → highest/lowest/avg/pass%/top 10 |
| P2 | Customer Data Cleaner | Topics 7–9 | ⬜ | Dedup, fill missing, rename, clean phone/names |
| P3 | Sales Dashboard Backend | Topics 11–12 | ⬜ | Revenue, top products, by city, monthly, avg order |
| P4 | Employee Database Analyzer | Topic 18 | ⬜ | Merge 3 CSVs → reports |
| P5 ⭐ | EDA Toolkit (Mandatory) | All topics | ⬜ | Upload any CSV → auto full analysis report |

---

## ⚠️ COMMON MISTAKES TO REVISIT
- [ ] Using loops (`iterrows`) instead of vectorized ops
- [ ] Chaining methods without understanding each step
- [ ] Ignoring missing values before modeling
- [ ] Not checking dtypes with `df.info()` first
- [ ] Confusing `loc` (labels) with `iloc` (positions)

---

## 📊 OVERALL PROGRESS
**Topics completed:** 0 / 23
**Projects completed:** 0 / 5
**Progress:** ░░░░░░░░░░ 0%

---

*Last updated: Session 0 (roadmap created)*
