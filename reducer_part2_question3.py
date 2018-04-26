#!/usr/bin/python

import sys

hitCount = 0
prevPage = None
maxHits = 0
popularPage = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		# Something has gone wrong. Skip this line.
		continue
	thisKey, thisCount = data_mapped
	
	if prevPage and prevPage != thisKey:
		if hitCount > maxHits:
			maxHits = hitCount
			popularPage = prevPage
		prevPage = thisKey
		hitCount = 0
	prevPage = thisKey
	hitCount += 1

if prevPage != None:
	if hitCount > maxHits:
		maxHits = hitCount
		popularPage = prevPage
print popularPage, "\t", maxHits
