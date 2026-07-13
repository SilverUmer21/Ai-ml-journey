import numpy as np 

x = np.array([1, 2, 3])
y = np.array([3, 5, 7])

w = 1
b = 0

ALPHA = 0.01 
ITERATIONS = 500

def predict(x,w,b):
    return x*w+b

 
def compute_cost(x,y,w,b):
    prediction = predict(x,w,b)
    
    error = prediction - y
    squared_error = error ** 2
    total_error = np.sum(squared_error)
    m= len(x)   # number of examples

    cost = total_error/(2*m)

    return cost

def compute_gradients(x,y,w,b):
    predictions = predict(x,w,b)
    m = len(x)
    error = predictions-y
    
    dj_dw = np.sum(error*x) / m
    dj_db = np.sum(error) / m
    
    return dj_dw,dj_db


def gradient_descent(x,y,w,b,alpha,iterations):

    for i in range(iterations):

        if i % 100 == 0 :
            print (f"At {i}th iteration Cost is {compute_cost(x,y,w,b)}")
        
        dj_dw,dj_db = compute_gradients(x,y,w,b)
        w = w - alpha*dj_dw
        b = b - alpha*dj_db

    return w,b


w , b = gradient_descent(x,y,w,b,ALPHA,ITERATIONS)
print(w)
print(b)

print(compute_cost(x,y,w,b))
