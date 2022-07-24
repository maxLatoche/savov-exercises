# Fundamental Spaces

Lets start with some data represented in a 3 dimensional space by a matrix.

Here is the visualization of the static state of the matrix A.  It's probably easiest to think of this data as a 3D representation of space, but it could represent a financial model, data in a computer file, or many other use cases.

Now lets say some motion is applied to this static 3D state.  In the example of the financial model, maybe it's when some new asset or liability gets added to the system. For the computer file, maybe the user updated the file in the GUI and we need to update the data on the disk.

We can operate on this data in a few different ways.  If we want to apply the existing data as a transformation to some vector we can multiply the Matrix from the right by the vector (Av), AKA matrix-vector multiplication, AKA inner product.  This will give a new vector, w.


A = Matrix([
    [4, 1, 2],
    [4, 3, 0],
    [1, 2, 4],
])

v = Matrix([
    [1],
    [1],
    [1]
])

Av = w

w === [
    [7],
    [7],
    [7],
]

If we start with the vector v (the unit vector in this example), we'd represent that geometrically like this. (unit_vector.png)

Now lets say that some forces are exerted on that vector, those are represented by our Matrix, A. (forces_exerted.png).

The resulting vector will be the combination of matrix (which is essentially a list of vectors), and the original vector.  (matrix-vector1.gif)

You can see the effect of only applying certain columns of the matrix to the original vector. (matrix-vector2-4)

Interestingly, when negative vectors are operated on my the same matrix they behave in similar ways but in the opposite direction.  (matrix-vector5-8)

In all of these examples, what we're solving for is the domain of __column space__, which are all of the possible outputs when multiplying the matrix from the right. {w is a vector of real numbers of __m__ dimensions | A is a matrix of dimensions __m__ x __n__ w = Av when v is a vector of real numbers of n dimensions}

Left multiplication

We can think of left multiplication by M as right multiplication by M-transpose.  --Explain why.

Is a vector suitable for multiplying from the right or left?  For a matrix with dimensions __m__ x __n__, a vector must have __m__ columns to multiply from the left and __n__ rows to multiply from the right.





-------
## column space
Any time you multiply a matrix by a vector _the result will fall ("land") somewhere within the column space_

(for orthogonality/gram-schmidt)
Ax = b might not have a solution.  If b is not in the column space of a x does not exist!  You can pick something close though, that lies on the same plane as b (call it p), and calculate what the projection of A onto p is.

If b is the basis that we want to convert to orthonormal, it lies outside of the desired (orthonormal) plane.





We can represent any matrix A as a vector of coefficients _with respect to the basis_ B. (more on p300)

projection matrix 2 extremes
b is in column space Pb = b
bperp is in column space Pb = 0 (null space)


basis functions vs basis vectors

for a polynomial:
```
b_0(x) = 1
b_1(x) = x
b_2(x) = x**2
b_n(x) = x**n
```

where a basis _vector_ might be
```
x_hat = [1, 0]
y_hat = [0, 1]
```

The coefficients of the polynomial then form the coordinates that are projected onto the current space.  (Any given polynomial is finite, but there exist infinite possibilities for how large the abstract space of a polynomial is)

```
x**2 + 3 === [
    [3],
    [1],
]
5x**4 + 3x**2 + 3 === [
    [3],
    [3],
    [0],
    [5],
]
2x**9 + x**7 + x**6 === [
    [0],
    [0],
    [0],
    [0],
    [0],
    [1],
    [1],
    [0],
    [2],
]
```
