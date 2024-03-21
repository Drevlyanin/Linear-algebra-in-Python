import numpy as np

"""
The essence of the singular decomposition of a matrix is that it can be represented
as a product of three matrices:

    A = UΣT^T.
Where matrix U is orthogonal, Σ - diagonal, T - orthogonal.

Matrix defines
some linear transformation over a vector. Singular decomposition
matrices shows how such a linear operation can be turned into
sequential vector rotation, scaling (stretching or shrinking) and
rotation again
"""

# Perform QR decomposition for the following matrix.
A = np.matrix("1 0 1; 0 1 0; 1 0 1")
print("Matrix A:\n", A)

u, s, v = np.linalg.svd(A)
print("\nu:\n", u)
print("\ns:\n", s)
print("\nv:\n", v)
