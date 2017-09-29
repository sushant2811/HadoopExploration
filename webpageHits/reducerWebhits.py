#!/usr/bin/python

import sys

hitsTotal = 0
oldKey = None

# Loop around the data
# It will be in the format key \t val
# Where key is the webpage name, val = 1 for the page hit
#
# All the hits for a particular webpage will be presented,
# then the key will change and we'll be dealing with the next webpage

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisHit = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", hitsTotal
        oldKey = thisKey;
        hitsTotal = 0

    oldKey = thisKey
    hitsTotal += float(thisHit)

if oldKey != None:
    print oldKey, "\t", hitsTotal

