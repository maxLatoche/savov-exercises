import matplotlib.pyplot as plt
from matplotlib import collections, colors, transforms
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from sympy import Matrix


ax = plt.axes(xlim=(0,10), ylim=(0, 10), zlim=(0, 10), projection='3d')

plt.xlabel('x - axis')
plt.ylabel('y - axis')
ax.set_zlabel('z - axis')

x1 = []
x2 = []
x3 = []
y1 = []
y2 = []
y3 = []

A = Matrix([
    [4, 1, 2],
    [4, 3, 0],
    [1, 2, 4],
])

v = Matrix([
    [-1],
    [-1],
    [-1]
])

# w = Matrix([
#     [1],
#     [-1],
#     [9]
# ])

# z = w.adjoint()

print(z)

# v1 = [4, 1, 2]
# v2 = [4, 3, 0]
# v3 = [1, 2, 4]

x1 = [0, A[0,0]]
y1 = [0, A[0,1]]
z1 = [0, A[0,2]]
x2 = [0, A[1,0]]
y2 = [0, A[1,1]]
z2 = [0, A[1,2]]
x3 = [0, A[2,0]]
y3 = [0, A[2,1]]
z3 = [0, A[2,2]]

# origin = (0, 0, 0)

ax.plot(x1, y1, z1)
ax.plot(x2, y2, z2)
ax.plot(x3, y3, z3)
# ax.plot([0, v[0]], [0, v[1]],[0, v[2]])
ax.plot([0, w[0]], [0, w[1]],[0, w[2]])

# plt.show()
# plt.savefig("simpleRref5.png")
