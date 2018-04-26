#!/usr/bin/python

# Replace this with your mapper code
# This will actually not get graded at the moment, because it's
# pretty hard to properly simulate Hadoop cluster in our system :-)
# Thi will serve as a storage for your code.

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

reader.next()

for line in reader:
    if len(line) == 19:
        tagnames = line[2].split()
        for tag in tagnames:
			print tag
