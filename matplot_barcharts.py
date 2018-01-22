import matplotlib.pyplot as plt

# Barcharts and Histograms
# Bar Charts - One series or comparison
# Histogram - meant to show a distribution

x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 = [1,3,5,9,11]
y2 = [7,8,2,4,2]

# Adding this data to stack on y2
x3 = [1,3,5,9,11]
y3 = [3,1,5,3,6]

plt.bar(x, y, label = 'Bars 1', color = 'r')
plt.bar(x2, y2, label = 'Bars 2', color = 'c')
# There are various ways how to call colors, single letters, names, # numbers etc.
# If 2 bar charts called A and B share the same x values, they can be stacked by adding bottom = A to B.
# This will result in B to be stacked over A.
plt.bar(x3, y3, label = 'Bar 3', color = 'g', bottom = y2)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Bar Charts')
plt.legend()
plt.show()
