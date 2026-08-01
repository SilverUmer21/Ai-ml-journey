# ML From Scratch — Coding the Math Behind Andrew Ng's ML Specialization

## Why this folder exists

This folder is where I re-implement every core ML algorithm from the course — linear regression, logistic regression, neural networks — using **only NumPy**, no `sklearn.fit()`, no shortcuts.

Each lab forces me to build a model from its individual math components (prediction, cost, gradient) before combining them into a full training loop, and every implementation is checked against hand-verifiable expected values before I move on. If the assert fails, I don't proceed. Nothing here is copy-pasted from the course notebooks ; the datasets, structure, and edge cases are different on purpose, so I can't pattern-match my way through it.

## What's inside

| Notebook | Concept | What I implemented |
|---|---|---|
| `01_linear_regression.ipynb` | Linear Regression | Predict → cost (MSE) → gradient → gradient descent, single-feature then vectorized multi-feature, plus z-score normalization |
| `02_logistic_regression.ipynb` | Logistic Regression | Sigmoid → predict → log loss → gradient → gradient descent, decision boundaries |
| `03_neural_network_from_scratch.ipynb` | Neural Networks | Manual forward propagation, manual backpropagation (no TensorFlow), then a TensorFlow implementation for comparison |
| `04_regularization.ipynb` | Regularization | L2-regularized cost and gradients for both linear and logistic regression |

*(Notebooks are added as I complete them — check commit history for the latest.)*

## How each lab is structured

1. A short concept intro and the exact math formula being implemented
2. A function signature + docstring — I write the code myself, no scaffolding
3. A sanity check cell with a hand-computed expected value and a hard `assert` , if my code is wrong, it fails loudly instead of silently producing a plausible-looking wrong answer
4. A run on a larger, noisier synthetic dataset with a loss curve, to confirm the full training loop actually converges
5. A reference solution at the bottom, used only after I've already passed my own implementation

## Why this matters

I already know the theory , this is about proving I can translate math into working code, debug numerical issues (learning rate blowups, unscaled features, vanishing gradients), and reason about a model at the level of matrix shapes and gradients rather than just calling a library function. That's the level of understanding I want going into ML engineering roles.

## What's next

After these labs, I'm applying the same concepts to real datasets (California housing for regression, a binary classification dataset for logistic regression, an image dataset for the neural network) as full end-to-end projects — see the `projects/` folder once that phase starts.
