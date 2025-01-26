import sympy as sp
import numpy as np

# E7.6
a = np.array([
    [0,1,0],
    [0,0,1],
    [1,1,0],
])

b = np.array([
    [0,1,0],
    [0,1,1],
    [0,0,0],
])

c = np.array([
    [0,1,1],
    [1,0,1],
    [1,1,0],
])

print('E7.6a\n', a)
print('E7.6b\n', b)
print('E7.6c\n', c)

# E7.7
a_connectivity_graph = np.add(np.add(np.identity(3), a), np.linalg.matrix_power(a, 2))
b_connectivity_graph = np.add(np.add(np.identity(3), b), np.linalg.matrix_power(b, 2))
c_connectivity_graph = np.add(np.add(np.identity(3), c), np.linalg.matrix_power(c, 2))
print('E7.7a\n', a_connectivity_graph[0, 2])
print('E7.7b\n', b_connectivity_graph[0, 2])
print('E7.7c\n', c_connectivity_graph[0, 2])


print('E7.10\n')

A = np.matrix([
    [8],
    [16],
    [24],
    [32],
    [40],
])

b = np.matrix([
    [4],
    [9],
    [13],
    [17],
    [20],
])

# m = A+.b

print('lin alg solution', np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(A), A)), np.transpose(A)), b))

A_prime = np.matrix([
    [1, 8],
    [1, 16],
    [1, 24],
    [1, 32],
    [1, 40],
])

print('affine solution', np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(A_prime), A_prime)), np.transpose(A_prime)), b))

print('\n')
print('E7.10\n')

A = sp.Matrix([[105, 113, 125, 137, 141, 153]]).T
b = sp.Matrix([[45, 63, 86, 118, 112, 169]]).T

m = sp.N((A.T*A).inv()*A.T*b)

# e is an array of all of the differences between the slope and the actual values
e = A*m - b

# squared error can be found by squaring the length of the error vector
# ||e||**2
# but it's tricky because the length is the square root of the inner product
# it looks funny to square root then square the result but I'm leaving both steps to make it clear
# what's happening, that step could be optimized away by canceling both operations
result = (sp.sqrt(e.T*e)**2)[0] # result == 4704.62

# OR, you can use the built in matrix.norm() to get the length of the vector before squaring it
print(e.norm()**2)
