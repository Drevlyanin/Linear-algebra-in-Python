import numpy as np
import math
"""
To solve the problem of parallel vector transfer in three-dimensional space,
we need a 3x3 matrix of the following form:
"""
A_mov = np.array ([[1, 0, 1], [0, 1, 2], [0, 0, 1]])

# Use the vector as an argument
z = np.array([2, 1, 1]) 

f = lambda A, x: np.dot(A, x.T)

print("Axis movement:\nf(z) = A_mov × z =", f(A_mov, z))
