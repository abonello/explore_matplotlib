import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [1,2,5,8,6,3,4,7]

plt.plot(x,y, linestyle=":", label="data")
plt.xlabel('x')
plt.ylabel('y')
plt.title("Smoothed Line")
plt.legend()
plt.show()