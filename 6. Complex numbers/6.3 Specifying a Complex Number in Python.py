import numpy as np
import cmath
"""
Complex numbers can be specified by a pair (a, b), which immediately leads to the idea
using Python tuples to work with them:
"""
z = (1, 2)
print("Pair (a, b):\n",z)

"""
But in this case you will have to write functions yourself to perform
arithmetic operations with complex numbers. We won't do this
Let's use the complex type instead:
"""
z = complex(1, 2)
print("\ncomplex (a, b):\n",z)

z1 = complex('1+3j')
print("\ncomplex (a, bj):\n", z1)

"""
As you can see, when you print out a number like this, it appears in a familiar
us algebraic form. The real and imaginary parts of a number can be
obtained using special attributes:
"""

print("\nz.real:\n", z.real)
print("\nz.imag:\n", z.imag)

"""
The complex type does not have methods for calculating the module and argument; for this you can
use functions from the cmath module.
The modulus r and argument of the number z created above is defined as follows:
"""
r = cmath.polar(z)[0]
print("\ncmath.polar(z)[0]:\n", r)
f = cmath.phase(z)
print("\ncmath.phase(z):\n", f)