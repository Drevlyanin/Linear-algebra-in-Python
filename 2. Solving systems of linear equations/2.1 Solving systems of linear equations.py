import numpy as np
"""
A system of linear equations is a set of two or more linear equations that contain the same variables.
A homogeneous system is a system of linear equations in which all free terms are equal to zero.
An inhomogeneous system is a system of linear equations in which at least one free term is not equal to zero.
Collaborative system - has at least one solution.
An inconsistent system has no solutions.
Let us solve the inhomogeneous system in matrix form:
"""


A = np.matrix('3 -1 2; 1 4 -1; 2 3 1') # Main matrix of the system with known components of the left side.
B = np.matrix('-4; 10; 8') # Matrix of elements of the right sides.
print("Matrix with know components:\n", A)
print("Matrix with right components:\n", B)

A_inv = np.linalg.inv(A) # Calculate the inverse matrix of a matrix with known components of the left side.
print("Invers matrix A:\n", A_inv)

X = A_inv.dot(B) # Multiply A^T matrix by B matrix. 
print("Matrix of unknowns:\n", X)