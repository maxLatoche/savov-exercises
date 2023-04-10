import sympy as sp

print("P8.2\n", sp.Rational(.5**4))


# print("P8.3\n", "p**n\n") this was wrong, why?

# flip 1 P(n) === Pr({1 = p})
# flip 2 P(n) === Pr({2 = p}) AND Pr({1 = p - 1}) because to hit flip 2 flip 1 would need to be tails, which is p - 1
# so
# flip 2 P(n) === p(p - 1)
# continue the chain with subsequent flips
# flip 3 P(n) === p(p-1)(p-1) === p(p-1)**2
# flip N P(n) === p(p-1)**(N-1)


print("P8.3\n", "p(p-1)**(N-1)\n")



