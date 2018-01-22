import matplotlib.pyplot as plt

# Explore Stack Plots
# Usually used to convey a holistic number as well as its breakdown.

# We will log 5 days of things happening.
days = [1,2,3,4,5]

sleeping = [7,8,6,9,7]
eating   = [2,3,4,3,2]
working  = [7,8,4,6,5]
playing  = [8,5,10,6,10]

plt.stackplot(days, sleeping, eating, working, playing, colors=['k', 'r', 'b', 'g'], labels=['sleeping', 'eating', 'working', 'playing'])

plt.xlabel('days')
plt.ylabel('hrs')
plt.title("Stack Plots")
plt.legend()
plt.show()