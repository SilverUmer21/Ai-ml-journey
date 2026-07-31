#Coding Questions
import numpy as np

#Implement the sigmoid function.

def sigmoid(z):
    return 1 / (1 + np.exp(-z))



#Implement the logistic regression prediction function.

def predict(X, w, b):
    z = X @ w + b
    return sigmoid(z)


#Implement the logistic cost function.

def compute_cost(X, y, w, b):
    m = X.shape[0]
    f = predict(X, w, b)
    cost = -y * np.log(f) - (1 - y) * np.log(1 - f)
    return np.sum(cost) / m


#Implement one step of gradient descent for logistic regression (gradient formula is same shape as linear regression, just f(x) is sigmoid now).

def gradient_step(X, y, w, b, alpha):
    m = X.shape[0]
    err = predict(X, w, b) - y
    dw = (X.T @ err) / m
    db = np.sum(err) / m
    w = w - alpha * dw
    b = b - alpha * db
    return w, b
