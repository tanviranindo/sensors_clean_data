import csv

count = 0
sumCO = 0.0
maximumCO = None

file = open('../Sensors clean data/mq7_without CO.csv')
csv_reader = csv.reader(file)
next(csv_reader)

for x in csv_reader:
    variation = int(x[1])

    sumCO += variation

    if maximumCO is None or variation > maximumCO:
        maximumCO = variation

    count = count + 1

print("Max Without_CO: " + str(maximumCO) + ", Average Without_CO: " + str("{:.2f}".format(sumCO / count)))