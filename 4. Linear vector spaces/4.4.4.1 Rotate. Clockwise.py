import numpy as np
import math
"""
The matrices of operators performing a rotation at a given angle have more
interesting content. Let's consider two linear operators: the first one will be
turn clockwise, the second turn counterclockwise.

To rotate clockwise by angle α, use the matrix operator
of the following form:
"""
# Use the vector as an argument
z = np.array([2, 1]) 
# Build a matrix for the operator that rotates the vector by 45 degrees
A_rot_not_cl= np.array([[math.cos(math.pi/4), math.sin(math.pi/4)],[(-1)*math.sin(math.pi/4), math.cos(math.pi/4)]])

f = lambda A, x: np.dot(A, x.T)

print("Reverse vector\n f(z) = A_hor × z =\n", f(A_rot_not_cl, z))
