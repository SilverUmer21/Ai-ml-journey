# Decision Trees, Random Forest and XGBoost

## 1. Dataset Preparation

I used a simple Titanic dataset to practice the implementation of tree
based models.

### One hot encoding

Categorical columns such as `sex` and `embarked` were converted into
separate binary columns using Pandas.

Example:

``` python
pd.get_dummies(df, columns=["sex", "embarked"])
```

This produced columns such as:

``` text
sex_female
sex_male
embarked_C
embarked_Q
embarked_S
```

Pandas can represent these values as `True` and `False`. These work as
binary values for our ML models.

### Separating features and target

``` python
X = df.drop("survived", axis=1)
y = df["survived"]
```

`X` contains the input features.

`y` contains the target I want to predict.

`axis=1` means I am working with columns when using `drop()`.

### Train and validation split

``` python
X_train, X_val, y_train, y_val = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)
```

`test_size=0.3` means 30% of the data is used for validation and 70% for
training.

The validation set lets us test how well the model works on data it did
not train on.

------------------------------------------------------------------------

# 2. Decision Tree

## What it does

A Decision Tree repeatedly splits the data using feature based rules.

For example, it might learn rules related to:

``` text
age
fare
pclass
sex
```

The final leaf gives the predicted class.

## Basic implementation

``` python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_val)
```

`fit()` learns the tree rules.

`predict()` uses the learned tree to make predictions.

## Important parameters

### max_depth

Controls the maximum depth of the tree.

``` python
max_depth=4
```

Smaller depth means a simpler tree.

Larger depth means a more complex tree.

`max_depth=None` means there is no maximum depth limit from this
parameter.

Large depths can cause overfitting.

### min_samples_split

Controls the minimum number of samples required before a node can be
split.

``` python
min_samples_split=50
```

Increasing it makes the tree harder to split and therefore less complex.

## What I observed

As depth increased, training accuracy generally increased, but
validation accuracy did not necessarily increase.

Example:

``` text
Depth 2  Train 80.5%  Validation 75.7%
Depth 12 Train 97.6%  Validation 72.4%
```

This showed overfitting.

The model was becoming better at the training data without becoming
better at unseen data.

------------------------------------------------------------------------

# 3. Random Forest

## Why I use it

A Random Forest combines many Decision Trees instead of relying on one
tree.

Each tree contributes to the final prediction.

The idea is to get a more robust model than a single Decision Tree.

## Basic implementation

``` python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=8,
    min_samples_split=50,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_val)
```

## Important parameters

### n_estimators

Number of Decision Trees in the forest.

``` python
n_estimators=100
```

More trees generally give the forest more trees to combine, but more
trees do not guarantee better validation accuracy.

### max_depth

Controls the maximum depth of each tree in the forest.

### min_samples_split

Controls how easily each tree can split its nodes.

Increasing it generally makes the individual trees less complex.

## What I observed

With:

``` text
n_estimators = 100
max_depth = 8
min_samples_split = 50
```

I got about:

``` text
Train: 83.5%
Validation: 78.5%
```

In our experiments, increasing the depth from 2 to 8 improved validation
accuracy, but increasing it further did not help.

------------------------------------------------------------------------

# 4. XGBoost

## Main idea

XGBoost is a boosting algorithm.

Instead of building independent trees like Random Forest, XGBoost builds
trees sequentially.

Each new tree tries to improve the current model by focusing on its
errors.

Basic mental model:

``` text
Tree 1
Tree 2 improves the model
Tree 3 improves the model
Tree 4 improves the model
...
```

The trees are combined into one final model.

## Basic implementation

``` python
from xgboost import XGBClassifier

model = XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=4,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_val)
```

------------------------------------------------------------------------

# 5. Important XGBoost Parameters

## n_estimators

Maximum number of boosting rounds or trees.

``` python
n_estimators=500
```

More trees give the model more opportunities to learn.

However, too many trees can lead to overfitting.

## learning_rate

Controls how strongly each new tree contributes to the model.

