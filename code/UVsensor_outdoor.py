import csv
import matplotlib.pyplot as plt
import numpy as np

count = 0
sumUV_outdoor = 0.0
maximumUV_outdoor = None
x = []
y = []

file = open('../Sensors clean data/UVsensor_outdoor.csv')
csv_reader = csv.reader(file)
next(csv_reader)

for i in csv_reader:
    UV_outdoor = float(i[1].split('sensor reading = ')[1])

    sumUV_outdoor += UV_outdoor

    if maximumUV_outdoor is None or UV_outdoor > maximumUV_outdoor:
        maximumUV_outdoor = UV_outdoor

    x.insert(count, count)
    y.insert(count, UV_outdoor)
    count = count + 1

xpt = np.array(x)
ypt = np.array(y)

plt.plot(xpt, ypt)
plt.title('UV sensor outdoor')
plt.show()
print("Max sensor reading: " + str(maximumUV_outdoor) + ", Average sensor reading : " + str("{:.2f}".format(sumUV_outdoor / count)))

