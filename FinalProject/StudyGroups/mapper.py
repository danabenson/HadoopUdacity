#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    #skip header orw
    if line[0] == 'id':
        continue

    nodeType = line[5]
    #if question get the post id
    if nodeType == 'question':
        postId = line[0]
    else:
        #otherwise get the abs parent id
        postId = line[7]

    authorId = line[3]

    writer.writerow([postId, authorId])