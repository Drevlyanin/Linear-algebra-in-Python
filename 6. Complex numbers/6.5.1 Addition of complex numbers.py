import numpy as np
import cmath
"""
When adding complex numbers, the real and imaginary parts are added according to
separately:
    z = a + ib,
    x = c + ib,
    z + x = (a + c) + i(b + d)
"""
z = complex('1+2j')
x = complex('3+4j')

print("Addition of complex numbers:\n", z + x)