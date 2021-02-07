import csv

count = 0
sumAQ_withSmoke = 0.0
maximumAQ_withSmoke = None

file = open('../Sensors clean data/with smoke_mq135.csv')
csv_reader = csv.reader(file)
next(csv_reader)

for x in csv_reader:
    AQ_withSmoke = int(x[1].split(' PPM')[0])

    sumAQ_withSmoke += AQ_withSmoke

    if maximumAQ_withSmoke is None or AQ_withSmoke > maximumAQ_withSmoke:
        maximumAQ_withSmoke = AQ_withSmoke

    count = count + 1

print("Max AQ_withSmoke: " + str(maximumAQ_withSmoke) + " PPM, Average AQ_withSmoke: " + str("{:.2f}".format(sumAQ_withSmoke / count)) + " PPM")