#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    if line[0] == 'id':
        continue
    nodeType = line[5]
    bodyLength = len(line[4])
    if nodeType == 'question':
        postId = line[0]
    elif nodeType == 'answer':
        #get the parent id
        postId = line[6]

    #only question and answers
    if nodeType == 'question' or nodeType == 'answer':
        writer.writerow([postId, nodeType, bodyLength])

