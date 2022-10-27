import csv
from datetime import datetime
import sys

import enum

for line in sys.stdin:
    data = line.split()

    print(data[1] + "\t" + data[0])
