from sympy import *
from sympy.solvers.solveset import linsolve

print('Section 1.2 | Problem 23\n', 'w1/||w||, w2/||w||')

print('Section 1.2 | Problem 28\n', 'Yes.  Think of the 4 quadrants of a plane.  Because vectors need to point in different directions to have negative dot products, 4 vectors in 4 quadrants would be a 0 dot product at least.  But with only three vectors, we just need to pick 3 spaced appropriately.  If you look at the unit circle you can pick (0, 1), (-1/2, √3/2), (-√3/2, -1/2), or any 3 vectors roughly spaced the same amount.')

w1 = [
    1,
    2,
    3,
]

w2 = [
    4,
    5,
    6,
]

w3 = [
    7,
    8,
    9,
]

"""
x1w1 + x2w2 + x3w3 = 0

x11 + x24 + x37 = 0
x12 + x25 + x38 = 0
x13 + x26 + x39 = 0

"""

x, y, z = symbols('x, y, z')
print('!!!', linsolve(
    Matrix((
    [1, 4, 7, 0],
    [2, 5, 8, 0],
    [3, 6, 9, 0],
    )
), (x, y, z)))



print('Section 1.3 | Problem 4\n', '')
