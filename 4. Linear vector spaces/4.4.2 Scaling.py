import numpy as np
"""
The matrix that performs the scaling of the vector has the following form:
    k 0 0 0 0
A = 0 k 0 0 0
    ......... .
    0 0 0 0 k
In this form, the vector scale will be changed by a given coefficient for each
from the coordinate axes.

If you need to change the scale only in selected directions, then set
coefficients at the required positions of the main diagonal, assign the rest
value 1. For example, for a space with a basis for scaling
in the direction of the vector, you can use the following matrix:
    1 0 0
A = 0 k 0 .
    0 0 1
    
Construct an operator that doubles the coordinates of the vector, its matrix
will look like:
       (2 0)
A_m1 = (0 2).

Apply this operator to a vector:
    z = (2 1)^T
    f(z) = A_m1 ×  z = (4 2)^T.
    
Let's consider another example: along the abscissa axis we reduce the vector by half, 
and along the ordinate axis we increase it by three times:
       (0.5 0)
A_m2 = (0   3)

Then the result of applying this vector to the vector z we already know will be
look like this:
f(z) = A_m2 × z = (1 3)^T.
"""
# Operator that doubles the coordinates of a vector, its matrix
# will look like
x = np.array([2, 1])
A_m1 = np.array([[2, 0], [0, 2]])

f = lambda A, x: np.dot(A, x.T)

# Apply operator to a vector
print("f(z) = A_m1 × z = :\n", f(A_m1, x))
# Another example, along the abscissa axis we will reduce the vector by half, and along the axis
# increase the ordinate by three times
A_m2 = np.array([[0.5, 0], [0, 3]])
print("f(z) = A_m2 × z = :\n", f(A_m2, x))
