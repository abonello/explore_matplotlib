import matplotlib.pyplot as plt

# I want to plot a line and also mark the individual points.

x = [1,2,3,4,5,6,7,8]
y = [3,7,6,8,5,4,9,4]

plt.scatter(x, y, color='r', marker="*", s = 20)
plt.plot(x, y, color='g', label="data", linestyle = ":")
plt.xlabel("independent variable")
plt.ylabel("data")
plt.title("Line with points")
plt.legend()
plt.show()