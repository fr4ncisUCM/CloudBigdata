import csv
from datetime import datetime
import sys

import enum
n = 0

for line in csv.reader(sys.stdin):
    if n != 0:
        print(line[3]+"\t"+(line[4] if line[4] != "" else "0"))
    n = n+1

