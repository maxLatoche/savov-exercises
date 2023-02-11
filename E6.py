import numpy as np
import sympy as sp

print('E6.1a\n')

l = sp.Symbol('λ')

A = sp.Matrix([
    [10 - l, -9],
    [4, -2 - l],
])

characteristic_polynomial = sp.factor(A.det())

print(characteristic_polynomial, sp.roots(characteristic_polynomial))
print('\n')

print('E6.1b\n')

A = sp.Matrix([
    [1 - l, 2],
    [4, 3 - l]
])

characteristic_polynomial = A.det()

print(characteristic_polynomial, sp.roots(characteristic_polynomial))
print('\n')

print('E6.1c\n')

A = sp.Matrix([
    [0 - l, 3],
    [7, 0 - l]
])

characteristic_polynomial = sp.factor(A.det())
print(characteristic_polynomial, sp.roots(characteristic_polynomial))
print('\n')

print('E6.1d\n')


A = sp.Matrix([
    [0 - l, 0],
    [0, 0 - l]
])
characteristic_polynomial = sp.factor(A.det())
print(characteristic_polynomial, sp.roots(characteristic_polynomial))
print('\n')


print('E6.1d\n')

A = sp.Matrix([
    [1 - l, 0],
    [0, 1 - l]
])

characteristic_polynomial = sp.factor(A.det())
print(characteristic_polynomial, sp.roots(characteristic_polynomial))
print('\n')


print('E6.11\n', )
print('a 2x2 upper triangular matrix would be:\n')
print([
    [1, 1],
    [0, 1],
])
print('so the basis would be 3 2x2 vectors\n')
print([
    [1, 0],
    [0, 0]
])
print([
    [0, 1],
    [0, 0]
])
print([
    [0, 0],
    [0, 1]
])

print('normally a 2x2 matrix would have 4 basis vectors, but if we know it\'s an upper triangular matrix we can skip one of them')

print('\n')

# Gram-schmidt
print('E6.15\n', )

# A is A and not a because E6.15 is looking for an orthogonal vector, not an orthonormal vector
A = sp.Matrix([4, 2])
b = sp.Matrix([1, 3])

# A = sp.Matrix.hstack(v1, v2) <-- this is wrong for this problem, but useful for remembering how to build arrays from vectors
# print('A', A)
# print('A', A.inv())
# print('A', A*A.inv())

# Ax = b
# becomes
# x = (A.Tb/A.TA)A
print(b - (A.T.dot(b)/A.T.dot(A))*A)

print('\n')
# I've worked out the logic so the answer is correct by hand
# why is the result of i / a.norm() sqrt(2)/2 instead of 1/sqrt(2)?
# A: sqrt(2)/2 and 1/sqrt(2) are equivalent expressions and represent the same value, but they are represented differently in SymPy because of the way it simplifies fractions.
# In SymPy, the sqrt function returns a symbolic square root, which is not necessarily simplified. When you divide a value by sqrt(2), SymPy will not automatically simplify the fraction to 1/sqrt(2).
# sqrt(2)/sqrt(2) * 1/sqrt(2) == sqrt(2)/sqrt(2)sqrt(2) == sqrt(2)/2
print('E6.16\n')

a = sp.Matrix([1, 1, 0])
b = sp.Matrix([1, 0, 1])
c = sp.Matrix([0, 1, 1])

# A = a.applyfunc(lambda i: i/a.norm())
# A = a.multiply(1/a.norm())
A = a/sp.sqrt(a.dot(a))
ortho_2 = (b - (A.T.dot(b)/A.T.dot(A))*A)
B = ortho_2/ortho_2.norm()
ortho_3 = (c - (A.T.dot(c)/A.T.dot(A))*A - (B.T.dot(c)/B.T.dot(B))*B)
C = ortho_3/ortho_3.norm()


print(A, B, C)



