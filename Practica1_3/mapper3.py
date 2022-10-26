import csv
from datetime import datetime
import sys

import enum
n=0

for line in csv.reader(sys.stdin):
    if n!= 0:
        print(line[0].split("-")[0]+","+line[4])
    n=n+1

