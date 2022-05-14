from sympy import *

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
