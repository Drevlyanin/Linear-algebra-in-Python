import numpy as np
"""
Let us introduce the concept of linear space. Let us consider such a set, on
which defines the operation of adding elements from this set and multiplying
element of the set by a certain number. Here and below we will use the number
understand a number from the set of real numbers. In this case, the element
resulting from the above addition or multiplication by a number, also
belongs to the multitude.

If a set has the following properties (they are called
axioms of linear space), then such a set is called linear
space. If the elements of such a linear space are
vectors, then such a space is called a linear vector space.
For the purposes of this chapter, a vector will be understood as a row or column of numbers.
"""

# Property 1. The addition of elements of a linear space is commutative. From
# rearrangement of terms does not change the sum:
# a + b = b + a; a, b ∈ X.
a = np.array([[1,2]]).T
b = np.array([[3,4]]).T
L = a + b
R = b + a
print(L)
print(R)

# Property 2. The addition of elements of a linear space is associative. Result
# the summation of a number of elements does not depend on the order of summation:
# a + (b + c) = (a + b) + c; a, b, c ∈ X.
a = np.array([[1,2]]).T
b = np.array([[3,4]]).T
c = np.array([[5,6]]).T
L = a +(b + c)
R = a + b)+ c
print(L)
print(R)

# Property 3. The set contains a zero element for which
# following:
# a + 0 = a; a ∈ X.
a = np.array([[1,2]]).T
z = np.array([[0,0]]).T
L = a + z
R = a
print(L)
print(R)

# Property 4. In a set, for any element there is an inverse
# element: if - is an element of the set, then - is the inverse element
# for , and it is also contained in the set . In this case the equality is fulfilled:
# a + (-a) = 0; a ∈ X
a = np.array([[1,2]]).T
m_a = np.array([[-1,-2]]).T
z = np.array([[0,0]]).T
L = a + m_a
R = z
print(L)
print(R)

# Property 5. The product of the sum of elements from a set by a number is equal to the sum
# products of this number by these elements:
# q ∙ (a + b) = q ∙ a + q ∙b; a,b ∈ X; q ∈ R.
a = np.array([[1, 2]]).T
b = np.array([[3, 4]]).T
k = 2
L = k * (a + b)
R = k * a + k * b
print(L)
print(R)

# Property 6. The product of the sum of numbers and an element of the set is equal to the sum
# products of an element by given numbers:
# (q + p) ∙ a =q ∙ a + p ∙ a; a ∈ X; p, q ∈ R.
a = np.array([[1, 2]]).T
p = 2
q = 3
L = (p + q) * a
R = p * a + q * a
print(L)
print(R)

# Property 7. The product of numbers multiplied by an element from the set is equal to
# the product of one of the numbers and an element multiplied by another number:
# (q ∙ p) ∙a = q ∙ (p ∙ a); a ∈ X; p, q ∈ R.
a = np.array([[1, 2]]).T
p = 2
q = 3
L = (p * q) * a
R = p *(q * a)
print(L)
print(R)

# Property 8. A set contains an identity element for which
# the following equality:
# 1 ∙ a = a; a ∈ X.
a = np.array([[1, 2]]).T
k = 1
L = k * a
R = a
print(L)
print(R)
