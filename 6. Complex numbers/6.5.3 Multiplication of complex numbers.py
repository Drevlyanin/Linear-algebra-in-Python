import numpy as np
"""
Multiplication of complex numbers. It is performed using algebraic
rules for multiplying sums in brackets:
    z = a + ib,
    x = c + ib,
    z × x = (a + ib) × (c + id) = a × c + i(a × d) + i(b × c) + i^2(b × d) = 
    (a × c - b × d) + i(a × d + b × c).
"""
z = complex('5+3j')
x = complex('2+4j')

print("Multiplication of complex numbers:\n", z * x)