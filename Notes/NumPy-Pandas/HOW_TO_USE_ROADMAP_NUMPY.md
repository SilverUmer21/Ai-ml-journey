# How to Use the NumPy Mastery Tracker

This file is part of the **AI/ML Journey** repository. It documents how to get the most out of `numpy_mastery_tracker.md` — a living progress file designed to work with a teaching AI (Claude) across multiple sessions.

---

## What This File Is

`numpy_mastery_tracker.md` is not just a checklist. It is the **shared memory** between you and your AI tutor. Every topic, project, and session you complete gets recorded here. At the start of each new session, uploading this file tells the AI exactly:

- What you've already learned
- What depth you need (skim, working knowledge, or deep understanding)
- Where you left off
- What comes next

Without it, every session starts from zero. With it, every session is a continuation.

---

## Workflow: How Each Session Should Go

**1. Start of session — upload the file**

Open a new Claude conversation and upload `numpy_mastery_tracker.md` as your first message. You don't need to explain anything. The AI reads the file and resumes from your current topic automatically.

**2. During the session — learn, then practice**

For each topic, the flow is:
1. AI teaches the concept intuitively
2. You ask questions until it clicks
3. AI gives you exercises (easy → hard)
4. You solve them independently — no hints first
5. You share your solution, AI gives feedback

Don't rush past the exercises. The exercises are where the learning actually happens.

**3. End of session — update the file**

Before closing, tell the AI: *"Update the tracker."* It will tell you exactly which lines to change — status symbols, session log row, and the "Currently Working On" field. Make those edits and save the file. Next session, upload the updated version.

---

## Status Symbols — What They Mean in Practice

| Symbol | Status | What to do |
|--------|--------|------------|
| ⬜ | Not started | This is the queue |
| 🔄 | In progress | You opened the topic but haven't finished exercises |
| ✅ | Complete | Concept understood + exercises done |

A topic is only ✅ when you've done the exercises, not just read the explanation.

---

## Depth Levels — How Hard to Push

| Level | Symbol | What it means for you |
|-------|--------|----------------------|
| Deep Understanding | 🔴 | Know *why* it works, not just how to use it. Expect harder exercises and conceptual questions. |
| Working Knowledge | 🟡 | Know how to use it comfortably. Get the syntax and common patterns right. |
| Skim | 🟢 | Know it exists. One read-through is enough for now. |

When a topic is 🔴, don't move on until you can answer *"why"* questions out loud without looking anything up.

---

## The Projects Are Not Optional

Each mini-project unlocks after a set of topics and **must be built before moving to the next level**. They exist because reading and doing exercises is not enough — building something real with no guidance is where the knowledge solidifies.

The mandatory one is **Project 4: Linear Regression from Scratch** (NumPy only, no sklearn). Do not skip it.

---

## The Rougier 100 Exercises

The [100 NumPy Exercises](https://github.com/rougier/numpy-100) by Nicolas Rougier are mapped to topics in the tracker. Don't solve them in order — let the AI pull the relevant ones as you study each topic. This keeps the exercises contextual rather than random.

---

## Tips for Getting the Most Out of This

- **Don't paste solutions from the internet.** If you're stuck, ask for a hint, not the answer. The struggle is the point.
- **Ask "why" constantly.** Especially on 🔴 topics. If you can't explain it to someone else, you don't know it yet.
- **Keep the file honest.** If a topic felt shaky, leave it as 🔄. Don't mark ✅ until it's real.
- **One topic per session is fine.** Depth over speed, especially in Level 1 and Level 4.
- **The session log is useful.** Over time it shows you how far you've come, which matters when things get hard.

---

## File Location in This Repo

```
ai-ml-journey/
└── numpy/
    ├── numpy_mastery_tracker.md   ← upload this every session
    └── HOW_TO_USE_NUMPY_TRACKER.md ← you are reading this
```

---

*Built for the ML Engineer path. The goal is not to memorize NumPy — it is to think in arrays.*
