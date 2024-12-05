import numpy as np

# 5.2
'''
16)

Q:
Fn is the determinant of the 1, 1, -1 tridiagonal matrix of order n

F2 = [[1, 1], [-1, 1]]  F3 = [[1, 1, 0], [-1, 1, 1], [0, -1, 1]]  F4 = [[1, 1, 0, 0],[-1, 1, 1, 0],[0, -1, 1, 1],[0, 0, -1, 1]]

Expand in cofactors to show that Fn = Fn-1 + Fn-2. These determinants are fibonacci numbers 1, 2, 3, 5, 8, 13...
The sequence usually starts 1, 1, 2, 3 ... (with 2 1's) so our Fn is the usual Fn+1. (last clause?)

A:
The 1, 1 cofactor of an n x n matrix is Fn-1. So the 1, 1 cofactor of F4 is F3.

The 1, 2 cofactor of an n x n matrix has a 1 in the first column and Fn-2 in the rest. So the 1, 2 cofactor of F4 is [[1, 0, 0], [-1, 1, 1], [0, -1, 1]]

Multiply by (-1)1+2 and also (-1) from the 1, 2 entry to
find Fn = Fn-1 + Fn-2 (so these determinants are Fibonacci numbers).

'''


'''
32)

Q:
Cofactors of these 1, 3, 1 matrices give the recursion Sn = 3Sn-1 - Sn-2
This recursion produces every second Fibonacci number

S1 = [3]  S2 = [[3,1], [1,3]]  S3 = [[3, 1, 0], [1, 3, 1], [0, 1, 3]]

Show that Sn is the Fibonacci number F2n+2 by proving F2n+2 = 3F2n - F2n-2
Keep using Fibonaccis rule Fk = Fk-1 + Fk-2 starting with k = 2n + 2

'''

'''
33)

The symmetrical Pascal matrices have determinant 1.  If I subtract 1 from the n,n entry why does the determinant become 0?

det([
[1, 1, 1, 1],
[1, 2, 3, 4],
[1, 3, 6, 10],
[1, 4, 10, 20],
]) = 1 (known)

det([
[1, 1, 1, 1],
[1, 2, 3, 4],
[1, 3, 6, 10],
[1, 4, 10, 19],
]) = 0 (to explain)
'''


#5.3

'''
8)

Q:
Find the cofactors of A and multiply A(transpose(C)) to find det A:

A = [
    [1, 1, 4],
    [1, 2, 2],
    [1, 2, 5],
]

C = [
    [6, -3, 0],
    ...
    ...
]

A(transpose(C)) = ?

If you change that 4 to 100, why is det(A) unchanged?

A:

1[
    [2, 2],
    [2, 5],
] - 1[
    [1, 2],
    [1, 5],
] + 4[
    [1, 2],
    [1, 2],
] === 1*(2*5 - 2*2) - 1(1*5 - 1*2) + 4(1*2 - 1*2) === 6 - 3 + 0


the 1, 3 cofactor is 0, so the first multiple doesn't matter
'''



