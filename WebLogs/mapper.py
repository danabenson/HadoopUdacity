#!/usr/bin/python

import sys
import re

regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (\d+|-)'

for line in sys.stdin:

    if not line.strip():
        continue

    match = re.match(regex, line)

    if match is not None:
        data = match.groups()
        if len(data) == 5:
            ip,time,request,status,size= data
            print "{0}\t{1}".format(request, 1)

