import numpy as np
"""
When raising a complex number to a power, it is convenient to work with
trigonometric form of writing a number, this will allow you to use the formula
Moivre:
    [r (cos φ + i sin φ)]^n = r^n (cos nφ + i sin nφ)
"""
z = complex('1+2j')

print("Exponentiation of a complex number:\n", z**2
)