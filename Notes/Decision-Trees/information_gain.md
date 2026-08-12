# Information Gain

(how decision trees actually pick which feature to split on)

## quick entropy recap
H(p) = impurity. p = fraction that are cats.
H(0.5) = 1, worst case, totally mixed
H(0) = H(1) = 0, pure

## the problem
3 candidate features at root (ear shape, face shape, whiskers). Each split gives you TWO entropy numbers (left + right). Can't compare 6 numbers across 3 splits directly, need it collapsed to one number per split.

ear shape: left p=0.8, H=0.72. right p=0.2, H=0.72
face shape: left p=0.57, H=0.99. right p=0.33, H=0.92
whiskers: left p=0.75, H=0.81. right p=0.33, H=0.92

## step 1, weighted avg
weight by how many examples went each way. makes sense, high entropy in a branch w/ 5 examples is worse than high entropy in a branch w/ 1 example.

ear shape: (5/10)(0.72) + (5/10)(0.72)
face shape: (7/10)(0.99) + (3/10)(0.92)
whiskers: (4/10)(0.81) + (6/10)(0.92)

## step 2, information gain, the actual formula used
just: entropy before split minus weighted entropy after split.

root has 5 cats/10 total, p=0.5, H=1 (max impurity before we do anything)

**Info Gain = H(root) - [w_left*H(left) + w_right*H(right)]**

ear shape: 1 - 0.72 = **0.28**
face shape: 1 - 0.97 = **0.03**
whiskers: 1 - 0.88 = **0.12**

ear shape wins, this is why root splits on ear shape. matches last lecture.

side note: could've just compared weighted averages directly (ear shape still wins), didn't NEED the subtraction. so why bother?

because "reduction in entropy" is the number you check against the stopping threshold later. "improvement below threshold, don't split", that's literally checking if info gain is too small. raw weighted entropy doesn't give you that comparison point as cleanly.

## general formula
p1_root, p1_left, p1_right = fraction cats in root/left/right
w_left, w_right = fraction of examples that went left/right

$$IG = H(p_1^{root}) - (w^{left}H(p_1^{left}) + w^{right}H(p_1^{right}))$$

applies at ANY node, not just root. compute for every candidate feature, pick highest.

## what this means
info gain = how much a split reduces mess. pick the feature that reduces it the most.

*Source: Andrew Ng, Machine Learning Specialization*
