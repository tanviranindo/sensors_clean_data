import csv

count = 0
sumNormal = 0.0
maximumNormal = None

file = open('../Sensors clean data/normal air_mq135.csv')
csv_reader = csv.reader(file)
next(csv_reader)

for x in csv_reader:
    normal = int(x[1].split(' PPM')[0])

    sumNormal += normal

    if maximumNormal is None or normal > maximumNormal:
        maximumNormal = normal

    count = count + 1

print("Max : " + str(maximumNormal) + ", Average : " + str("{:.2f}".format(sumNormal / count)))