#!/usr/bin/python

from audioop import add
from email.policy import default
import sys

previous = None

files = {}

for line in sys.stdin:
    key = line.strip()
    if key != previous:  # si la clave no es null ( la primera )
    
        if previous is not None:  # no es none
            print(previous + '\t' + str(files.get(previous)))
        previous = key
        files = {}
           
    files[key] = files.get(key, 0)+1
#print(str(files))
