'''
5.2

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