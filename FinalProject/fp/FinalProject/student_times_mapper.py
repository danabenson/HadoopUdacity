#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    if line[0] == 'id':
        continue
    #"2012-04-30 18:01:05.800986+00"
    #get date of post
    dateAdded = line[8][:-3]
    #get time of post
    timeAdded = dateAdded.split(' ')[1]
    #hour of post
    hourAdded = timeAdded[:2]
    writer.writerow([line[3], int(hourAdded)])

