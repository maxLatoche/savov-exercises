What is the usefulness of the determinant?

## Calculating a determinant is weird.

For larger matrices, when you learn how to compute determinants it seems quite arbitrary.

graphic from page 166

multiply some index by another sub-section of the matrix ...what? why?

It becomes much clearer when your mental starting point is, "how do I find the 'area' of this dataset?".

For a simple 2x2 matrix we're literally getting the area of a rectangle, an elementary length x height.

A simple example, the determinant of the vectors v = [3, 0] and w = [1, 2] (graph here)

Ok, a parallelogram is easy, it's the same area equation as a rectangle, l x h.  So why is the equation for a 2x2 matrix a11a22 - a21a11?

Here is a similar 2x2 matrix, but it does not have parallel sides. (odd2d)
v1 = [3, 1]
v2 = [1, 2]

Lets visualize each half of the equation a11a22 - a21a11.
()

We can apply the same logic to a 3D vector.  A determinant for the vectors
v1 = [4, 0, 2]
v2 = [4, 3, 0]
v3 = [1, 2, 4]










The determinant of the identity matrix 𝐼 is 1.

Once we are working with arrays greater than three dimensions, it can be hard to conceptualize what the determinant represents.  Keeping this fact about the identity matrix in mind can help you orient yourself when considering the deteminant and its relation to the identity, even in an abstract nD space, since the behavior and relationships within the space will be analogous to simpler, geometric spaces.

## Three ways to get the determinant

### Pivot

You can do gaussian elimination and take the multiples of the pivots.

### Brute force

### Cofactor Expansion

cofactors are useful when matrices have many 0s.

## Cramers Rule

for Ax = b, you can solve for x by taking the identity matrix and plugging in the vector x for the column you want to solve for.

once you do something like A[
    [x1, 0, 0],
    [x2, 1, 0],
    [x3, 0, 1]
    ] = [
        [b1, a12, a13],
        [b2, a22, a23],
        [b3, a32, a33],
    ] = B1

then x1 = det(B1) / det(A)

likewise for columns 2 and 3

A[
    [1, x1, 0],
    [0, x2, 0],
    [0, x3, 1]
    ] = [
        [a11, b1, a13],
        [a21, b2, a23],
        [a31, b3, a33],
    ] = B2

then x2 = det(B2) / det(A)

A[
    [1, 0, x1],
    [0, 1, x2],
    [0, 0, x3]
    ] = [
        [a11, a12, b1],
        [a21, a22, b2],
        [a31, a32, b3],
    ] = B1

then x3 = det(B3) / det(A)

up to N -- as long as det(A) !== 0

xn = det(Bn)/det(A)
