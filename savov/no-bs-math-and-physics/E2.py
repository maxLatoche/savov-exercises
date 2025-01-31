import sympy as sp

target_velocity = 100 # m/s
t =  sp.symbols('t')

# .5at^2 + v_i*t + x_i
a = 5 # m/s^2
v_i = 20 # m/s
x_i = 0

# 100m === 5m/s^2 * ts + 20m/s

print('E2.1a\n', sp.solve(sp.Eq(target_velocity, a*t + v_i), t))
# print('E2.1a\n', Polynomial((x_i, v_i, .5*a)).roots())

v_i = 30 # m/s
a = 10 # m/s^2
print('E2.1b\n', sp.solve(sp.Eq(target_velocity, a*t + v_i), t))

# the book says these are wrong but I can't figure out why?  chatgpt says I'm right but chatgpt is terrible at math (I did use the wolfram gpt)
# book answers are
# a 20s, 1400m
# b 10s, 800m