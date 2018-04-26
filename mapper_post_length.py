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
        body = line[4]
        node_type = line[5]

        if node_type == 'question':
            node_id = line[0]
        elif node_type == 'answer':
            node_id = line[7]

        print "{0}\t{1}\t{2}".format(node_id, node_type, len(body))
