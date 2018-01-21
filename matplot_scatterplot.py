import matplotlib.pyplot as plt

# Scatter Plot - a simple type of graph.
# Generally the idea of a scatter plot is to show
# the correlation between two sets of data or
# the distribution.
# In 3D graphs you can see the correlation between 3 sets of data.

x = [x+1 for x in range(8)]
y = [5,2,4,2,1,4,5,2]


plt.scatter(x, y, label = 'spread', color = 'k', marker ='$hjk$', s = 300) # k = black
# examples of markers: o, *, ^, ., v, <, >, 8, s, p, P, x, X, h, H, d, D, _, |
# interesting $text$ will render the string using mathtext
# s is the size of the marker


plt.xlabel('x')
plt.ylabel('y')
plt.title('A title')
plt.legend()
plt.show()