``` python
learning_rate=0.1
```

Small learning rate:

``` text
Smaller updates
Usually needs more trees
```

Large learning rate:

``` text
Larger updates
Usually needs fewer trees
Can overfit faster
```

`learning_rate` and `n_estimators` should therefore be considered
together.

For example:

``` text
Small learning_rate + more trees
Large learning_rate + fewer trees
```

There is no universally best combination. It depends on the dataset and
other parameters.

## max_depth

Controls the depth of each tree.

Larger values make individual trees more complex.

Smaller values make them simpler.

Large values can increase overfitting.

------------------------------------------------------------------------

# 6. What I Observed With XGBoost

I experimented with different learning rates.

Our best validation accuracy in that experiment was around:

``` text
learning_rate = 0.2
Validation accuracy = 81.1%
```

I then tested different combinations of:

``` text
learning_rate
n_estimators
```

I observed that increasing the number of estimators often increased
training accuracy, but validation accuracy could eventually decrease.

For example, with a learning rate of 0.5:

``` text
20 trees  Train 92.0%  Validation 78.5%
500 trees Train 99.0%  Validation 74.8%
```

This is an example of overfitting.

------------------------------------------------------------------------

# 7. Early Stopping

## Problem

If I set:

``` python
n_estimators=500
```

XGBoost can keep adding trees even after validation performance stops
improving.

This can lead to overfitting.

## Solution

Early stopping monitors validation performance and stops training when
it stops improving.

Example:

``` python
model = XGBClassifier(
    n_estimators=500,
    learning_rate=0.1,
    max_depth=4,
    early_stopping_rounds=20,
    eval_metric="error",
    random_state=42
)

model.fit(
    X_train,
    y_train,
    eval_set=[(X_val, y_val)],
    verbose=False
)
```

`n_estimators=500` now acts as an upper limit.

`early_stopping_rounds=20` means training stops when the validation
metric does not improve for 20 consecutive rounds.

## Best iteration

``` python
model.best_iteration
```

This tells us which boosting round had the best validation performance.

In our experiment:

``` text
Best iteration: 2
Best validation error: 0.2336
Validation accuracy: 0.7664
```

Because:

``` text
accuracy = 1 - error
```

So:

``` text
1 - 0.2336 = 0.7664
```

------------------------------------------------------------------------

# 8. Accuracy and Overfitting

i compared training and validation accuracy throughout the experiments.

A large gap can indicate overfitting.

Example:

``` text
Train: 99%
Validation: 71%
```

The model learned the training data very well but generalized poorly.

A smaller gap is generally better, although i still care about getting
good validation performance.

The validation score is more useful for judging how well the model
generalizes to unseen data.

------------------------------------------------------------------------

# 9. Parameter Relationships

## Decision Tree

``` text
max_depth
    controls tree depth

min_samples_split
    controls how easily nodes can split
```

Increasing complexity can increase training accuracy but also increase
overfitting.

## Random Forest

``` text
n_estimators
    number of trees

max_depth
    depth of each tree

min_samples_split
    splitting restriction for each tree
```

The forest combines many trees, while these parameters control how those
trees are built.

## XGBoost

``` text
n_estimators
    number of boosting rounds

learning_rate
    contribution of each new tree

max_depth
    complexity of each tree

early_stopping_rounds
    stops training when validation performance stops improving
```

The most important relationship i practiced was:

``` text
learning_rate and n_estimators
```

A smaller learning rate generally needs more trees.

A larger learning rate generally needs fewer trees.

------------------------------------------------------------------------

# 10. What I Learned

I learned the complete basic workflow for tree based classification
models:

``` text
Prepare data
Encode categorical features
Separate X and y
Split training and validation data
Train model
Predict
Measure accuracy
Compare train vs validation
Tune parameters
Check for overfitting
Use early stopping with XGBoost
```

I also learned the practical scikit-learn and XGBoost APIs instead of
only knowing the theory.

The next useful step is to build these models again on another dataset
without following a full tutorial, especially spending more practice
time with XGBoost.
