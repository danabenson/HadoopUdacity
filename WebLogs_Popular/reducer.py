#!/usr/bin/python

import sys

maxTotalHits = 0
maxRequest = ''

totalHits = 0
prevKey = ''

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, value = data_mapped

    if prevKey != '' and thisKey != prevKey:
        if totalHits > maxTotalHits:
            maxTotalHits = totalHits
            maxRequest = prevKey
        totalHits = 0

    totalHits += 1
    prevKey = thisKey


if totalHits > maxTotalHits:
    maxTotalHits = totalHits
    maxRequest = thisKey

print "{0}\t{1}".format(maxRequest, maxTotalHits)