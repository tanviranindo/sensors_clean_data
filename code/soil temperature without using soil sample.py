import csv
import matplotlib.pyplot as plt
import numpy as np

count = 0
sumDegree = 0.0
sumTemperature = 0.0
maximumDegree = None
maximumTemperature = None
x = []
y = []
z = []

file = open('../Sensors clean data/soil temperature without using soil sample.csv')
csv_reader = csv.reader(file)
next(csv_reader)

for i in csv_reader:
    degree = float(i[1].split(' C')[0])
    fahrenheit = float(i[2].split(' F')[0])

    sumDegree += degree
    sumTemperature += fahrenheit

    if maximumDegree is None or degree > maximumDegree:
        maximumDegree = degree
    if maximumTemperature is None or fahrenheit > maximumTemperature:
        maximumTemperature = fahrenheit

    x.insert(count, count)
    y.insert(count, degree)
    z.insert(count, fahrenheit)
    count = count + 1

print(x)
print(y)
print(z)
xpt = np.array(x)
ypt = np.array(y)
zpt = np.array(z)
plt.scatter(xpt, ypt, zpt)
plt.show()
print("Max Degree: " + str(maximumDegree) + ", Average Degree: " + str("{:.2f}".format(sumDegree / count)))
print('Max Fahrenheit: ' + str(maximumTemperature) + ', Average Fahrenheit: ' + str("{:.2f}".format(sumTemperature / count)))