#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    if line[0] == 'id':
        continue
    #get individual tags
    tags = line[2].split(' ')
    nodeType = line[5]

    #only tags for questions
    if nodeType == 'question':
        for t in tags:
            writer.writerow([t,1])
