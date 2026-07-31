# Numerical Round off errors 
![alt text](<../../Assets/Screenshots/round off error.png>)
because the computer has a finite memory , so the way we decide to compute 2/10000 , will result in more or less round off error

# Logistic regression round off erros
![alt text](<../../Assets/Screenshots/logistic round off errors.png>)
But instead, by specifying ​this expression at the bottom ​directly as the loss function, ​it gives TensorFlow more flexibility in terms of ​how to compute this and whether or not ​it wants to compute a explicitly. ​The code you can use to do this ​is shown here and what this does is it ​sets the output layer to just use ​a linear activation function and it ​puts both the activation function, ​1/1 plus to the negative z, ​as well as this cross entropy loss into ​the specification of the loss function over here.

# Softmax round off erros
![alt text](<../../Assets/Screenshots/softmax round off.png>)
Softmax converts logits into probabilities.
Logits are the raw outputs z=Wx+b.
Softmax probabilities always sum to 1.
During Training
Prefer activation="linear" in the output layer.
Use SparseCategoricalCrossentropy(from_logits=True).
TensorFlow internally applies Softmax and Cross-Entropy together.
Why use from_logits=True?
Prevents floating-point roundoff errors.
Avoids extremely large or tiny values from exponentials.
Uses optimized algorithms (including the log-sum-exp trick) for stable computation.
Produces the same mathematical result with better numerical accuracy.
During Prediction : logits = model(X)
probabilities = tf.nn.softmax(logits)
## Important Points : 
Logits = raw scores (z).
Softmax = converts logits → probabilities.
Cross-Entropy = measures how wrong the prediction is.
from_logits=True = "My model outputs logits, so please apply Softmax internally before computing the loss."
The difference is implementation, not mathematics. Both approaches optimize the same objective; the second is simply more reliable on real computers.
