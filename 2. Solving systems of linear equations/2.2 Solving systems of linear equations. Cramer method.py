import numpy as np

"""
Cramer's method is suitable for solving inhomogeneous systems of linear equations.
N.B. The determinant of the main matrix of the system must not be different from zero!
"""

A = np.matrix(' 3 -1 2; 1 4 -1; 2 3 1') # Main matrix of the system with known components of the left side.
B = np.matrix('-4; 10; 8') # Matrix of elements of the right sides.
print("Matrix with know components:\n", A)
print("Matrix with right components:\n", B)

A_det = np.linalg.det(A) # Calculate the determinant of matrix A
print("Determinant of matrix A:\n", A)

X_m = np.matrix(A)
X_m[:, 0] = B # Replacing the first column of matrix x_m with vector B.
print(X_m)

Y_m = np.matrix(A)
Y_m[:, 1] = B
print(Y_m)

Z_m = np.matrix(A)
Z_m[:, 2] = B
print(Z_m)

x = np.linalg.det(X_m) / A_det
y = np.linalg.det(Y_m) / A_det
z = np.linalg.det(Z_m) / A_det
print(x)
print(y)
print(z)