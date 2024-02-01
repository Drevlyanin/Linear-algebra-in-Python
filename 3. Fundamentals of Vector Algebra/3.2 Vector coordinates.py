import numpy as np
"""
The coordinates of a vector are its projections on the coordinate axes:
α = (a_x, a_y, a_z),
    pr_ox α = a_x,
    pr_oy α = a_y,
    pr_oz α = a_z.
 
If the coordinates of the starting and ending points are known,
then the coordinates of the vector are determined as follows:
    a_x = x_2 - x_1,
    a_y = y_2 - y_1,
    a_z = z_2- z_1.
 
Consider a vector whose initial point has coordinates A(1,2,3),
final - B(7,9,5). Then the vector AB, expressed in terms of the coordinates of the projections onto
coordinate axes will look like this:
    A(1, 2, 3),
    B(7, 9, 5),
    AB = (7 - 1, 9 - 2, 5 - 3) → AB = (6, 7, 2).
    
Now let's solve this problem in Python. As mentioned above, a vector can
be specified through the coordinates of its beginning and end, in Python for this we will
use Numpy arrays. Let's set these points as variables:
"""

A = np.array([1, 2, 3]) # Define vector A with coordinates (1, 2, 3)
print ("Vector A:\n", A)

B = np.array ([3, 5, 2]) # Define vector B with coordinates (3, 5, 2)
print("Vector B:\n", B)

AB = B - A # Calculate the difference between vectors B and A (vector AB)
print ("Vector AB:\n", AB)
