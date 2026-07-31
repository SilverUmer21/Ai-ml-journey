# NumPy Mastery roadmap — ML Engineer Edition

> Upload this file at the start of every session so Claude knows exactly where you are and what's next. This would burn tokkens instead make Project in claude and add this md file to memory/context.

---

## Legend

| Symbol | Meaning |
|--------|---------|
| 🔴 | Deep Understanding required |
| 🟡 | Working Knowledge required |
| 🟢 | Skim only |
| ⬜ | Not started |
| 🔄 | In progress |
| ✅ | Complete |

---

## LEVEL 1 — NumPy Foundations
> Goal: Replace Python lists with NumPy thinking.

| # | Topic | Depth | Status | Notes |
|---|-------|-------|--------|-------|
| 1 | Why NumPy Exists | 🔴 | ⬜ | Why lists are slow, memory layout, speed |
| 2 | Creating Arrays | 🟡 | ⬜ | array, arange, linspace, zeros, ones, eye, random |
| 3 | Shape Fundamentals | 🔴 | ⬜ | shape/size/ndim, reshape, ravel, (5,) vs (5,1) |
| 4 | Indexing & Slicing | 🔴 | ⬜ | boolean, fancy, multidim — must be second nature |

**Level 1 Mini-Project:** ⬜ Matrix Calculator (addition, subtraction, multiplication, transpose, determinant)

---

## LEVEL 2 — Array Operations

| # | Topic | Depth | Status | Notes |
|---|-------|-------|--------|-------|
| 5 | Vectorization | 🔴 | ⬜ | Rewrite for-loops into NumPy; SIMD concept |
| 6 | Broadcasting | 🔴 | ⬜ | THE most important topic; rules + ML usage |
| 7 | Universal Functions (ufuncs) | 🟡 | ⬜ | sqrt, exp, log, abs, maximum, minimum |
| 8 | Mathematical Operations | 🔴 | ⬜ | sum/mean/std/argmax etc; axis parameter deeply |

**Level 2 Mini-Project:** ⬜ Student Marks Analyzer (CSV → highest, average, top students, fail %)

---

## LEVEL 3 — Array Manipulation

| # | Topic | Depth | Status | Notes |
|---|-------|-------|--------|-------|
| 9 | Reshaping | 🔴 | ⬜ | reshape/ravel/flatten; View vs Copy deeply |
| 10 | Joining Arrays | 🟡 | ⬜ | concatenate, stack, vstack, hstack, split |
| 11 | Sorting & Searching | 🟡 | ⬜ | sort, argsort, where, nonzero, searchsorted |
| 12 | Boolean Logic | 🔴 | ⬜ | masking, logical_and/or, filtering — used in every ML notebook |

**Level 3 Mini-Project:** ⬜ Image Brightness Manipulator (brightness, contrast, invert, grayscale, crop)

---

## LEVEL 4 — Linear Algebra
> The heart of ML.

| # | Topic | Depth | Status | Notes |
|---|-------|-------|--------|-------|
| 13 | Matrix Multiplication | 🔴 | ⬜ | dot(), @, matmul(); element-wise vs matmul |
| 14 | Linear Algebra Basics | 🔴 | ⬜ | transpose, inverse, det, rank, trace, eigenvalues, norms |

**Level 4 Mini-Project:** ⬜ Linear Regression FROM SCRATCH (NumPy only, no sklearn) — MANDATORY

---

## LEVEL 5 — Random Module

| # | Topic | Depth | Status | Notes |
|---|-------|-------|--------|-------|
| 15 | Random Numbers | 🟡 | ⬜ | seed, rand, randn, integers, choice, shuffle, permutation |

---

## LEVEL 6 — Performance

| # | Topic | Depth | Status | Notes |
|---|-------|-------|--------|-------|
| 16 | Memory | 🔴 | ⬜ | views, copies, contiguous arrays, itemsize, nbytes |
| 17 | Vectorized Thinking | 🔴 | ⬜ | Mindset: auto-ask "Can I remove this loop?" |
| 18 | Time Complexity | 🟡 | ⬜ | Which ops copy, which don't; why repeated concat is slow |

**Level 5+6 Mini-Project:** ⬜ Mini Data Analysis Toolkit (CSV → stats, missing values, normalization, correlation matrix)

---

## LEVEL 7 — File Handling

| # | Topic | Depth | Status | Notes |
|---|-------|-------|--------|-------|
| 19 | Loading Data | 🟡 | ⬜ | loadtxt, genfromtxt, save, load, npz, csv basics |

---

## LEVEL 8 — Advanced

| # | Topic | Depth | Status | Notes |
|---|-------|-------|--------|-------|
| 20 | Structured Arrays | 🟢 | ⬜ | Skim only |
| 21 | Custom dtypes | 🟢 | ⬜ | Skim only |
| 22 | Strides | 🔴 | ⬜ | Concept only — explains views, transpose, performance |
| 23 | Broadcasting Internals | 🟢 | ⬜ | Skim only |
| 24 | Advanced Indexing | 🟡 | ⬜ | Good working knowledge |
| 25 | np.einsum | 🟢 | ⬜ | Know it exists; don't master now |

---

## Projects Summary

| # | Project | Unlocks After | Status |
|---|---------|--------------|--------|
| P1 | Matrix Calculator | Topics 1–4 | ⬜ |
| P2 | Student Marks Analyzer | Topics 5–8 (bool + stats) | ⬜ |
| P3 | Image Brightness Manipulator | Topic 6 (Broadcasting) | ⬜ |
| P4 | Linear Regression from Scratch | Topics 13–14 (Lin Algebra) | ⬜ |
| P5 | Mini Data Analysis Toolkit | Topics 15–18 (Random + Perf) | ⬜ |

---

## Rougier 100 Exercises Mapping

> Don't solve in order. Map to topic being studied.

| Topic | Relevant Rougier Exercise Range |
|-------|---------------------------------|
| Array creation, indexing, reshaping | Early exercises (roughly 1–35) |
| Statistics, broadcasting, vectorization | Mid exercises (roughly 36–65) |
| Structured arrays, performance, advanced indexing | Later exercises (roughly 66–100) |

**Exercises Completed:** None yet

---

## Session Log

| Session | Date | Topics Covered | Exercises Done | Notes |
|---------|------|---------------|---------------|-------|
| 1 | — | — | — | Starting fresh |

---

## How to Use This File

1. **Upload at session start** — Claude reads it and knows exactly where you are.
2. **After each topic** — Tell Claude to update the status (⬜ → 🔄 → ✅).
3. **After each project** — Mark P1–P5 complete in the Projects Summary.
4. **Session log** — Claude will add a row after each session.
5. **"What's next?"** — Claude reads the first ⬜ in the table and resumes from there.
