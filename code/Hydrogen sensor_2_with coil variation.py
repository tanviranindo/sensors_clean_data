import csv

count = 0
sumH2 = 0.0
maximumH2 = None

file = open('../Sensors clean data/Hydrogen sensor_2_with coil variation.csv')
csv_reader = csv.reader(file)
next(csv_reader)

for x in csv_reader:
    H2 = int(x[1].split('ppm')[0])

    sumH2 += H2

    if maximumH2 is None or H2 > maximumH2:
        maximumH2 = H2

    count = count + 1

print("Max H2_Concentration: " + str(maximumH2) + ", Average H2_Concentration: " + str("{:.2f}".format(sumH2 / count)))