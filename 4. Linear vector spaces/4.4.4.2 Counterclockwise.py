import numpy as np
import math
"""
To rotate counterclockwise by an angle, we slightly modify the matrix from
previous paragraph.
"""

# Use the vector as an argument
z = np.array([2, 1]) 
# Construct a matrix for the operator that rotates the vector by 60 degrees against clockwise
A_rot_not_cl = np.array([[math.cos(math.pi/3), (-1)*math.sin(math.pi/3)], [math.sin(math.pi/3), math.cos(math.pi/3)]])

f = lambda A, x: np.dot(A, x.T)

print("Counterclockwise:\nf(z) = A_rot_not_cl × z =", f(A_rot_not_cl, z))
