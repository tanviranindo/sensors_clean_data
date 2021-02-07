import csv

count = 0
sumHeight = 0.0
sumPressure = 0.0
sumTemperature = 0.0
maximumHeight = None
maximumPressure = None
maximumTemperature = None

file = open('../Sensors clean data/Barometric pressure sensor.csv')
csv_reader = csv.reader(file)
next(csv_reader)

for x in csv_reader:
    height = float(x[1])
    pressure = float(x[2].split(' Pa')[0])
    temperature = float(x[3].split(' C')[0])

    sumHeight += height
    sumPressure += pressure
    sumTemperature += temperature

    if maximumHeight is None or height > maximumHeight:
        maximumHeight = height
    if maximumPressure is None or pressure > maximumPressure:
        maximumPressure = pressure
    if maximumTemperature is None or temperature > maximumTemperature:
        maximumTemperature = temperature

    count = count + 1

print("Max Height: " + str(maximumHeight) + ", Average Height: " + str("{:.2f}".format(sumHeight/count)))
print("Max Pressure: " + str(maximumPressure) + ", Average Pressure: " + str("{:.1f}".format(sumPressure/count)))
print("Max Temperature: " + str(maximumTemperature) + ", Average Temperature: " + str("{:.2f}".format(sumTemperature/count)))
