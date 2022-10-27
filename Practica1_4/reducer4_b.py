#!/usr/bin/python
import sys
import math

actualRang = 1
print("Range {0}".format(actualRang))
for line in sys.stdin:
    data = line.split()
    if float(data[0]) > actualRang:# lo supera
        actualRang += 1
        print("Range {0}".format(actualRang))
    print("Film ID {0}".format(data[1]))
