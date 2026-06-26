#  How to Use the Pandas Roadmap Tracker

This file explains how to get the most out of `pandas_roadmap.md` — your session-by-session progress tracker for the Pandas Mastery curriculum.

---

## The Core Idea

The roadmap file is your **shared memory with Claude**. Claude has no memory between conversations by default. This file fixes that. Every time you start a new session, you upload it — Claude reads it and instantly knows:

- What you've already learned
- What's next
- Any notes or struggles from past sessions

At the end of every session, Claude gives you an **updated version** of the file to replace the old one. That's the whole system.

---

## Session Start — What to Do

1. Open a new Claude conversation
2. Upload `pandas_roadmap.md`
3. Say something like: **"Let's continue from where we left off"** or **"Start the next topic"**

Claude will read the file, orient itself, and begin. No need to re-explain what you know.

---

## Session End — What to Do

Before closing the conversation, say: **"Update the roadmap file."**

Claude will give you a fresh `pandas_roadmap.md` with:
- Completed topics marked ✅
- Your current position updated
- Any notes from the session added (struggles, shortcuts, things to revisit)

Download it and **replace the old file** in this repo. That's your next session's starting point.

---

## How the Priority Levels Work

The topics are tagged with three priority levels — this tells Claude how deep to go:

| Icon | Level | What it means in practice |
|------|-------|--------------------------|
| 🔴 | Deep Understanding | Full explanation + code + exercises + edge cases. You should be able to use this without thinking. |
| 🟡 | Working Knowledge | Solid coverage, some practice. You'll know how and when to use it. |
| 🟢 | Skim | Brief intro only. You'll know it exists and can look it up when needed. |

You don't need to memorize this — Claude already knows how to treat each topic based on its tag.

---

## How Projects Fit In

Five projects are built into the roadmap, each unlocking after a specific set of topics. Don't skip them — they're not optional exercises, they're where the concepts actually stick.

The final project, **P5: EDA Toolkit**, is the most important one. It mirrors the first step of nearly every real ML workflow. By the time you build it, you'll have a reusable tool you can actually use in future projects.

---

## A Few Tips

**Don't rush the 🔴 topics.** Topics like `loc/iloc`, `GroupBy`, and `Merge` will show up constantly in real ML work. It's worth going slow and getting them solid the first time.

**Tell Claude when something didn't click.** If an explanation didn't land, just say so. Claude will try a different angle — an analogy, a diagram, a different example. Add a note in the roadmap file so future sessions know to revisit it.

**Treat the common mistakes section as a checklist.** Before finishing any project, go through the ⚠️ section at the bottom of the roadmap and make sure you're not making those errors. They're listed there because they trip up almost everyone.

**One topic per session is fine.** Some 🔴 topics deserve a full session on their own. Don't feel pressure to rush through. Consistency over speed.

---

## File Location in This Repo

```
/pandas/
├── pandas_roadmap.md        ← the tracker (update this after every session)
└── HOW_TO_USE_ROADMAP.md    ← this file
```

---

*This system works best when you're consistent — upload, learn, update, repeat.*
