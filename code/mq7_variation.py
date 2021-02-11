import csv
import matplotlib.pyplot as plt
import numpy as np

count = 0
sumVariation = 0.0
maximumVariation = None
x = []
y = []

file = open('../Sensors clean data/mq7_variation.csv')
csv_reader = csv.reader(file)
next(csv_reader)

for i in csv_reader:
    variation = int(i[1])

    sumVariation += variation

    if maximumVariation is None or variation > maximumVariation:
        maximumVariation = variation

    x.insert(count, count)
    y.insert(count, variation)
    count = count + 1

xpt = np.array(x)
ypt = np.array(y)
plt.plot(xpt, ypt)
plt.title('mq7_variation')
plt.show()
print("Max variation: " + str(maximumVariation) + ", Average variation: " + str("{:.2f}".format(sumVariation / count)))