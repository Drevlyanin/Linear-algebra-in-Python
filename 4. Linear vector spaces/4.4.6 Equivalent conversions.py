import numpy as np

"""
We analyzed the Gauss method for solving systems of linear
algebraic equations. Our goal was to bring the original system
equations to triangular form. The essence of this work was that with
with the original system, we sequentially carried out a number of transformations, while
the system before and after these transformations had the same solution. Such
transformations are called equivalent.
There are three types of equivalent transformations:
    1. Rearrangement of two equations in the system.
    2. Multiplying one of the equations of the system by a number that is not equal to zero.
    3. Adding one equation to another, multiplied by a number.
It is convenient to apply equivalent transformations in matrix form.
First, let's do this manually.
"""
# Create the initial extended matrix systems:
A = np.array([[3, -1, 2, -4], [1, 4, -1, 10], [2, 3, 1, 8]])
print("Extended system matrix:\n", A)

# Build matrices to perform equivalent transformations:
R1 = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
R2 = np.array([[1, 0, 0], [0.5, -1, 0], [1.5, 0, -1]])
R3 = np.array([[1, 0, 0], [0, 1, 0], [0, -2.2, -1]])
print("Matrices for performing equivalent transformations:\n R1 =\n", R1, "\n R2 =\n", R2, "\n R3 =\n", R3)

print("Matrix multiplications:\n", R3.dot(R2.dot(R1.dot(A))))

"""
If this question is translated into the language of linear operators, then we can do
the following interesting observation: by specifying the multiplication by the corresponding matrix
like a linear display, we can get the finished result through composition
linear operators - that is, their sequential application to the result
obtained at the previous stage. Let's look at this with an example. Let's create three
linear operator:
"""
def f1(x):
    R1 = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    return R1.dot(x)
    
def f2(x):
    R2 = np.array([[1, 0, 0], [0.5, -1, 0], [1.5, 0, -1]])
    return R2.dot(x)
def f3(x):
    R3 = np.array([[1, 0, 0], [0, 1, 0], [0, -2.2, -1]])
    return R3.dot(x)
# Apply them sequentially to the given matrix:
print("Apply them sequentially to the given matrix:\n", f3(f2(f1(A))))