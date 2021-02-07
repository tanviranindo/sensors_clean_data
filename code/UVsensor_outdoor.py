import csv

count = 0
sumUV_indoor = 0.0
maximumUV_indoor = None

file = open('../Sensors clean data/UVsensor_outdoor.csv')
csv_reader = csv.reader(file)
next(csv_reader)

for x in csv_reader:
    UV_indoor = float(x[1].split('sensor reading = ')[1])

    sumUV_indoor += UV_indoor

    if maximumUV_indoor is None or UV_indoor > maximumUV_indoor:
        maximumUV_indoor = UV_indoor

    count = count + 1

print("Max sensor reading: " + str(maximumUV_indoor) + ", Average sensor reading : " + str("{:.2f}".format(sumUV_indoor / count)))