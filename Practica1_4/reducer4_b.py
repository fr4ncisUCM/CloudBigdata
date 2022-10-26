#!/usr/bin/python
import sys
import math

actualRang = 1
print("Range {0}".format(actualRang))
for line in sys.stdin:
    rat, idFilm = line.split("\t")
    if float(rat) > actualRang:# lo supera
        actualRang += 1
        print("Range {0}".format(actualRang))
    print("Film ID {0}".format(idFilm))
