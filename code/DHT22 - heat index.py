import csv

count = 0
sumHeat_index_C = 0.0
sumHeat_index_F = 0.0
maximumHeat_index_C = None
maximumHeat_index_F = None

file = open('../Sensors clean data/DHT22 - heat index.csv')
csv_reader = csv.reader(file)
next(csv_reader)

for x in csv_reader:
    celsius = float(x[1].split('Heat index:')[1].split(' *C')[0])
    fahrenheit = float(x[2].split(' *F')[0])

    sumHeat_index_C += celsius
    sumHeat_index_F += fahrenheit

    if maximumHeat_index_C is None or celsius > maximumHeat_index_C:
        maximumHeat_index_C = celsius
    if maximumHeat_index_F is None or fahrenheit > maximumHeat_index_F:
        maximumHeat_index_F = fahrenheit

    count = count + 1

print("Max Celsius: " + str(maximumHeat_index_C) + ", Average Celsius: " + str("{:.2f}".format(sumHeat_index_C / count)))
print('Max Fahrenheit: ' + str(maximumHeat_index_F) + ', Average Fahrenheit: ' + str("{:.2f}".format(sumHeat_index_F / count)))