import csv
from datetime import datetime
import sys

import enum

for line in sys.stdin:
    idFilm, rat, rest = line.split("$")

    print(rat + "\t" + idFilm)
