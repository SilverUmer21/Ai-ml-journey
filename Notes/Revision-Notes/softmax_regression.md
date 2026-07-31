# Softmax Summary 
Softmax is the multi-class extension of logistic regression.
Every class has its own weights (wj) and own bias (bj).
For each class, compute a score: zj=wj⋅x+bj.
These scores (logits) are not probabilities.
Softmax converts all logits into probabilities using exponentials and normalization.
All output probabilities always add up to 1.
The predicted class is simply the one with the highest probability.
During training, the loss only uses the probability assigned to the correct class: −log(aj).
If the model assigns a high probability to the correct class, the loss is close to 0.
If it assigns a very low probability to the correct class, the loss becomes very large, pushing the model to improve.