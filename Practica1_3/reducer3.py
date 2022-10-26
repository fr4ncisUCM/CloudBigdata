#!/usr/bin/python

import sys
import enum

class Column(enum.Enum):
    DATE = 1
    OPEN = 2
    HIGH = 3
    LOW = 4
    CLOSE = 5
    ADJ_CLOSE = 6
    VOLUME = 7

last = None
BufferDay = 0
NumDays = 0
actual = None

for line in sys.stdin:
    actual = line.split(",")[0]
    # Have to ignore the first row
    if last == None : # Check year
        last = actual
    
    if last != actual:         
        print(last+" "+str(BufferDay/NumDays))
        last = actual
        BufferDay = 0
        NumDays = 1
        BufferDay += float(line.split(",")[1])
    else:
        # Doesn't work bc the notacion with points don't fit with integer
        BufferDay += float(line.split(",")[1])
        NumDays+=1
        
if last == actual:         
    print(last+" "+str(BufferDay/NumDays))
   