import numpy as np
"""
Solve the problem of determining the inverse matrix in Python.
To receive feedback matrices we will use the inv() function
"""

A = np.matrix('1. -3.; 2. 5.') # Create matrix A
A_inv = np.linalg.inv(A) # Calculating the matrix inverse (A^-1) of matrix A

print("A^-1 =\n",A_inv)

"""
Property 1. The inverse matrix of the inverse matrix is the original matrix:

(A^-1)^-1 = A
"""

A = np.matrix('1. -3.; 2. 5.')
A_inv = np.linalg.inv(A)
A_inv_inv = np.linalg.inv(A_inv) #Inverting an inverted matrix
print("A =\n", A)
print("(A^-1)^-1 =\n", A_inv_inv)

"""
Property 2. The inverse matrix of a transposed matrix is equal to
transposed matrix from the inverse matrix:

(A^T)^-1=(A^-1)^T
"""

A = np.matrix('1. -3.; 2. 5.')
L = np.linalg.inv(A.T) 
R = (np.linalg.inv(A)).T 
print("(A^T)^-1 =\n", L)
print("A^-1)^T =\n", R)

"""
Property 3. The inverse matrix of the product of matrices is equal to the product of the inverses
matrices:

(A1 x A2)^-1 = A2^-1 x A1^-1
"""

A = np.matrix('1. -3.; 2. 5.')
B = np.matrix('7. 6.; 1. 8.')
L = np.linalg.inv(A.dot(B))
R = np.linalg.inv(B).dot(np.linalg.inv(A))
print("(A1 x A2)^-1 =\n", L)
print("A2^-1 x A1^-1 =\n", R)

 
