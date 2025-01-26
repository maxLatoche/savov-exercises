from sympy import *
import numpy as np

# 3.2

A = Matrix([
    [3, 3, 6],
    [2, S(3)/2, 5],
])

B = Matrix([
    [3, 3, 6],
    [2, S(3)/2, 5],
])

# divide the first row by 3 (makes 0, 0 === 1)
B.row_op(0, lambda i, j: i/3)
# yields [[1, 1, 2], [2, 3/2, 5]]

# we want to eliminate the first element in the second row
# map over row 1 and multiply each element by 2/3
# then subtract the result from the second row
reduced_row_one = list(map(lambda i: i*(S(2)/3), A[0:3]))
B.row_op(1, lambda i, j: i-reduced_row_one[j])
# yields [[1, 1, 2], [0, -1/2, 1]]

# now scale row 2 so 1, 1 === 1
B.row_op(1, lambda i, j: i*-2)
# yields [[1, 1, 2], [0, 1, -2]]

# finally, eliminate 0, 1 from the first row
B.row_op(0, lambda i, j: i-B[3:][j])

print('E3.2\n', A.rref(), B)

print('E3.4a\n', 'BA**-1')
print('E3.4a\n', 'C**-1B**-1A**-1ED**-1')
print('E3.4a\n', 'AD**-1')

P_a = [
    [1, 2],
    [3, 4]
]
P_b = [
    [5, 6],
    [7, 8]
]

print('E3.5\n', np.dot(P_a, P_b))

Q_a = [
    [3, 1, 2, 2],
    [0, 2, -2, 1]
]
Q_b = [
    [-2, 3],
    [1, 0],
    [-2, -2],
    [2, 2]
]

print('E3.5\n', np.dot(Q_a, Q_b))

A = [
    [2, 3],
    [5, 6]
]

B = [
    [7, 8],
    [1, 4]
]

C = [
    [-1, 4],
    [2, 1],
    [-1, 2],
]

U = [2, 1]

V = [
    [1],
    [-2]
]

print('E3.6a\n', np.linalg.matrix_power(A, 2))
print('E3.6b\n', np.linalg.matrix_power(B, 2))
print('E3.6c\n', np.matmul(A, B))
print('E3.6d\n', np.matmul(B, A))
# print('E3.6e\n', np.multiply(A, C))
print('E3.6e\n', 'Does not exit, C\'s Y is larger than A\'s X')
print('E3.6f\n', np.matmul(C, A))
print('E3.6g\n', np.matmul(np.matmul(np.matmul(U, A), B), V))

