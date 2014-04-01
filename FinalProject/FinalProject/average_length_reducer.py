#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_NONE)

currentPostId = ''
answerLengths = []
postLength = 0

for line in reader:

    postId = line[0]
    nodeType = line[1]
    length = line[2]

    if postId != currentPostId and currentPostId != '':
        if len(answerLengths) > 0:
            #get the average length of all answers
            avgAnswerLength = sum(answerLengths) / float(len(answerLengths))
        else:
            #no answers for this question
            avgAnswerLength = 0
        writer.writerow([postLength, avgAnswerLength])
        answerLengths = []
        postLength = 0

    currentPostId = postId
    if nodeType == 'question':
        #set length of current question
        postLength = length
    elif nodeType == 'answer':
        #accumulate answer lengths for this question
        answerLengths.append(int(length))

#last post
if len(answerLengths) > 0:
    avgAnswerLength = sum(answerLengths) / float(len(answerLengths))
else:
    avgAnswerLength = 0

writer.writerow([postLength, avgAnswerLength])

