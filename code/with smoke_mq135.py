import csv
import matplotlib.pyplot as plt
import numpy as np

count = 0
sumAQ_withSmoke = 0.0
maximumAQ_withSmoke = None
x = []
y = []

file = open('../Sensors clean data/with smoke_mq135.csv')
csv_reader = csv.reader(file)
next(csv_reader)

for i in csv_reader:
    AQ_withSmoke = int(i[1].split(' PPM')[0])

    sumAQ_withSmoke += AQ_withSmoke

    if maximumAQ_withSmoke is None or AQ_withSmoke > maximumAQ_withSmoke:
        maximumAQ_withSmoke = AQ_withSmoke

    x.insert(count, count)
    y.insert(count, AQ_withSmoke)
    count = count + 1

xpt = np.array(x)
ypt = np.array(y)

plt.plot(xpt, ypt)
plt.title('mq135 with smoke')
plt.show()
print("Max AQ_withSmoke: " + str(maximumAQ_withSmoke) + " PPM, Average AQ_withSmoke: " + str(
    "{:.2f}".format(sumAQ_withSmoke / count)) + " PPM")
