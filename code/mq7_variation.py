import csv

count = 0
sumVariation = 0.0
maximumVariation = None

file = open('../Sensors clean data/mq7_variation.csv')
csv_reader = csv.reader(file)
next(csv_reader)

for x in csv_reader:
    variation = int(x[1])

    sumVariation += variation

    if maximumVariation is None or variation > maximumVariation:
        maximumVariation = variation

    count = count + 1

print("Max variation: " + str(maximumVariation) + ", Average variation: " + str("{:.2f}".format(sumVariation / count)))