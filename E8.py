import sympy as sp

print('E8.1a\n')
print('no')
print('\n')
print('E8.1a\n')
print('yes')
print('\n')
print('E8.1c\n')
print('no')
print('\n')

print('E8.2\n')
print('TBD see picture\n')

print('E8.4\n')

M = sp.Matrix([
    [sp.sympify("2/10"), sp.sympify("1/10"), sp.sympify("1/3")],
    [sp.sympify("4/10"), sp.sympify("8/10"), sp.sympify("1/3")],
    [sp.sympify("4/10"), sp.sympify("1/10"), sp.sympify("1/3")],
])

stationary_distribution = [
    sp.sympify("5/31"), sp.sympify("20/31"), sp.sympify("6/31")
]

# first option is to use the built in eigenvects method, which abstracts the steps of finding the roots of the
# characteristic polynominal, then substituting them into 𝒩(A - λ𝟙)
evec = M.eigenvects()[0][2][0]

# normalize to form a basis for the eigenspace (which is how the answer in the book is formatted)
print(evec/evec.norm(1))


evec = sp.Matrix((M - sp.Matrix.eye(3)).nullspace())

print(evec/evec.norm(1))

print('\n')
print('E8.5\n')

C = sp.Matrix([
    [sp.sympify("8/10"), sp.sympify("3/10"), sp.sympify("2/10")],
    [sp.sympify("1/10"), sp.sympify("2/10"), sp.sympify("6/10")],
    [sp.sympify("1/10"), sp.sympify("5/10"), sp.sympify("2/10")],
])

evec = C.eigenvects()[0][2][0]
evec = (C - sp.Matrix.eye(3)).nullspace()[0]

# it's unclear at this point why we switched from a Frobenius norm (square root of the sum of squares) to the
# maximum column sum norm, but that is what is used in the provided answer on page 545 and in this case they return different values, so it is necessary to switch -- revisit
print(evec/evec.norm(1))


