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
