#!/usr/bin/python

import sys
import enum

class Column(enum.Enum):
    CLASS = 0
    MASS = 1

last = None
BufferMass = 0
NumMet = 0
actualType = None

for line in sys.stdin:
    
    actualType = line.split("\t")[Column.CLASS.value] # The type of met
    # Have to ignore the first row
    if last == None : # Check if is the first met
        last = actualType
    
    if last != actualType:         
        print(last+" "+str(BufferMass/NumMet))
        last = actualType
        BufferMass = 0
        NumMet = 1
        BufferMass += float(line.split("\t")[Column.MASS.value])
    else:
        BufferMass += float(line.split("\t")[Column.MASS.value])
        NumMet+=1
        
if last == actualType:          
    print(last+" "+str(BufferMass/NumMet))
   