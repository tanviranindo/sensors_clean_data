import csv
import matplotlib.pyplot as plt
import numpy as np

count = 0
sumHumidity = 0.0
maximumHumidity = None
x = []
y = []

file = open('../Sensors clean data/DHT22 - humidity sensor.csv')
csv_reader = csv.reader(file)
next(csv_reader)

for i in csv_reader:
    humidity = float(i[1].split('Humidity: ')[1].split(' %')[0])

    sumHumidity += humidity

    if maximumHumidity is None or humidity > maximumHumidity:
        maximumHumidity = humidity

    x.insert(count, count)
    y.insert(count, humidity)
    count = count + 1

xpt = np.array(x)
ypt = np.array(y)
plt.plot(xpt, ypt)
plt.show()
print("Max Humidity: " + str(maximumHumidity) + ", Average Humidity: " + str("{:.2f}".format(sumHumidity / count)))