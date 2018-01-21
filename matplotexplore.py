import matplotlib.pyplot as plt

# plotting something
# plt.plot(x, y)
plt.plot([1,2,3], [5,7,4])
plt.show()

# data in variables, later can be non hard coded data filled by some function
x = [1,2,3,4]
y = [5,7,4,8]

x2 = [1,2,3,4]
y2 = [6,7,9,12]

plt.plot(x, y, label = 'line 1')
plt.plot(x2, y2, label = 'line 2')
plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Interesting graph')
plt.legend()
plt.show()