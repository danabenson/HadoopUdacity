#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

currentPostId = ''
authors = []

for line in reader:

    postId = line[0]
    authorId = line[1]

    if currentPostId == '':
        currentPostId = postId

    #accumulate authors
    if currentPostId == postId:
        authors.append(authorId)

    if currentPostId != postId:
        #write out current list of authors
        writer.writerow([currentPostId, ','.join(authors)])
        #start next post
        authors = [authorId]
        currentPostId = postId

#last post
writer.writerow([currentPostId, ','.join(authors)])