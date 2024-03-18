import numpy as np

"""
If from matrix A we subtract the identity matrix E multiplied by some
variable λ, we obtain a matrix called characteristic
matrix matrix A.
"""
A = np.matrix("1 4 1; 0 2 2 ; 0 0 3")

"""
The determinant of such a matrix will be a polynomial of the nth degree in λ and can
treated as a function:
f(λ) = | A - λE|.

Let's use the capabilities of Python and the Numpy library to calculate roots
characteristic equation of the matrix:
"""
A = np.matrix("1 4 1; 0 2 2 ; 0 0 3")
print("Matrix A:\n", A)

w, v = np.linalg.eig(A)
print("Calculation of the root of the characteristic equation of the matrix:\n", w)