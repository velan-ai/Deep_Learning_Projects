# -*- coding: utf-8 -*-
"""1_NEURONS_AND_PERCEPTRONS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1W4BoTJlJQ5TxUVRjTr5zWbf1t1K-P1Es

#NEURONS AND PERCEPTRONS

It's a self learning project in which I tried to learn the deep learning techniques during my internship tenure
"""

#IMPORTING LIBRARIES
import numpy as np
import pandas as pd
from numpy import random, dot, exp, array, tanh
from random import choice

"""#Activation Function"""

activation_fn = lambda x: 0 if x < 0 else 1 # tells that if input is negative the o/p is 0 else 1

"""#Initializing Dataset"""

data_set=[
    ((array([0,0,1])), 0), #    (array([x,y,b]), e) --> (x,y) = Inputs; b = bias; e = Expected o/p for validation
    ((array([0,1,1])), 1),
    ((array([1,0,1])), 1),
    ((array([1,1,1])), 1)
]
print(data_set)

"""#WEIGHTS"""

weights = random.rand(3)
weights

"""#Initializing Additional variables"""

r = 0.2 # learning rate
n = 100  # number of iteration

"""# Training the Model"""

for j in range(n):
  x,expected = choice(data_set)
  res = dot(weights , x)
  err = expected - activation_fn(res)
  weights += r * err * x        # Calculating the correction factor

"""#Evaluating the model


"""

for x , _ in data_set:
  res = dot(x, weights)
  print("Input {}: Result_Before_AF {} -> ResultAf {}".format(x[:2], round(res,3), activation_fn(res)))