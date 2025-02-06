import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5,100)
y = x

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x,y, 'r')
plt.plot([-3],[-3], marker="o", markersize=4, markeredgecolor="b")

# plt.show()
plt.savefig('linear_plot_point_minus_3.png')
