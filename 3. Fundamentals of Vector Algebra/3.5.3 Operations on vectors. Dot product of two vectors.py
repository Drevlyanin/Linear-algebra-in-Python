import numpy as np

"""
The scalar product of two vectors α and β is a number equal to
the product of the moduli of these vectors and the cosine of the angle between them:
    α × β = |α| × |β| × cos(φ)
    
The scalar product can be expressed in terms of vector coordinates:
    α = (a_x, a_y, a_z),
    β = (b_x, b_y), b_z).
    
    α × β = a_x × b_x + a_y × b_y + a_z × b_z.
    
If we transpose one of the vectors, then the scalar product can be
express through the operation of matrix multiplication:

B = (b_x, b_y, b_z).
α × β = (a_x a_y a_z) × B^T = a_x × b_x + a_y × b_y + a_z × b_z.

Example:
     α = (2, 7, 3),
     β = (5, 9, 3).
Find their scalar product:
    α × β = 2 × 5 + 7 × 9 + 3 × 3 = 82.
"""
# Create two matrices
a = np.array([2, 7, 3])
b = np.array([5, 9, 3])

# Find their scalar product
ab_scal = a.dot(b.T)
print("Dot product of vectors:\n", ab_scal)
