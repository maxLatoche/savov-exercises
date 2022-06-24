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

