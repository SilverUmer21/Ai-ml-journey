# Full Cycle of an ML Project + Deployment

Prof made the point that training the model is only *one* piece of building a real ML system. There's a whole cycle around it. He used speech recognition (voice search on phone) as the running example.

## The 4 stages

![Full cycle diagram](../../Assets/Screenshots/1786371735073_image.png)
![alt text](<../../Assets/Screenshots/CamScanner 08-10-2026 16.32.jpg>)
1. **Scope project** — decide what you're even working on (e.g. "speech recognition for voice search")
2. **Collect data** — get audio + transcripts (labels)
3. **Train model** — train, do error analysis, improve
4. **Deploy in production** — ship it, then monitor + maintain

Important thing: this is NOT a straight line. Notice the arrows go backward too — from train back to collect data, and from deploy back to train/collect. So it's a loop, not a checklist.

**What:** it's the end-to-end process of building an ML product — scoping → data → training → deployment — and looping back whenever needed.

**How:** you scope the project, gather the data, train + error-analyze the model (going back for more/targeted data if a weakness shows up, like his example of the model failing on car-noise audio → he used data augmentation to fix it), then deploy. Even after deployment you're not done — if it underperforms in the real world you loop back to training or data collection again.

**Why:** because a model that's great on your dataset can still fail in the real world (new slang, new celebrity names, changing user behavior). If you don't loop back and keep improving, the system just degrades over time. Treating ML as one-and-done training run is the mistake beginners make.

---

## Deployment in detail

![Deployment diagram](../../Assets/Screenshots/1786371733901_image.png)

So deployment usually looks like:

- Model gets wrapped inside an **inference server**
- Some client (e.g. mobile app) makes an **API call** with input `x` (here, the audio clip)
- Inference server runs the model and sends back the prediction `ŷ` (here, the text transcript)

**What:** deployment = taking your trained model and putting it behind an API so real apps can call it and get predictions back.

**How:** mobile app records audio → sends it via API call to inference server → inference server runs the ML model → sends back ŷ (transcript) → app shows it to user. Around this, software engineering work is needed for:
- reliable & efficient predictions (low latency/cost)
- scaling to however many users you have
- logging inputs/predictions (only if privacy/consent allows)
- system monitoring
- model updates when needed

This whole practice has a name: **MLOps** (Machine Learning Operations) — systematically building, deploying, and maintaining ML systems.

**Why:** because the real world shifts under your model. Prof's own example — his speech system was trained on old data, then new politicians got elected / new celebrities got famous, and people started searching those names. Model hadn't seen those words → performance dropped. Only because they were *monitoring* the system did they catch the shift, retrain, and push a model update. Without monitoring + maintenance, you'd just have a silently rotting model in production.

Also noted: how much software engineering this needs depends on scale — a laptop demo for a few users needs way less than a system serving hundreds of millions.
