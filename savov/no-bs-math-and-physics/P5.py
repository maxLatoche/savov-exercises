
print('P5.1 1\n', -6)
print('P5.1 2\n', 2)
print('P5.1 3\n', None)
print('P5.1 4\n', 8.5)
print('P5.1 5\n', -5)
print('P5.1 6\n', None)
print('P5.1 7\n', -2)
print('P5.1 8\n', -2)
print('P5.1 9\n', -2)
print('P5.1 10\n', False)
print('P5.1 11\n', "['-10', -5), [-5, 2), [2, 5), (5,10]")


print('P5.2 a\n', 4)
print('P5.2 b\n', 6)
print('P5.2 c\n', 5)

# y = x^13
print('P5.7 1\n', '13x^12')
# y = x^-3/2
print('P5.7 2\n', '(-3/2)x^-5/2')
# y = x^2a
print('P5.7 3\n', '2ax^(2a-1)')
# u = x^2.4
print('P5.7 4\n', '2.4x^1.4')
# z = cube_root(x)
print('P5.7 5\n', '(1/3)x^-2/3')
# y = cube_root(x^-5)
# chain rule f'(g(x))g'(x)
# f'(x) === (1/3)x^-2/3
# f'(g(x)) === (1/3)(x^-5)^-2/3 === (1/3)x^10/3
# g'(x) === -5x^-6
# (1/3)x^10/3 * -5x^-6
print('P5.7 6\n', '(-5/3)x^-8/3')
# u = 5_root(1/x^8)
print('P5.7 7\n', '')
# y = 2x^a
print('P5.7 8\n', '')
# y = q_root(x^3)
print('P5.7 9\n', '')

# y = ax^3 + 6
print('P5.8 1\n', "dy/dx p = 3ax^2")
# y = 13x^(3/2) - c
# y' = 13(3/2)x^1/2
print('P5.8 2\n', "dy/dx = 19.5x^1/2")
# y = 12x^(1/2) + c^1/2
# y' = 12((1/2)x^-1/2)
print('P5.8 3\n', "dy/dx = 6x^-1/2")
# y = c^(1/2)x^(1/2)
print('P5.8 4\n', "dy/dx = ((1/2)c^(-1/2))(x^(-1/2)) + (c^(1/2))((1/2)x^(-1/2))") # WRONG -- c is a constant so the answer is just ((1/2)x^(-1/2))
# u = (az^n - 1)/c
print('P5.8 5\n', "du/dz = naz^n-1)/c")
# y = 1.18t^2 + 22.4
print('P5.8 6\n', "dy/dt = 2.36t")

print('P5.9a', "it's the same because it is the taylor series for e^x, and e^x has the derivative (e^x)ln(e) === (e^x)*1")

print('P5.9b', "2ax + b")

print('P5.9c', "3(x + a)^2")

# w = t(a - (1/2)bt)
print('5.10a', "dw/dt = 1(a - (1/2)bt) + t((1/2)b) === a - (1/2)bt + (1/2)bt === a - bt")

# y = (x + -1^(1/2))(x - -1^(1/2))
# x^2 + x1^(1/2) - x1^(1/2)
print('5.10b', "2x")

# y = (197x - 34x^2)(7 + 22x - 83x^3)
# 197x7 + 197x22x - 197x83x^3 -( 34x^2)7 - 22x34x^2 + (83x^3)(34x^2) === 2822x^5 −16351x^4 −748x^3 +4096x^2 +1379x
print('5.10c', "14110x^4 - 65404x^3 - 2244x^2 + 8192x + 1379")

# x = (y + 3)(y + 5)
# 1(y+5) + (y + 3)1
print('5.10c', "2y + 8")

# y = 1.3709x(112.6 + 45.202x^2)
# 1.3709(112.6 + 45.202x^2) + 1.3709x(90.404x)
# 154.36334 + 61.967x^2 + 123.934x^2
print('5.10c', "154.36334 + 185.901x^2")
