import numpy as np

"""
Ran matrix, an important numerical characteristic. The rank of a matrix is the maximum number of linearly independent rows (columns) of the matrix.
Linear independence means that rows (columns) cannot be expressed linearly in terms of other rows (columns).
The rank of a matrix can be found through its minors; it is equal to the largest minor order that is not zero.
The existence of a rank of a matrix does not depend on whether it is square or not.
"""
 
m_eye = np.eye(4) # Create an identity matrix.
print("Identity matrix =\n", m_eye)

"""
The rank of such a matrix is equal to the number of its columns (or rows), in our case the rank
will be equal to four, to calculate it in Python we will use the function
matrix_rank():
"""
rank = np.linalg.matrix_rank(m_eye)
print("Matrix rank =", rank)

"""
If we set the element in the lower right corner to zero, then the rank becomes
three:
"""
m_eye[3] [3] = 0
print("Matrix rank =\n", m_eye)
rank = np.linalg.matrix_rank(m_eye)
print("Matrix rank =\n", rank)