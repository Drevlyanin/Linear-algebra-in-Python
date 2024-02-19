import numpy as np

"""
    α × β = |α| × |β| × cos(φ)
The vector product of two vectors α and β is the third vector c = α × β,
which satisfies the following conditions:
    1. Vector c is perpendicular to vectors α and β.
    2. The magnitude of the vector c is determined by the formula:
        |c| = |α × β| = |α|×|β| × sin(φ).
    3. Vectors α, β and c form a right-hand triplet of vectors.
    
The cross product can also be expressed in terms of the coordinates of the multiplied
vectors: 
    α = (a_x, a_y, a_z),
    β = (b_x, b_y, b_z),
    
               | i   j   k |
    c = α × β =|a_x a_y a_z|.
               |b_x b_y b_z|
               
The vector product is equal to the determinant of a matrix composed of identity
orth-vectors and projections of vectors α and β onto these orth-vectors.
"""             
# Define the module.
a = np.array([2, 7, 3])
b = np.array([5, 9, 3])

# Find the cosine of the angle between the vectors by first implementing the corresponding formula.
vect_cos = lambda a, b: a.T.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
print("Cosine distance:\n", vect_cos(a, b))

# Using the resulting function, we find the sine of the angle between the vectors.
vect_sin = lambda a, b: (1 - vect_cos(a, b)**2)**0.5
print("Sine of the angle between vectors:\n", vect_sin(a, b))

# Create a formula for the vector product modulus.
prod_vect = lambda a, b: np.linalg.norm(a)*np.linalg.norm(b)*vect_sin(a, b)
print("Product vector:\n", prod_vect(a, b))