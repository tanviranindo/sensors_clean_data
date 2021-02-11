import csv
import matplotlib.pyplot as plt
import numpy as np

count = 0
sumUV_indoor = 0.0
maximumUV_indoor = None
x = []
y = []

file = open('../Sensors clean data/UVsensor_indoor.csv')
csv_reader = csv.reader(file)
next(csv_reader)

for i in csv_reader:
    UV_indoor = float(i[1].split('sensor reading = ')[1])

    sumUV_indoor += UV_indoor

    if maximumUV_indoor is None or UV_indoor > maximumUV_indoor:
        maximumUV_indoor = UV_indoor
    x.insert(count, count)
    y.insert(count, UV_indoor)
    count = count + 1

print(x)
print(y)
xpt = np.array(x)
ypt = np.array(y)

plt.plot(xpt, ypt)
plt.show()
print("Max sensor reading: " + str(maximumUV_indoor) + ", Average sensor reading : " + str("{:.2f}".format(sumUV_indoor / count)))