import numpy as np
"""
When obtaining the difference of complex numbers, subtracting real and imaginary
parts are produced separately:
    z = a + ib,
    x = c + ib,
    z + x = (a - c) + i(b - d)
"""
z = complex('5+3j')
x = complex('2+4j')

print("Subtracting Complex Numbers:\n", z - x)