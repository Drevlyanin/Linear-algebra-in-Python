import numpy as np

"""
When subtracting, the resulting vector goes from the end of the second vector to the end
first vector. For the two-dimensional case with vectors:
    α = (a_x, a_y),
    β = (b_x, b_y).

The difference vector is defined as follows:

    (α - β) = (a_x - b_x, a_y - b_y).
    
    Пример:
    α = (3, 2),
    β = (2, 4).
    (α - β) = (3 - 2, 2 - 4) → (1, -2)
"""
# In Python, the task of subtracting vectors comes down to getting the difference
# corresponding arrays:

a = np.array([3, 2])
b = np.array([2, 4])
c = a - b
print("Vector difference:\n", c)