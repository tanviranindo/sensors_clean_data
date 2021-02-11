import csv
import matplotlib.pyplot as plt
import numpy as np

count = 0
sumNormal = 0.0
maximumNormal = None
x = []
y = []

file = open('../Sensors clean data/normal air_mq135.csv')
csv_reader = csv.reader(file)
next(csv_reader)

for i in csv_reader:
    normal = int(i[1].split(' PPM')[0])

    sumNormal += normal

    if maximumNormal is None or normal > maximumNormal:
        maximumNormal = normal

    x.insert(count, count)
    y.insert(count, normal)
    count = count + 1

xpt = np.array(x)
ypt = np.array(y)
plt.plot(xpt, ypt)
plt.show()
print("Max : " + str(maximumNormal) + ", Average : " + str("{:.2f}".format(sumNormal / count)))