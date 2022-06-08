
print('E4.12a\n', True)
print('E4.12b\n', True)
print('E4.12c\n', True)
print('E4.12d\n', False)
print('E4.12e\n', True)

A = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
]

# all answers for 4.13 refer to dimensions
# nullity(M) == dim(nullspace(M))

# A**mxn === A**3x4
# to calculate null space, rank(A) + nullity(A) = n
# to calculate left null space dim(rowspace(A)) + nullity(A) = n
print('E4.13A\n', 'rank', 3,'\nrow space', 3, '\ncolumn space', 3, '\nnull space', 1,'\nleft null space', 0, '\n')

B = [
    [1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
]
print('E4.13B\n', 'rank', 3,'\nrow space', 3, '\ncolumn space', 3, '\nnullspace', 2,'\nleft null space', 0, '\n')

C = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
print('E4.13C\n', 'rank', 0,'\nrow space', 0, '\ncolumn space', 0, '\nnullspace', 0,'\nleft null space', 0, '\n')
