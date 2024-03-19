import numpy as np
import scipy.linalg as la

"""
LU decomposition is used to represent a matrix as a product of two
matrices: - lower triangular matrix and - upper triangular matrix:
    A = LU.
The matrix A has all elements of the main diagonal equal to one. Matrix A can be
represented as a LU decomposition if all the main diagonal minors are not
degenerate (non-zero).
This type of decomposition is used for:
• solving systems of linear equations;
• inverse matrix calculations;
• calculation of the determinant.
Let's consider a numerical example - expansion
"""
# Create LU-decomposition of the following matrix.
A = np.array([[4, 1, 3], [8, 1, 8], [-12, -4, -6]])
print("LU -decomposition of the following matrix:\n", A)

"""
Using elementary transformations we reduce it to the upper triangular
mind. You can read more about this in section “4.4.7 Equivalent
transformations.
"""
R1 = np.array([[1, 0, 0],[2, -1, 0],[3, 0, 1]])
R2 = np.array([[1, 0, 0],[0, 1, 0],[0, 1, 1]])

U = R2.dot(R1.dot(A))
print("\nU :\n", U)

"""
If the product of matrices that perform equivalent
transformations, we select it into a separate matrix and find its inverse, then
this will be the required matrix L.
"""

T = R2.dot(R1)
print("\nT:\n", T)

L = np.linalg.inv(T)
print("\nL:\n", L)

print("\n L × U", L.dot(U))

"""
LU Decomposition can be performed using a special function from the library
scipy, this library must first be installed and imported. Behind
this type of decomposition corresponds to scipy.linalg.lu. As a result, we will get
matrices P, L and U The meaning of matrices L and U remains the same, matrix P is a simple
permutation matrix.
"""

P, L, U = la.lu(A)
print("\nP :\n", P)
print("\nL :\n", L)
print("\nA :\n", A)
print("\nU :\n", U)
print("\nP.dot(L.dot(U) :\n", P.dot(L.dot(U)))