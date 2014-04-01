#!/usr/bin/python

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    words = re.findall(r"[\w]+", line[4])
    words = [x.lower() for x in words]
    words = [x.trim() for x in words]
    for word in words:
        writer.writerow([word,1])

