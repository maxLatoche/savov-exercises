# found at https://www.geeksforgeeks.org/how-to-plot-an-angle-in-python-using-matplotlib/
import matplotlib.pyplot as plt
import numpy as np

# slope  and intercepts
s1, intercept1 = (1/4), 1.0
s2, intercept2 = (3/4), 0.0

l = np.linspace(-6, 6, 100)

plt.xlim(0, 6)
plt.ylim(0, 6)
plt.title('plot an angle w python')
plt.plot(l, l*s1+intercept1)
plt.plot(l, l*s2+intercept2)

plt.show()

