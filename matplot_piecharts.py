import matplotlib.pyplot as plt

# Pie Charts - Useful to show percentage taken by different categories.

# We will log 5 days of things happening.
days = [1,2,3,4,5]

sleeping = [7,8,6,9,7]
eating   = [2,3,4,3,2]
working  = [7,8,4,6,5]
playing  = [8,5,10,6,10]

slice1 = [sleeping[4],eating[4], working[4], playing[4]] # 7 2 5 10
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['k', 'r', 'b', 'g']

plt.pie(slice1, labels = activities, colors = cols)

# It does not make sense to have x and y labels
# Legend is not needed in this case
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
plt.title('Pie Chart')
plt.suptitle('Day 5', y = 0.88, fontsize = 10) # used as subtitle
plt.show()