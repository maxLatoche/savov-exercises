import matplotlib.pyplot as plt
import numpy as np

plt.xlabel('x - axis')
plt.ylabel('y - axis')

v1 = [3, 0]
v2 = [1, 2]
vector_sum = np.add(v1, v2) # [4, 2]

x = [0, v1[0]]
y = [0, v1[1]]
x1 = [0, v2[0]]
y1 = [0, v2[1]]



plt.plot(x, y, x1, y1)
plt.fill_between([0, 1, 3, vector_sum[0], 3], [0, 2, 2, vector_sum[1], 0], color="red", alpha=0.4)

plt.show()
# plt.savefig("pgram2d.png")
