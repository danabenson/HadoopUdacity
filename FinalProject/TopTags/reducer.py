#!/usr/bin/python

import sys
import csv

#class used to associate a tag with a count
class Tag:
    def __init__(self, tag, count):
        self.TagName = tag
        self.Count = count

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

currentTag = ''
topTags = []

for line in reader:

    tag = line[0]

    if currentTag == '':
        currentTag = Tag(tag,0)

    #increment tag count
    if currentTag.TagName == tag:
        currentTag.Count = currentTag.Count + 1

    elif currentTag.TagName != tag:
        #less than 10 tags in top 10, just add to top 10
        if len(topTags) <10:
            topTags.append(currentTag)
        else:
            #sort by count
            topTags = sorted(topTags, key=lambda x: x.Count)
            #should current tag go in top 10?
            if currentTag.Count > topTags[0].Count:
                #add to top 10
                topTags[0] = currentTag
        #update current tag
        currentTag = Tag(tag,1)

#last tag
if len(topTags) <10:
    topTags.append(currentTag)
else:
    topTags = sorted(topTags, key=lambda x: x.Count)
    if currentTag.Count > topTags[0].Count:
        topTags[0] = currentTag

topTags = sorted(topTags, key=lambda x: x.Count)

for t in topTags:
    writer.writerow([t.TagName,t.Count])
