#!/usr/bin/python

import sys


def reducer():
    prevKey = ''
    currentPosts = []
    currentReputation = ''


    for line in sys.stdin:
        data = line.strip().split('\t')

        thisKey = data[0]

        if prevKey != '' and prevKey != thisKey:
            for post in currentPosts:
                reputationAndPostId = [post[2], currentReputation]
                print '\t'.join(reputationAndPostId)
            currentPosts = []


        if line[1] == 'A':
            currentReputation = line[2]

        if line[1] == 'B':
            currentPosts.append(line)

        prevKey = thisKey