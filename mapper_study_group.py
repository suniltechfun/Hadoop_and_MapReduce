#!/usr/bin/python

# Replace this with your mapper code
# This will actually not get graded at the moment, because it's
# pretty hard to properly simulate Hadoop cluster in our system :-)
# This will serve as a storage for your code.

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

reader.next()

for line in reader:
    if len(line) == 19:
        author_id = line[3]
        node_type = line[5]

        if node_type == 'question':
            node_id = line[0]
        else:
            node_id = line[7]

        print "{0}\t{1}".format(node_id, author_id)