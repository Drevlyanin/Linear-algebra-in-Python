import numpy as np

"""
Mixed product of three vectors (also called vector-scalar)
is defined as follows: two vectors are multiplied vectorially, after which the resulting
the product must be multiplied scalarly by the third vector.

Consider three vectors a, b and c:
    a = (a_x, a_y, a_z),
    β = (b_x, b_y, b_z),
    c = (c_x, c_y, c_z).
    
The mixed product will look like this:

              |a_x a_y a_z|
(a × b) × c = |b_x b_y b_z|.
              |c_x c_y c_z|
"""           
a = [2, 7, 3]
b = [5, 9, 3]
c = [7, 4, 5]

vmp = np.matrix([a, b, c])
print("Mixed product of three vectors:\n", np.linalg.det(vmp))