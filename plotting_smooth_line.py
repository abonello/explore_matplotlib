import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

x = [1,2,3,4,5,6,7,8]
y = [1,2,5,8,6,3,4,7]

# we need to convert x and y to np arrays

x = np.array(x)
y = np.array(y)

# We need to define new versions of x and y -- Smoothed
x_smooth = np.linspace(x.min(), x.max(), 300)
y_smooth = spline(x, y, x_smooth)

plt.scatter(x, y, color='k', label = "raw points", marker="v")
plt.plot(x, y, linestyle=":", label="raw data")
plt.plot(x_smooth, y_smooth, color = 'r', label = "smooth data")
plt.xlabel('x')
plt.ylabel('y')
plt.title("Smoothed Line")
plt.legend()
plt.show()