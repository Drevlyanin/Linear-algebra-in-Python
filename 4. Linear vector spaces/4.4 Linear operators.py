import numpy as np
"""
Operators, or whatever they are called
called mappings, can be perceived as functions of a special type. Operator
associates a vector from linear space X with some vector y from
linear space Y. In the language of mathematics, this can be written as follows:
     y = f(x), x ∈ X, y ∈ Y.
An operator is called linear if the following equalities hold for it:
     f(X_1 + x_2) = f)x_1) + f(x_2) = y_1 + y_2,
     f(α × x_1) = α × f(x_1) = α × y_1,
where x_1 and x_2 are vectors from the linear space X;
y_1, y_2 - vectors from linear space Y;
α is a number from the set of real numbers R.

You can move from one basis to another by multiplying the first by a special matrix
transition.
In order to define a linear operator f, which transforms a vector from a linear
space X with basis (a_1, a_2,..., a_n), into linear space Y with basis
(b_1, b_2, ..., b_m) it is enough to specify the images f(a_1), f(a_2) ..., f(a_n), which translate
X basis to Y basis.

The vector, if represented as a linear combination of basis vectors, will be
look like this:
     x = x_1 a_1 + x_2 a_2 + ... + x_n a_n
Then the mapping from vector to vector space will be represented by
in the following way:
      f(x) = x_1 f(a_1) + x_2 f(a_2) + ... + x_n f(a_n).
Mapping linear space basis vectors to basis vectors
linear space we already know how to construct:
    f(a_1) = c_11 b_1 + c_21 b_2 + ... + c_m1 b_m
    f(a_2) = c_12 b_1 + c_22 b_2 + ... + c_m2 b_m,
    ...      ...  ...   ...  ...   ...   ...  ...
    f(a_n) = c_1n b_1 + c_2n b_2 + ... + c_mn b_m
    
The matrix C_ba is called the matrix of the linear operator f. Unlike the matrix
transition, which is square, the linear operator matrix is defined
the dimension of the spaces that this operator connects.

In what follows we will be of interest to linear operators, which
map linear space onto itself - the case when X = Y. Matrices
such operators are square.
"""
# In Python this task is solved quite simply. In order for the solution to be
# more beautiful, create a special function that will implement
# given display.

f  = lambda x: np.dot(np.array([[1, 2], [0, 1]]), x.T)
x = np.array ([1, 2])
x_ = f(x)
print(x_)

"""
Thus, we find that in order to fulfill certain
transforming with a vector you need to multiply its matrix with a linear operator.
The composition of the matrix determines the type of transformation: reflection, scaling,
turn, etc. Let's look at examples of different types of transformations.
"""
