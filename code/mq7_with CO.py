import csv
import matplotlib.pyplot as plt
import numpy as np

count = 0
sumCO = 0.0
maximumCO = None
x = []
y = []

file = open('../Sensors clean data/mq7_with CO.csv')
csv_reader = csv.reader(file)
next(csv_reader)

for i in csv_reader:
    variation = int(i[1])

    sumCO += variation

    if maximumCO is None or variation > maximumCO:
        maximumCO = variation

    x.insert(count, count)
    y.insert(count, variation)
    count = count + 1

xpt = np.array(x)
ypt = np.array(y)
plt.plot(xpt, ypt)
plt.title('mq7_with CO')
plt.show()
print("Max With_CO: " + str(maximumCO) + ", Average With_CO: " + str("{:.2f}".format(sumCO / count)))