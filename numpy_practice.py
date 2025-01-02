# found at https://www.geeksforgeeks.org/how-to-plot-an-angle-in-python-using-matplotlib/
import matplotlib.pyplot as plt
import numpy as np

import get_angle

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

# m === slope
# m = (y2 - y1) / (x2 - x1)
x_point_of_intersection = (y_intercept_2 - y_intercept_1) / (slope1 - slope2)
y_point_of_intersection = slope1 * x_point_of_intersection + y_intercept_1

plt.scatter(x_point_of_intersection, y_point_of_intersection, color='midnightblue')

theta = np.linspace(0, 2*np.pi, 100)
r = 1.0

x_points_circle = r * np.cos(theta) + x_point_of_intersection
y_points_circle = r * np.sin(theta) + y_point_of_intersection

plt.plot(x_points_circle, y_points_circle, color='green')

# intersection points
# I dislike mutating a global but this gets the job done for the simple example here
x_points = []
y_points = []

# point-slope formula
def get_points_of_intersection(m, intercept, center_x, center_y, radius):
    # the following was a failed attempt to solve this, which failed because we don't know one of the coordinates of the point we're trying to find
    # (y - y1) = m(x - x1)
    # our known point is the center of the circle, use that in the point-slope equation
    # (y - center_y) = m(x - center_x)
    # (y - 1.5)  = m(x - 2) === y - 1.5 = mx - 2 === y = mx - 0.5


    # this ended up being more relevant info than the previous comment block
    # We know that the equation of the circle having centre at (h, k) and radius = r units is
    # (x - h)**2 + (y - k)**2 = r**2
    # (x - h)(x - h) + (y - k)(y - k) = r**2
    # x**2 - 2xh + 2yk + h**2 + k**2 = r**2

    # find the coefficients
    # if slope is 0, 1 + m**2 === 1 + 0, so the coefficient of x**2 is 1
    a = 1 + m**2
    # -2xh + 2yk
    b = -2 * center_x + 2 * m * (intercept - center_y)
    # h**2 + k**2 - r**2
    c = center_x**2 + (intercept-center_y)**2 - radius**2

    # solving the quadratic equation:
    delta = b**2 - 4.0*a*c  # b^2 - 4ac
    x1 = (-b + np.sqrt(delta)) / (2.0 * a)
    x2 = (-b - np.sqrt(delta)) / (2.0 * a)


    x_points.append(x1)
    x_points.append(x2)

    y1 = m*x1 + intercept
    y2 = m*x2 + intercept

    y_points.append(y1)
    y_points.append(y2)

get_points_of_intersection(slope1, y_intercept_1, x_point_of_intersection, y_point_of_intersection, r)
get_points_of_intersection(slope2, y_intercept_2, x_point_of_intersection, y_point_of_intersection, r)

# the only root of the secant line that we care about here is the "upper" (higher y value)
plt.scatter(x_points[0], y_points[0], color='crimson')
plt.scatter(x_points[2], y_points[2], color='crimson')

# Naming the points.
plt.text(x_points[0], y_points[0], '  Point_P1', color='black')
plt.text(x_points[2], y_points[2], '  Point_P2', color='black')

upper_angle = get_angle.get_angle(x_points[0], y_points[0], x_point_of_intersection, y_point_of_intersection, r)
lower_angle = get_angle.get_angle(x_points[2], y_points[2], x_point_of_intersection, y_point_of_intersection, r)
difference = abs(upper_angle - lower_angle)
print(difference, np.rad2deg(difference))

theta_list = []
for i in range(len(x_points)):

    x = x_points[i]
    y = y_points[i]

    print('intersection point p{}'.format(i))
    theta_list.append(get_angle.get_angle(x, y, x_point_of_intersection, y_point_of_intersection, r))

p0 = theta_list[0]
p2 = theta_list[2]

arc_points = np.linspace(p0, p2, 100)

x1 = r * np.cos(arc_points) + x_point_of_intersection
x2 = r * np.sin(arc_points) + y_point_of_intersection

plt.plot(x1, x2, color="black")

plt.show()

