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

'''

