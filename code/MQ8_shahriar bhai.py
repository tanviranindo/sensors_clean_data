import csv

count = 0
sumH2 = 0.0
sumAlcohol = 0.0
sumCO = 0.0
sumCH4 = 0.0
maximumH2 = None
maximumAlcohol = None
maximumCO = None
maximumCH4 = None

file = open('../Sensors clean data/MQ8_shahriar bhai.csv')
csv_reader = csv.reader(file)
next(csv_reader)

for x in csv_reader:
    H2 = int(x[1].split(' HYDROGEN:')[1].split('ppm')[0])
    Alcohol = int(x[2].split(' ALCOHOL:')[1].split('ppm')[0])
    CO = int(x[3].split(' CARBON_MONOXIDE:')[1].split('ppm')[0])
    CH4 = int(x[4].split(' METHANE:')[1].split('ppm')[0])

    sumH2 += H2
    sumAlcohol += Alcohol
    sumCO += CO
    sumCO += CH4

    if maximumH2 is None or H2 > maximumH2:
        maximumH2 = H2
    if maximumAlcohol is None or Alcohol > maximumAlcohol:
        maximumAlcohol = Alcohol
    if maximumCO is None or CO > maximumCO:
        maximumCO = CO
    if maximumCH4 is None or CH4 > maximumCH4:
        maximumCH4 = CH4

    count = count + 1

print("Max H2: " + str(maximumH2) + ", Average H2: " + str("{:.2f}".format(sumH2 / count)))
print("Max Alcohol: " + str(maximumAlcohol) + ", Average Alcohol: " + str("{:.1f}".format(sumAlcohol / count)))
print("Max CO: " + str(maximumCO) + ", Average CO: " + str("{:.2f}".format(sumCO / count)))
print("Max CH4: " + str(maximumCH4) + ", Average CH4: " + str("{:.2f}".format(sumCO / count)))
