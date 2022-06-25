from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
import numpy as np

# plt.xlabel('x - axis')
# plt.ylabel('y - axis')

ax = plt.axes(xlim=(0, 4.5), ylim=(0, 3.5))

v1 = [3, 2]
v2 = [2, 2]
vector_sum = np.add(v1, v2) # [4, 2]

x = [0, v1[0]]
y = [0, v1[1]]
x1 = [0, v2[0]]
y1 = [0, v2[1]]


origin = (0, 0)

plt.plot(x, y, x1, y1)
ax.add_collection(PolyCollection([(origin, v1, vector_sum, v2, origin)], color="red", alpha=0.4))
# ax.add_collection(PolyCollection([(origin, (0, 2), (3, 2), (3, 0))], color="blue", alpha=0.4))
ax.add_collection(PolyCollection([(origin, (0, 1), (1, 1), (1, 0))], color="blue", alpha=0.4))

plt.show()
# plt.savefig("odd2d.png")
