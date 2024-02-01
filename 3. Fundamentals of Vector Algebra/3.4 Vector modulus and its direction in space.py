import numpy as np
"""
The modulus of a vector is equal to the square root of the sum of the squares of its coordinates:
    α = (a_x, a_y, a_z),
    |α| = √(a_x^2 + a_y^2 + a_z^2).
The direction of the vector is determined by the cosines of the angles between the vector and the axes
coordinates:
α - angle between α vector and axisO_x.
β - angle between α vector and axis O_y.
γ - angle between α vector and axis O_z.

Direction vectors are calculated using the following formulas:
    cos(α) = a_x/|α|,
    cos(β) = a_y/|α|,
    cos(γ) = a_z/|α|.
    
Example:
AB = (6, 7, 2).
Finding the module:
    |AB| = √(a_x^2 + a_y^2 + a_z^2) = √(6^2 + 8^2 +2^2 ≈ 9.434,
    os(α) = a_x/|α| = 6/9.434 ≈ 0.636,
    cos(β) = a_y/|α| = 7/9.434 ≈ 0.742,
    cos(γ) = a_z/|α| = 2/9.434 ≈ 0.212.
"""
AB = np.array([6, 7, 2]) # Create vector AB.
module_AB = np.linalg.norm(AB) # Calculate the module of the vector AB
print("Module of the vector AB:\n", module_AB)

# Creating functions to calculate cosines.
cos_x = lambda a: a[0] / np.linalg.norm(a) # cos(α) = a_x/|α|.
cos_y = lambda a: a[1] / np.linalg.norm(a) # cos(β) = a_y/|α|.
cos_z = lambda a: a[2] / np.linalg.norm(a) # cos(γ) = a_z/|α|.

# Create function to get the cosine valuesю
vect_cos = lambda a: [a[i] / np.linalg.norm(a) for i in range(len(a))]
vect_cos(AB)

print("Direction cosines:\n", vect_cos(AB))
