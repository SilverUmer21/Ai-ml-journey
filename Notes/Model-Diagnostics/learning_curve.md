![alt text](<../../Assets/Screenshots/image copy 7.png>)
In this example , we learned that as we increase the number of training examples, it is harder for the quadratic model we made to fit all the training data to the curve. Thats why J_train is increasing as we increase m_train 

# High bias (underfiting)
![alt text](<../../Assets/Screenshots/image copy 8.png>)

If a learning model has bias then adding more and more training data wont help, which in our case we can see the J_cv and J_train getting steep as the model isnt changing much even after adding more and more training examples
![alt text](<../../Assets/Screenshots/image copy 9.png>)

# High variance (overfitting)
![alt text](<../../Assets/Screenshots/image copy 10.png>)

If a learning model has High variance then it can be possible that adding more training data can produce better model and the J_cv may approach J_train which gives us the indication that the model is learning rather than overfitting now.
![alt text](<../../Assets/Screenshots/image copy 11.png>)

## "Remarks on plotting the learning curve" from Andrew Ng 
​One downside of the plotting learning curves ​like this is something I've done, ​but one downside is, ​it is computationally quite expensive to train ​so many different models using ​different size subsets of ​your training set, so in practice, ​it isn't done that often, but nonetheless, ​I find that having ​this mental visual picture ​in my head of what the training set looks like, ​sometimes that helps me to think through what I think ​my learning algorithm is doing and whether it ​has high bias or high variance.