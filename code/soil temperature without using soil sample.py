import csv

count = 0
sumDegree = 0.0
sumTemperature = 0.0
maximumDegree = None
maximumTemperature = None

file = open('../Sensors clean data/soil temperature without using soil sample.csv')
csv_reader = csv.reader(file)
next(csv_reader)

for x in csv_reader:
    degree = float(x[1].split(' C')[0])
    fahrenheit = float(x[2].split(' F')[0])

    sumDegree += degree
    sumTemperature += fahrenheit

    if maximumDegree is None or degree > maximumDegree:
        maximumDegree = degree
    if maximumTemperature is None or fahrenheit > maximumTemperature:
        maximumTemperature = fahrenheit

    count = count + 1

print("Max Degree: " + str(maximumDegree) + ", Average Degree: " + str("{:.2f}".format(sumDegree / count)))
print('Max Fahrenheit: ' + str(maximumTemperature) + ', Average Fahrenheit: ' + str("{:.2f}".format(sumTemperature / count)))