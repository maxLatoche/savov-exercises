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

'''
27)

Polar coords satisfy x = rcosθ and y = rsinθ.  Polar area is J dr dθ.

J = [
    [δx/δr, δx/δθ],
    [δy/δr, δy/δθ]
] = [
    [cosθ, -rsinθ],
    [sinθ, rcosθ]
]

Note: this is Substituting for x=rcosθ && y=rsinθ, so:
δx/δr === δrcosθ/δr === cosθ,
δx/δθ === δrcosθ/δθ === -rsinθ -- the derivative of sin is cos and vice versa, This negative sign arises because as θ increases, cosθ is decreasing (moving downward on the graph), indicating a negative rate of change.
δy/δr === δrsinθ/δr === sinθ
δy/δθ === δrsinθ/δθ === rcosθ -- Why there’s no sign change: The cosθ is positive in its derivative because sinθ is increasing as you increase θ


The derivative of either x or y with respect to r simply gives a scaling factor, as there is no interaction with -sinθ (which only arises from derivatives with respect to theta. (r is scaling, theta is directional)


A:
the two columns are orthogonal. Their lengths are 1 and r.  thus J = r.

To compute the area of a region in polar coordinates, the integral is
Area=∫∫rdrdθ.

'''

'''
28)

Q: Spherical coordinates ρ (rho, radius), θ (theta, angle from z axis), ɸ (phi, angle from x axis) satisfy
x = ρsinɸcosθ and y = ρsinɸsinθ and z = ρcosɸ.  Find the 3x3 matrix of partial derivatives.  Simplify its determinant to
J = p^2sinɸ.  Then dV in spherical coords is p^2sinɸdpdɸdθ, the volume of an infinitesimal "coordinate box"

A:

J = [
    [δx/δp, δx/δɸ, δx/δθ],
    [δy/δp, δy/δɸ, δy/δθ],
    [δz/δp, δa/δɸ, δz/δθ]
] = [
    [sinɸcosθ, psinɸsinθ, -pcosɸcosθ],
    [sinɸsinθ, psinɸcosθ, psinθcosɸ]
    [cosɸ, 0, -psinɸ]
] (Even without specific values for r,ϕ,θ, this abstract expression describes the sensitivity of x to p, ϕ, and θ)

x = psinɸcosθ
y = psinɸsinθ
z = pcosɸ

δx/δp = p(δ/δp)sinɸcosθ = sinɸcosθ
δx/δɸ = p(δ/δɸ)sinɸcosθ = psinɸsinθ
δx/δθ = p(δ/δθ)sinɸcosθ = -pcosɸcosθ

δy/δp = p(δ/δp)sinɸsinθ = sinɸsinθ
δy/δɸ = p(δ/δɸ)sinɸsinθ = psinɸcosθ
δy/δθ = p(δ/δθ)sinɸsinθ = pcosɸsinθ

δz/δp = p(δ/δp)cosɸ = cosɸ
δz/δɸ = p(δ/δɸ)cosɸ = 0
δz/δθ = p(δ/δθ)cosɸ = -psinɸ

sinɸcosθ(psinɸcosθ(-psinɸ) - 0*psinɸcosθ) - psinɸsinθ(sinɸsinθ(-psinɸ) - pcosɸsinθcosɸ) + -pcosɸcosθ(sinɸsinθ*0 - cosɸpsinɸcosθ)
sinɸcosθ(-p^2sinɸ^2cosθ) - psinɸsinθ(-psinɸ^2sinθ - pcosɸ^2sinθ) + -pcosɸcosθ(-pcosɸsinɸcosθ)

NOTE: the next line was based on a typo that has been corrected, disregard it in the context of the problem but I'm leaving it because
its nice to see how trigometric identities work.
-psinɸ^2sinθ - psinɸcosθcosɸ === -psinɸ(-sinɸsinθ + cosθcosɸ) <-- trigometric identity -sinɸsinθ + cosθcosɸ === cos(θ-ɸ)

we can still factor out the middle, denser minor matrix result
-psinɸ^2sinθ - pcosɸ^2sinθ === -psinθ(sinɸ^2 + cosɸ^2) <-- trigomatric identity sinɸ^2 + cosɸ^2 = 1

-p^2sinɸ^3cosθ^2 - psinɸsinθ(-psinθ) + p^2cosɸ^2sinɸcosθ^2
-p^2sinɸ^3cosθ^2 + p^2sinɸsinθ^2 - p^2cosɸ^2sinɸcosθ^2

factor out p^2 and sinɸ

p^2sinɸ(-sinɸ^2cosθ^2 + sinθ^2 - cosɸ^2cosθ^2)

now trigometric identity sinɸ^2 + cosɸ^2 = 1
-sinɸ^2cosθ^2 - cosɸ^2cosθ^2 === -cosθ^2(sinɸ^2 + cosɸ^2) === -cosθ^2(1)

p^2sinɸ(sinθ^2 - cosθ^2)

now trigometric identity sinθ^2 - cosθ^2 === -cos(2θ)
p^2sinɸ(-cos(2θ))


how does p^2sinɸ(-cos(2θ)) simplify to -p^2sinɸ?

IF THE DETERMINANT IS A PART OF AN INTEGRAL OVER A FULL PERIOD OF θ, -cos(2θ) AVERAGES TO 0 AND THE RESULT WILL DEPEND ONLY ON r^2sinɸ

'''

