import csv
# import matplotlib.pyplot as plt
# import numpy as np

count = 0
sumDegree = 0.0
sumTemperature = 0.0
maximumDegree = None
maximumFahrenheit = None
# x = []
# y = []
# z = []

file = open('../Sensors clean data/soil temperature without using soil sample.csv')
csv_reader = csv.reader(file)
next(csv_reader)

for i in csv_reader:
    celsius = float(i[1].split(' C')[0])
    fahrenheit = float(i[2].split(' F')[0])

    sumDegree += celsius
    sumTemperature += fahrenheit

    if maximumDegree is None or celsius > maximumDegree:
        maximumDegree = celsius
    if maximumFahrenheit is None or fahrenheit > maximumFahrenheit:
        maximumFahrenheit = fahrenheit

    # x.insert(count, count)
    # y.insert(count, degree)
    # z.insert(count, fahrenheit)
    count = count + 1

# ran = range(0, 100)
# plt.plot(ran, y)
# plt.plot(ran, z)
# plt.show()
print("Max Celsius: " + str(maximumDegree) + ", Average Celsius: " + str("{:.2f}".format(sumDegree / count)))
print('Max Fahrenheit: ' + str(maximumFahrenheit) + ', Average Fahrenheit: ' + str("{:.2f}".format(sumTemperature / count)))