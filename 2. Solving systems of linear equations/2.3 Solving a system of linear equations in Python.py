import numpy as np

"""
The Numpi library has a separate method that helps solve systems of linear equations.
"""

A = np.matrix('3 -1 2; 1 4 -1; 2 3 1') # Main matrix of the system with known components of the left side.
B = np.matrix('-4; 10; 8') # Matrix of elements of the right sides.
print("Matrix with know components:\n", A)
print("Matrix with right components:\n", B)

# To solve the system, we will use the solve() method from the linalg package:

X = np.linalg.solve(A, B)
print("Matrix of unknowns:\n", X)