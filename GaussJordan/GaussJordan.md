What we know so far:

1. Linear systems change predictably.  If a we can represent a system like this (render 2D grid), that system could scale (render sheared version) to lots of different permutations (render scaled version), but we can follow a point through all of those permutations if when know how those changes affected a few other points (how many points depends on the number of dimensions, or "rank"). (render 3rd point that moves with the shear or scaled graph)

2. We can represent linear systems with a matrix. (show a matrix and how it plots vector to a grid)

Like a student of language itching to put conjugations to work, or a skier at the top of their first slope, you might be excited about all the things your intuition is telling you we can do with this information.  In theory we can build and understand really complex, cool systems!  But like the speaker or skier, we're going to make _a lot_ of mistakes, and we're going to have to rely on people that are a lot smarter to show us the way.

Lets walk through 4 fundamental operations used to reason about linear systems.

Gauss-Jordan Elimination
If we've got a system of equations and we need to solve for some variables, We can use an _augmented matrix_ and reduce each equation to its simplest form.

We can solve a system without a matrix
2a + 4b = 14
a + 8b = 10

// simplify equation 2
a = 10 - 8b

// plug in the new value of a to system 1
2(10 - 8b) + 4b = 14
20 - 16b + 4b = 14
-12b = -6
12b = 6
b = 1/2

// then solve for a
a + 8 * 1/2 = 10
a + 4 = 10
a = 6


We won't always be so lucky as to have simple, 2 variable systems though.  We might want to solve for many more variables at once. Lets solve that simple equation with Guass-Jordan elimination.

2a + 4b = 14
a + 8b = 10

^ these 2 equations can be put inside an _augmented matrix_, where each column corresponds to an element in the equation.

2a + 4b = 14
a + 8b = 10

becomes

[
    [2, 4, 14],
    [1, 8, 10]
]

You can see how each row corresponds to each coefficient, and the constant value is in the last column.

Every time we operate on one row, it has to be proportional to some scaled version one of the other equations (otherwise this would stop being a linear system).  We're looking for _pivots_ which is the matrix-y way of solving for a variable.  to solve for b, we'll eliminate `a` by scaling the first equation to a value that cancels it out in the second equation.

multiply the first row by 1/2 to get [1, 2, 7]
then subtract it from the second row to get

[
    [2, 4, 14],
    [0, 6, 3]
]

now scale row 2 to get the _pivot_
[0, 6, 3] * 1/6 === [0, 1, 1/2]

do you see it?
[0, 1, 1/2]
0a + 1b = 1/2

We solved for b!

continue these operations on the first row to solve for a.  this is the current state of the matrix.

[
    [2, 4, 14],
    [0, 1, 1/2]
]

So we'll scale row 1 by 1/2 to get our _pivot_ for a

[
    [1, 2, 7],
    [0, 1, 1/2]
]

our last step is eliminate 2, the coefficient for b in the first equation, and we have solved for a!  To do that, multiply the second row by 2 and subtract it from the first.

[
    [1, 0, 6],
    [0, 1, 1/2]
]


We chose a simple equation to get a basic understanding, now give some harder problems a try.

Problem 1 -- TBD

Problem 2 -- TBD
This problem has infinite solutions. (show graph and explain)

Problem 3 -- TBD
this problem has no solution (show graph and explain)

Problem 4 -- TBD
