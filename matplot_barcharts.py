import matplotlib.pyplot as plt

# Barcharts and Histograms
# Bar Charts - One series or comparison
# Histogram - meant to show a distribution

x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 = [1,3,5,9,11]
y2 = [7,8,2,4,2]

plt.bar(x, y, label = 'Bars 1', color = 'r')
plt.bar(x2, y2, label = 'Bars 2', color = 'c')
# There are various ways how to call colors, single letters, names, # numbers etc.

plt.xlabel('x')
plt.ylabel('y')
plt.title('A title')
plt.legend()
plt.show()
