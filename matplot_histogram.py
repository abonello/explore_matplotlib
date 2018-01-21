import matplotlib.pyplot as plt

# Histogram - show a distribution of some kind
# useful when you have an array or a very long list
# of things

population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,80,75,65,54,44,43,42,48]
#ids = [x+1 for x in range(len(population_ages))]
#plt.bar(ids, population_ages)

# For histograms we do not need the id.
# It has bins - a container for particular values

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
# The number of bins will control the number of bars.
# It can help to condense data.

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)


plt.xlabel('x')
plt.ylabel('y')
plt.title('A title\nA subtitle')
# plt.legend()
plt.show()