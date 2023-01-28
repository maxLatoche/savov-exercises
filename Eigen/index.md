# Eigenvectors/EigenValues

Think through `Ax = λx`:

When the matrix A has the vector x applied to it (remember the motion created by right side matrix multiplication), the result is the same as if x was scaled by the eigenvalue.

Another way to think of it is that the Projection matrix can scale x, but it always lies on the same plane after the projection. (I think this is right but not a clear or helpful description?)

Rotation matrix has imaginary eigenvalues (asymmetric matrices do).  Think of the graphic representation of an eigenvector as a stable vector, and how every single vector rotates in a rotation matrix.

triangular matrix has eigenvalues on the diagonal

```py
A = [
    [1, 2, 0],
    [0, 3, 0],
    [2, -4, 2],
]


# Ax = λx

# Ax - λx = 0

# (A - λ𝟙)x = 0

# A - λ𝟙 has to be singular, because if it's not, 0 is the only answer for x

# Singular matrices have a determinant of 0

# det(A - λ𝟙) = 0

# det(A - λ𝟙) = [
#   [1 - λ, 2, 0]
#   [0, 3 - λ, 0],
#   [2, -4, 2 - λ],
# ] =
# (1 - λ)((3 - λ) * (2- λ) - 0*-4)
# (1 - λ)(3(2 - λ) - λ(2 - λ))
# (1 - λ)(6 - 3λ - 2λ - λ^2)
# (6 - 3λ - 2λ - λ^2) - (6λ - 3λ^2 - 2λ^2 - λ^3)
# 6 - 3λ - 2λ - λ^2 - 6λ + 3λ^2 + 2λ^2 + λ^3
# λ^3 + 3λ^2 - 5λ + 6
#
# 2(0*(2 - λ) - (0 * 2))
# 0
#
# 0(...)
# 0






```
