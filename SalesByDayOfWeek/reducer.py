#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None
numSales = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

dayTotalSalesAmounts = [0,0,0,0,0,0,0]
dayTotalSalesCounts = [0,0,0,0,0,0,0]

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    thisKey, thisSale = data_mapped

    dayTotalSalesAmounts[int(thisKey)] = dayTotalSalesAmounts[int(thisKey)] + float(thisSale);
    dayTotalSalesCounts[int(thisKey)] += 1


for x in range(0,7):
    if dayTotalSalesCounts[x] > 0:
        total = dayTotalSalesAmounts[x] / dayTotalSalesCounts[x]
    else:
        total = 0
    print "{0}\t{1}".format(x, total)