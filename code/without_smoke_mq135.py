import csv
import matplotlib.pyplot as plt
import numpy as np

count = 0
sumAQ_withoutSmoke = 0.0
maximumAQ_withoutSmoke = None
x = []
y = []

file = open('../Sensors clean data/without_smoke_mq135.csv')
csv_reader = csv.reader(file)
next(csv_reader)

for i in csv_reader:
    AQ_withoutSmoke = int(i[1].split(' PPM')[0])

    sumAQ_withoutSmoke += AQ_withoutSmoke

    if maximumAQ_withoutSmoke is None or AQ_withoutSmoke > maximumAQ_withoutSmoke:
        maximumAQ_withoutSmoke = AQ_withoutSmoke

    x.insert(count, count)
    y.insert(count, AQ_withoutSmoke)
    count = count + 1

print(x)
print(y)
xpt = np.array(x)
ypt = np.array(y)

plt.plot(xpt, ypt)
plt.show()
print("Max AQ_withoutSmoke: " + str(maximumAQ_withoutSmoke) + " PPM, Average AQ_withoutSmoke: " + str("{:.2f}".format(sumAQ_withoutSmoke / count)) + " PPM")