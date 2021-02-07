import csv

count = 0
sumHumidity = 0.0
maximumHumidity = None

file = open('../Sensors clean data/DHT22 - humidity sensor.csv')
csv_reader = csv.reader(file)
next(csv_reader)

for x in csv_reader:
    humidity = float(x[1].split('Humidity: ')[1].split(' %')[0])

    sumHumidity += humidity

    if maximumHumidity is None or humidity > maximumHumidity:
        maximumHumidity = humidity

    count = count + 1

print("Max Humidity: " + str(maximumHumidity) + ", Average Humidity: " + str("{:.2f}".format(sumHumidity / count)))