'''
40)
Q:
suppose A is a 5x5 matrix.  Its entries in row 1 multiply determinants (cofactors) in rows 2-5 to
give the determinant.  Can you guess a "Jacobi formula" for det A using 2x2 determinants from
rows 1-2 times 3x3 determinants from rows 3-5?
Test your formula on the -1,2,-1 tridiagonal matrix that has a determinant = 6
M = [
    [2, -1, 0]
    [-1, 2, -1]
    [0, -1, 2]
]


A:
This is a recursive problem.

D23 === 2*2 - (-1)*(-1) === 4 - 1 === 3
D12 === 2*0 - (-1)*(-1) === 0 - 1 === -1

x11*D23 - x12*D12 === 2*3 - 0*(-1) === 6

So, to solve for a larger matrix:
Laplace expansion.  the steps are:
1. select k rows and k columns (doesn't this always reduce to 2 rows and 2 columns?)
2. compute the kxk determinant of the submatrix (so, yes, via cofactor expansion)
3. multiply the calculated determinant by the complementary matrix.

M = [
    [2, -1, 0, 0, 0]
    [-1, 2, -1, 0, 0]
    [0, -1, 2, -1, 0]
    [0, 0, -1, 2, -1]
    [0, 0, 0, -1, 2]
]

Since we're always focused on 2x2 matrices as the base case problem, for a 5x5 matrix there and 5 choose 2.  More generally n choose 2.

(5 choose 2 ) === 5!/2!(5-3)! === 10

So there are 10 possible combinations of rows and columns

pick (choose) 2 row indexes and 2 column indexes of the 5x5 matrix form 2x2 a submatrix to solve for.

∑(i,j i<j)(((-1)^i+j+1)*det(A1:2,i:j)*det(A3:5,complement)) . -- where for Ax:y,a:b x:y are rows and a:b are columns.

If you list all possible pairs of rows and columns for a 5x5 5x5 matrix:

Rows (1, 2) and Columns (1, 2)
Rows (1, 2) and Columns (1, 3)
Rows (1, 2) and Columns (1, 4)
Rows (1, 2) and Columns (1, 5)
Rows (1, 2) and Columns (2, 3)
Rows (1, 2) and Columns (2, 4)
Rows (1, 2) and Columns (2, 5)
Rows (1, 2) and Columns (3, 4)
Rows (1, 2) and Columns (3, 5)
Rows (1, 2) and Columns (4, 5)

this combinatorial approach holds for any _any square matrix_.

'''

'''
41)

Q:
The 2x2 matrix AB = (2 by 3)(3 by 2) has a "Cauchy-binet formula" for det(AB)

det(AB) = sum of 2x2 determinants to use from A and B

A) Guess which 2x2 determinants to use from A and B
B) Test your formula when the rows of A are 1,2,3 and 1,4,7 and B=transpose(A)

A:
A = [
    [1,2,3]
    [1,4,7]
]

B = [
    [1, 1]
    [2, 4]
    [3, 7]
]

AB = [
    [14, 30]
    [30, 66]
]


'''

