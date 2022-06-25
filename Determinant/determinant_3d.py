import matplotlib.pyplot as plt
from matplotlib import collections, colors, transforms
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


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

v1 = [4, 0, 2]
v2 = [4, 3, 0]
v3 = [1, 2, 4]

vector_sum12 = np.add(v1, v2)
vector_sum13 = np.add(v1, v3)
vector_sum23 = np.add(v2, v3)
vector_sum123 = np.add(vector_sum12, v3)

# def vectors_to_plot(*args):
#     result = {}
#     for i, vector in enumerate(args):
#         x_key = 'x' + str(i)
#         y_key = 'y' + str(i)
#         z_key = 'z' + str(i)
#         print(x_key)
#         for val in vector:
#             if x_key in result:
#                 result[x_key].append(val)
#             else:
#                 result[x_key] = [val]

# vectors_to_plot([v1, v2])

x1 = [0, v1[0]]
y1 = [0, v1[1]]
z1 = [0, v1[2]]
x2 = [0, v2[0]]
y2 = [0, v2[1]]
z2 = [0, v2[2]]
x3 = [0, v3[0]]
y3 = [0, v3[1]]
z3 = [0, v3[2]]

origin = (0, 0, 0)

ax.plot(x1, y1, z1)
ax.plot(x2, y2, z2)
ax.plot(x3, y3, z3)
# ax.add_collection3d(plt.fill_between([0, 1],[0,2], color='red', alpha=0.4), zdir='y')
ax.add_collection3d(Poly3DCollection([(origin, v1, vector_sum12, v2, origin)], color='red', alpha=0.4))
# ax.add_collection3d(Poly3DCollection([(origin, v1, vector_sum13, v3, origin)], color='red', alpha=0.4))
# ax.add_collection3d(Poly3DCollection([(origin, v2, vector_sum23, v3, origin)], color='red', alpha=0.4))
# ax.add_collection3d(Poly3DCollection([(v1, vector_sum12, vector_sum123, vector_sum13, v1)], color='red', alpha=0.4))
# ax.add_collection3d(Poly3DCollection([(v2, vector_sum12, vector_sum123, vector_sum23, v2)], color='red', alpha=0.4))
# ax.add_collection3d(Poly3DCollection([(v3, vector_sum13, vector_sum123, vector_sum23, v3)], color='red', alpha=0.4))

plt.show()
# plt.savefig("simpleRref5.png")
