import numpy as np
"""
The system of vectors is called linearly dependent,
if one of the system vectors can be represented as a linear combination
the remaining vectors of the system, and linearly independent - otherwise.

Let's make the following equality:
     a_1 x_1 + a_2 x_2 + ... + a_n x_n = 0.

If such an equality holds for a_1, a_2, …, a_n not all of which are equal to zero,
then such a system of vectors x_1, x_2, ..., x_n is called linearly dependent. Vector
z, which can be represented as the sum of products of vectors and numbers,
is called a linear combination of vectors:

     z = a_1 x_1 + a_2 x_2 + ... + a_n x_n.

In order to determine whether a given system of vectors is linear
dependent, it is necessary to decompose the vectors into components and compose
corresponding system of equations, if it has a non-zero solution, then such
the system of vectors is linearly dependent.

Example:

     x_1 = (1, 1, -2),
     x_2 = (-1, 3, 1),
     x_3 = (2, 2, -4).
    
It is necessary to determine whether it is linearly dependent.

     a_1 + a_2 + 2 ∙ a_3 = 0
     a_1 + 3 ∙ a_2 + 2 ∙ a_3 = 0
     2 ∙ a_1 + a_2 - 4 ∙a_3 = 0

The resulting system is homogeneous. So that she can have the only thing
(zero) solution, it is necessary that its rank coincides with the number of unknowns.
The rank of the main matrix of the system is two, and the number of unknowns is three,
Therefore, the system of equations has at least one non-zero solution, this is
means that the system of vectors is dependent.

In the case when the number of equations is equal to the number of unknowns, to determine the number
solutions can be guided by the determinant of the main matrix of the system. If
it is equal to zero, then the system has an infinite number of solutions if it is different from
zero, then it has one (zero) solution. The determinant of our main matrix
system is equal to zero, which once again confirms the conclusion that the given system
vectors are linearly dependent.
"""

A = np.matrix ('1 -1 2; 1 3 2; -2 1 -4')
print (np.linalg.det(A))
print (np.linalg.matrix_rank(A))