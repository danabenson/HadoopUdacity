#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_NONE)

currentAuthor = ''
hourFrequencies = [0] * 24

for line in reader:
    author = line[0]
    hour = int(line[1])

    if currentAuthor == '':
        currentAuthor = author

    #increment current hour
    if currentAuthor == author:
        hourFrequencies[hour] = 1 + hourFrequencies[hour]

    if currentAuthor != author:
        maxIndex = 0
        #get most frequent hour
        for x in range(24):
            if hourFrequencies[x] > hourFrequencies[maxIndex]:
                maxIndex = x

        #any hours with the same frequency as the max frequency
        maxIndexs = [maxIndex]

        for x in range(23):
            if hourFrequencies[x] == hourFrequencies[maxIndex] and x != maxIndex:
                maxIndexs.append(x)
        for h in maxIndexs:
            writer.writerow([currentAuthor, h])

        currentAuthor = author
        hourFrequencies = [0] * 24
        hourFrequencies[hour] = 1 + hourFrequencies[hour]

#last author
maxIndex = 0
#get most frequent hour
for x in range(24):
    if hourFrequencies[x] > hourFrequencies[maxIndex]:
        maxIndex = x

#any hours with the same frequency as the max frequency
maxIndexs = [maxIndex]

for x in range(23):
    if hourFrequencies[x] == hourFrequencies[maxIndex] and x != maxIndex:
        maxIndexs.append(x)
for h in maxIndexs:
    writer.writerow([currentAuthor, h])