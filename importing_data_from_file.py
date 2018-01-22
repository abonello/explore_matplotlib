import matplotlib.pyplot as plt
import csv

# We will import data from a file and plot it.

x = []
y = []

with open('example_data.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    print plots
    for row in plots:
        print row
        x.append(int(row[0]))
        y.append(int(row[1]))


print x
print y
# plt.xlabel('')
# plt.ylabel('')
# plt.title("Data from File")
# plt.legend()
# plt.show()