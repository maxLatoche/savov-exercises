# Eigenvectors/EigenValues

Think through `Ax = λx`:

When the matrix A has the vector x applied to it (remember the motion created by right side matrix multiplication), the result is the same as if x was scaled by the eigenvalue.

Another way to think of it is that the Projection matrix can scale x, but it always lies on the same plane after the projection.

To find the eigenvalue of a matrix, find the determinant of the formula A - λ𝟙, which, with the λ variables in place, will give a quadratic equation.  Solving for the roots of the quadratic equation will give the eigenvalues, λ.

Then, substitue the matrix for one whose eigenvalues are removed, and solve for the vectors that take the transformation in question to the null space.

(A - λ𝟙)x1 = 0

Rotation matrix has imaginary eigenvalues (asymmetric matrices do).  Think of the graphic representation of an eigenvector as a stable vector, and how every single vector rotates in a rotation matrix. -- what is the utility of the imaginary eigenvalue?

triangular matrix has eigenvalues on the diagonal
-- det(A - λ𝟙) = 0
-- the determinant of A - λ𝟙 is the product of the diagonal values: det(A - λ𝟙) = (a11 - λ)(a22 - λ)...(ann - λ)
-- if both of the above are true, then each entry on the diagonal must equal λ

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
# (1 - λ)(6 - 3λ - 2λ + λ^2)
# (1 - λ)(6 - 5λ + λ^2)
# 6 - 5λ + λ^2 - 6λ + 5λ^2 - λ^3
# -λ^3 + 6λ^2 - 11λ + 6
#
# 2(0*(2 - λ) - (0 * 2))
# 0
#
# 0(...)
# 0
#
# (-λ^3 + 6λ^2 - 11λ + 6) - 0 + 0
# roots are 1, 2, 3

# To find the eigenvectors, find the null space for different eigenvalues

# (A - 3𝟙)x = 0

# (A - (2)𝟙)x = 0
# (A - (1)𝟙)x = 0

```
