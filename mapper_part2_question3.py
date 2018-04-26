#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
	ip, id, user, datetime, timezone, method, path, proto, status, size = data
	fileName = path.split('/')[-1]
        #print "{0}\t{1}".format(path, fileName)
        print "{0}\t{1}".format(path,1)
    else:
	print("len=",len(data))
