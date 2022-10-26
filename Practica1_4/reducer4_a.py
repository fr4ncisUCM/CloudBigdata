#!/usr/bin/python

import sys
import enum


class Column(enum.Enum):
    ID = 0
    RATING = 1


last = None
BufferRating = 0
NumVal = 0
actualFilm = None

for line in sys.stdin:

    actualFilm = line.split("\t")[Column.ID.value]  # The type of met
    # Have to ignore the first row
    if last ==  None:  # Check if is the first met
        last = actualFilm

    if last != actualFilm:
        print(last + "$" + str(float(BufferRating / NumVal))+"$-")
        last = actualFilm
        BufferRating = 0
        NumVal = 1
        BufferRating += float(line.split("\t")[Column.RATING.value])
    else:
        BufferRating += float(line.split("\t")[Column.RATING.value])
        NumVal += 1

if last == actualFilm:
    print(last + "$" + str(BufferRating / NumVal)+"$-")
