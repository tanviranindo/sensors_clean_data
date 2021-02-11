import csv
import matplotlib.pyplot as plt
import numpy as np

count = 0
sumH2 = 0.0
maximumH2 = None
x = []
y = []

file = open('../Sensors clean data/HYdrogengas sensor_1_with coil variation.csv')
csv_reader = csv.reader(file)
next(csv_reader)

for i in csv_reader:
    H2 = int(i[1].split('ppm')[0])

    sumH2 += H2

    if maximumH2 is None or H2 > maximumH2:
        maximumH2 = H2

    x.insert(count, count)
    y.insert(count, H2)
    count = count + 1

xpt = np.array(x)
ypt = np.array(y)
plt.plot(xpt, ypt)
plt.title('Hydrogen gas sensor_1_with coil variation')
plt.show()
print("Max H2_Concentration: " + str(maximumH2) + ", Average H2_Concentration: " + str("{:.2f}".format(sumH2 / count)))