'''
6.1

19)
A 3x3 matrix B is known to have eigenvalues 0,1,2. this is information enough to find these:
a) the rank of B
b) the determinant of transpose(B)B
b) the eigenvalues of transpose(B)B
b) the eigenvalues of (B^2 + I)^-1

so for eigenvalue x:
Bx = λx
Bx = 0x
Bx = 1x
Bx = 2x


det(A-λI) = 0

a)
if 0 is an eigenvalue the matrix is singular.  Singular matrices are at most the rank of their dimensions minus 1, because all of the rows are not linearly independent
so rank is < 3

there are non-zero eigenvalues, so the rank is >0

if it were rank 1, there would only be one eigenvalue, corresponding to 1 independent vector

so x != 1, 0 < x < 3

x (rank) is 2

b)
transposition of a matrix doesn't affect the value of the determinant
The product of the eigenvalues of a matrix is equal to its determinant
det(transpose(B)B) === det(transpose(B))det(B) === det(B)^2 === (0*1*2)^2 === 0

c)


d)
In computational settings, (B^2 +I)^-1 is sometimes referred to as the inverse regularized matrix. (A shifted inverse or regularized inverse.)
This is due to its role in stabilizing computations when B^2 has eigenvalues close to zero.
In physics, appears in systems that involve damped responses or regularized inversions, especially in signal processing or control theory.
If B is diagonalizable, the eigenvalues of (B^2 +I)^-1 are given by a function

(B^2 + I) makes all of the elements positive with the sqaring, then adds the identity matrix so every element is +1, which ensures the matrix is not singular.

det(B) === ∏(λ^i) -- multiplying the trace gives you the determinant.  If any element is 0, the determinant is 0.  So sqaring means -1 == 1, adding the identity shifts the trace +1.  So it's impossible for 0 to be a value in the trace.


applying a polynomial to a matrix, then transforming the eigenvector has the same result as applying the polynomial to an eigenvalue, then transforming (scaling) the eigenvector.
so p(B)x === (asubk*A^k + asubk-1*A^k-1 + asubk-2*A^k-2 ... + asub0)x === (asubk*λ^k + asubk-1*λ^k-1 + asubk-2*λ^k-2 ... + asub0)x === p(λ)x
NOTE: adding a constant to a matrix, like the last step in the polynomial, + asub0, adds the value across the trace, not every element in the matrix.  so the constant term is really asub0*𝟙

so if p(B) === (B^2 + 𝟙)^-1 === 1/(B^2 + 𝟙)
then
p(0) === 1/(0^2 + 1) === 1
p(1) === 1/(1^2 + 1) === 1/2
p(2) === 1/(2^2 + 1) === 1/5
'''

'''
6.1

29)
Q: find the eigenvalues of A, B, and C

A = [
    [1,2,3]
    [0,4,5]
    [0,0,6]
]

B = [
    [0,0,1]
    [0,2,0]
    [3,0,0]
]

C = [
    [2,2,2]
    [2,2,2]
    [2,2,2]
]

det(A - λI)

det([
    [1 - λ,2,3]
    [0,4 - λ,5]
    [0,0,6 - λ]
]) === 1-λ((4-λ)(6-λ)) - 5*0 - 2*0 + 3*0 === 1-λ(20-4λ-6λ+λ^2) === 1-λ(20-10λ+λ^2) === 20-20λ-10λ+10λ^2+λ^2-λ^3 ===
-λ^3+11λ^2-30λ+20 <-- wrong, disregard

The eigenvalues of a triangular matrix are the entries of the trace, so for A, λ == {1,4,6}


Notes to help with C:
see Projection.md


A projection matrix is (v*transpose(v))/(transpose(v)*v)
so for a unit vector (1,1,1), the projection matrix is [
    [1/3, 1/3, 1/3]
    [1/3, 1/3, 1/3]
    [1/3, 1/3, 1/3]
]
this matrix projects any vector x onto the (column) space spanned by v

If the basis vector is scaled by 6, 6 * 1/3 === 2

so P = [
    [2,2,2]
    [2,2,2]
    [2,2,2]
] === 6*((1,1,1)transpose((1,1,1))/transpose((1,1,1))(1,1,1))

Pb === a((transpose(a)b)/(transpose(a)a)) === ax̂ === p

det(P−λI)=(2−λ)(−λ)(λ+4)

since all 3 vectors are dependent, the rank is 1, there is is only 1 non-zero eigenvalue, 6.  Technically 6, 0, 0 are the eigenvalues for the 3x3 matrix.
'''


'''
6.2

6)
Q:

a
Describe all matrices S that diagonalize this Matrix A

A = [
    [4, 0]
    [1, 2]
]

b.
Describe all of the matrices that Diagonalize A^-1


A:
a.
S = [
    [0, 2]
    [1, 1]
]

or

S = [
    [2, 0]
    [1, 1]
]

b.

A^-1 = [
    [.25, 0]
    [-.125, .5]
]

The same as a.? -- yes

'''

'''
6.2

15)
Q: A^k approaches 0 as k -> infinity. if and only if every eigenvalue is what?  Which matrix has A^k -> 0?

A1 = [
    [.6, .9]
    [.4, .1]
]

A2 = [
    [.6, .9]
    [.1, .6]
]

A:
less than 1
The first has an eigenvalue of 1 so it approaches infinity
the second has all eigenvalues < 1 so it approaches 0

'''

'''
6.2

16)

Q:

a. find Λ and S to diagonalize A1 in question 15.
b. what is the limit of Λ^k as k -> infinity?
c. what is the limit of S(Λ^k)S^1?
d. In the columns of this limiting matrix you see the what?

A:

a.
S = [
]

Λ = [
]

b.


c.


d.
steady state



'''
