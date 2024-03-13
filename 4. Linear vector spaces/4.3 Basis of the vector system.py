import numpy as np
"""
For a system of vectors, we can identify the maximum linearly independent
subsystem, which is characterized by the fact that if you add another vector to it
(from a given system), then it will become linearly dependent.

From the example given in Section 4.2, the maximum linearly independent
the vector system looks like this

     x_1 = (1, 1, -2), x2 = (-1, 3, 1),
or like this:
     x_1 = (2, 2, -4), x_2 = (-1, 3, 1).
At the same time, adding a vector from a given system to any of these subsystems
will lead to the resulting system being linearly dependent.

For a given finite linear system of vectors, a basis is any of its
maximum linearly independent subsystem, and the number of vectors in the basis
is called the rank of the vector system. If you, using the given vectors, construct
matrix, then its rank will be equal to the rank of the basis of the original system of vectors. Basis
of a finite linear system is a set of vectors through which there can be
any vector of the system is expressed. In other words, any vector from a linear
system is a linear combination of basis vectors.

The basis of a linear space is an ordered independent system
vectors, through which any vector of this space can be expressed.

The number of vectors in the basis is called the dimension of space. Number
There are infinitely different bases of linear space. When we say that
space is three-dimensional - this means that its basis consists of three vectors, and
any point (vector) in space can be defined through the basis vector

Most often, in practice, one has to encounter a natural basis.
It looks like this:

     e_1 = (1, 0, 0, ..., 0)T,
     e_2 = (0, 1, 0, ..., 0)T,
                     ...,
     e_n = (1, 0, 0, ..., 0)T.
    
It is very easy to express through a natural basis any vector of a given linear
space. In this case, the vector coordinates will be coefficients
corresponding linear combination. Consider a vector
     z = (z_1, z_2, ..., z_n)T.
Let's construct its linear combination, expressed through a natural basis:
     z = z_1e_1 + z_2e_2 + ... + z_ne_n.
As noted earlier, the number of bases of a linear space is infinite,
this means that in addition to the natural basis, there are others. All bases
linear space are interconnected. We can go from one
basis to another if necessary. Let's look at this question in more detail.

  Let us select two bases in our linear space:
     a = (a_1, a_2, ..., a_n),
     b = (b_1, b_2, ..., b_n).
Since every vector of space can be expressed in terms of basis vectors, then
We express each vector in terms of vector a, and we obtain the following system:

    b_1 = k_11a_1 + k21a2 + ... + k_n1an
    b_2 = k_12a_1 + k22a2 + ... + k_n2an.
    ...
    b_n = k_1na_1 + k2na2 + ... + k_nnan
    
We get the same result if we perform matrix multiplication:
    b = a × K,
where a and b are the vectors specified above, and a is the transition matrix, which has
the following form:
    k_11 k_12 ... k_1n
K = k_21 k_22 ... k_2m.
    ...  ...  ... ...
    k_n1 k_n2 ... k_nn
    
Numerical example:

                |i j k|      |7 3|      |2 3|      |2 7|
    c = a × b = |2 7 3|= i × |9 3| - j ×|5 3| + k ×|5 9| = -6 × i + 9 × j -17 ×
                |5 9 3|
                
Vectors i, j, k, in this case, are the natural basis of the three-dimensional
space, they have coordinates:
     i = (1, 0, 0),
     j = (0, 1, 0),
     k = (0, 0, 1).
These vectors are also called orth vectors.
"""