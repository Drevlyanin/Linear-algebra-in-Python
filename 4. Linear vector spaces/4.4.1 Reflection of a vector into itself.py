import numpy as np
"""
Let's start with the simplest linear operator, which takes a vector to itself
    x = (1 2)^T
    
The linear operator matrix reflecting a vector onto itself has the following
view:
    (1 0)
A = (0 1)

Calculate the result of applying the given linear operator
                    (1 0)
x' = f(x) = A ∙ x = (0 1) × (2 1)^T = (2 1)^T.
"""
# Create a vector and matrix of a linear operator:
x = np.array([2, 1])
A = np.array([[1, 0], [0, 1]])
print(A)

# Let's create a function that will implement linear reflection. This
# We will use the function in the following examples:
f = lambda A, x: np.dot(A, x.T)
# Carry out a linear transformation:
print("Reflection of a vector into itself:\n", f(A, x))
