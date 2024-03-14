import numpy as np
"""
        (-1 0)
A_hor = (0  1)
When multiplied by such a matrix, the vector is mirrored relative to the axis
ordinate
Take something already familiar to us as a vector:
z = (2 1)^T

f(z) = A_hor × z = (-2 1)^T.
"""
z = np.array([2, 1])
A_hor = np.array([[-1, 0], [0, 1]])
f = lambda A, x: np.dot(A, x.T)

print("f(z) = A_hor × z =:\n", f(A_hor, z))
