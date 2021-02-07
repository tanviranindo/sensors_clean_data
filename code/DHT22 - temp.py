import csv

count = 0
sumTemperature_c = 0.0
sumTemperature_F = 0.0
maximumTemperature_c = None
maximumTemperature_F = None

file = open('../Sensors clean data/DHT22 - temp.csv')
csv_reader = csv.reader(file)
next(csv_reader)

for x in csv_reader:
    celsius = float(x[1].split('Temperature: ')[1].split(' *C')[0])
    fahrenheit = float(x[2].split(' *F')[0])

    sumTemperature_c += celsius
    sumTemperature_F += fahrenheit

    if maximumTemperature_c is None or celsius > maximumTemperature_c:
        maximumTemperature_c = celsius
    if maximumTemperature_F is None or fahrenheit > maximumTemperature_F:
        maximumTemperature_F = fahrenheit

    count = count + 1

print("Max Celsius: " + str(maximumTemperature_c) + ", Average Celsius: " + str("{:.2f}".format(sumTemperature_c / count)))
print('Max Fahrenheit: ' + str(maximumTemperature_F) + ', Average Fahrenheit: ' + str("{:.2f}".format(sumTemperature_F / count)))