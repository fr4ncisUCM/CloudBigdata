import csv
from datetime import datetime
import sys

import enum

n = 0

for line in csv.reader(sys.stdin):
    if 80 > n > 0:
        print(line[1]+"\t"+line[2])
    n = n+1

