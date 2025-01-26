import numpy as np
from sympy import Matrix

# x + 5y = 25
# 2x + y = 32

A = Matrix([
    [1, 5, 25],
    [2, 1, 32]
])

A_rref = A.rref()[0] # return signature is the resulting array and shape in a tuple

print("P3.1\n", A_rref[2], '&', A_rref[5]) # not sure why the index is 1 dimensional


print("P3.7\n", 4)

print("P3.8\n", "C = B**-1")

B = Matrix([
    [1, 3],
    [-2, -1]
])

C = Matrix([
    [3, -5],
    [4, 0]
])

print("P3.33\n", np.matmul(B.inv(), C))


