import numpy as np
"""
When multiplying a vector by a number,
all vector components are multiplied by this number.

    α = (a_x, a_y),
    λ × α = (λ × a_x, λ × a_y),

Let's multiply the vector α with coordinates (3, 2) by the number 2:
    α = (3, 2),
    2 × α = (2 × 3, 2 × 2) → (6, 4)
"""

a = np.array([3, 2])
k = 2
c = k * a
print("Vector multiplied by a number:\n", c)
