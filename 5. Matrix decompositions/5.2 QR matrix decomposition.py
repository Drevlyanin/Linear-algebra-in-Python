import numpy as np

"""
By definition, QR matrix decomposition is a representation of a matrix in the form
product of the orthogonal matrix Q and the upper triangular matrix R. C
We have already encountered the concept of a true triangular matrix earlier. Orthogonal
matrix is a new concept for us, let's analyze it in more detail. Orthogonal
a matrix is a matrix whose transposed matrix is equal to
the inverse of a matrix, the sum of the squares of all elements in a row or column is
one, and the pairwise product of the elements of two rows or columns is equal to zero.

Let's look at a quick way to obtain a QR decomposition of a matrix; for this we will use the np.linalg.qr() function from the Numpy library. As an argument in
This function is passed the original matrix, the result of its work is two
matrices.
"""

# Perform QR decomposition for the following matrix.
A = np.matrix("2 1 3; 0 1 4; 1 3 4")
print("Matrix A:\n", A)

q, r = np.linalg.qr(A)
print("\nq:\n", q,)
print("\nr:\n", r)
