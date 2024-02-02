import numpy as np

"""
If we consider vectors in algebraic form - through numerical values
their projections, then when summing the vectors, we get a vector whose projections
are equal to the sum of the projections of the terms of the vectors. For a two-dimensional vector it would be
look like this: 

    α = (a_x, a_y),
    β = (b_x, b_y).
Vector sum of vectors:
    (α + β) = (a_x + b_x, a_y + b_y)
    
Example:
    α = (3, 2),
    β = (2, 4).
    (α + β) = (3 + 2, 2 + 4) → (5, 6)
"""

# In Python, the problem of summing vectors is reduced to obtaining the sum
# corresponding arrays:

a = np.array([3, 2])
b = np.array([2, 4])
c = a + b
print("Vector sum:\n", c)