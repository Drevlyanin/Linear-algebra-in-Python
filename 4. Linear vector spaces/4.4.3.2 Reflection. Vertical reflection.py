import numpy as np

A_vert = np.array([[1, 0], [0, -1]]) # The operator matrix that performs vertical reflection looks like this.
z = np.array([2, 1]) # Take something already familiar to us as a vector.

f = lambda A, x: np.dot(A, x.T)

print("f(z) = A_vert × z =:\n", f(A_vert, z))
