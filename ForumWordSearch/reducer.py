#!/usr/bin/python

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')

totalFantastic = 0
nodesWithFantastically = []

for line in reader:
    if line[0] == 'fantastic':
        totalFantastic+= 1

    #if 'fantastically' in line[1]:
     #   nodesWithFantastically.append(float(line[0]))

print totalFantastic
#nodesWithFantastically.sort()
#print nodesWithFantastically