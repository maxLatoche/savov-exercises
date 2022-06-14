# found at https://www.geeksforgeeks.org/how-to-plot-an-angle-in-python-using-matplotlib/
import matplotlib.pyplot as plt
import numpy as np

# slope  and intercepts
slope1, y_intercept_1 = (1/4), 1.0
slope2, y_intercept_2 = (3/4), 0.0

l = np.linspace(-6, 6, 100)

plt.figure(figsize=(8, 8))

plt.xlim(0, 6)
plt.ylim(0, 6)
plt.title('plot an angle w python')
plt.plot(l, l*slope1+y_intercept_1)
plt.plot(l, l*slope2+y_intercept_2)

x_point_of_intersection = (y_intercept_2 - y_intercept_1) / (slope1 - slope2)
y_point_of_intersection = slope1 * x_point_of_intersection + y_intercept_1

plt.scatter(x_point_of_intersection, y_point_of_intersection, color='midnightblue')

theta = np.linspace(0, 2*np.pi, 100)
r = 1.0

x_center = r * np.cos(theta) + x_point_of_intersection
y_center = r * np.sin(theta) + y_point_of_intersection

plt.plot(x_center, y_center, color='green')

plt.show()

