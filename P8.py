import sympy as sp

print("P8.2\n", sp.Rational(.5**4))


# print("P8.3\n", "p**n\n") this was wrong, why?

# good short post candidate
# flip 1 P(n) === Pr({1 = p})
# flip 2 P(n) === Pr({2 = p}) AND Pr({1 = p - 1}) because to hit flip 2 flip 1 would need to be tails, which is p - 1
# so
# flip 2 P(n) === p(p - 1)
# continue the chain with subsequent flips
# flip 3 P(n) === p(p-1)(p-1) === p(p-1)**2
# flip N P(n) === p(p-1)**(N-1)


print("P8.3\n", "p(p-1)**(N-1)\n")

print("P8.4\n", "come back to this")

print("P8.5\n")
# Pr({Red = 50, Black = 50, Green = 1})
red = 50 / 101
black = 50 / 101
green = 1 / 101

probability_distribution = [red, black, green]

# these values are for a $1 bet on black
red_payout = 0
black_payout = 2
green_payout = 0

payouts = [red_payout, black_payout, green_payout]

print("p(black) ===", black)

winnings = 0
for i, chance in enumerate(probability_distribution):
    winnings += chance * payouts[i]

print("winnings", winnings)

print("winnings < bet, don\'t play")

print("p8.6\n")

probabilities = [(1/6, 0), (1/6, 0), (1/6, 0), (1/6, 1), (1/6, 1), (1/6, 5)]

winnings = 0
for probability in probabilities:
    winnings += probability[0] * probability[1]

print("winnings", winnings)
print("winnings > bet, play")

print("p8.8\n")

good_day_start = sp.Matrix([[1], [0]])
M = sp.Matrix([
    [1/2, 1/4],
    [1/2, 3/4]
])

one = M.multiply(good_day_start)
print(one)
two = M.multiply(M.multiply(good_day_start))
print(two)
# finding the state at infinity iterations means we'll wind up at the standard distribution
# we know that the standard distribution will be an eigenvector of M
# (M - 1)v = 0

# n = M.eigenvects()
# print(n.multiply(good_day_start))

# I think I'm struggling with sympy and numpy implemenatation details

# test is the transition matrix from the example in 8.2, but it doesn't come out to the same answer as the book
# furthermore, switching between rationals and decimals gives different answers
test = sp.Matrix([
    [sp.Rational(1/5), sp.Rational(1/10), sp.Rational(1, 3)],
    [sp.Rational(2/5), sp.Rational(8/10), sp.Rational(1, 3)],
    [sp.Rational(2/5), sp.Rational(1/10), sp.Rational(1, 3)]
])

print(test.eigenvects(simplify=True, rational=True))


