import numpy as np
import cmath

z = complex('3+4j')
r = abs(z)
ph = cmath.phase(z)
x1 = complex((r**0.5)*cmath.cos(ph/2), (r**0.5)*cmath.sin(ph/2))
print("x1:\n", x1)

x2 = complex((r**0.5)*cmath.cos((ph+2*cmath.pi)/2), (r**0.5)*cmath.sin((ph+2*cmath.pi)/2))
print("\nx2:\n", x2)