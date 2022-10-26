#!/usr/bin/python

import sys

previous = None
#sum = 0
files = {}
#List of files empty
#hash para buscar cuantas veces aparece cada palabra.
#Mirar diccionarios en py
#grep zones 

for line in sys.stdin:
    key, value = line.strip().split('\t')
    
    if key != previous:
        if previous is not None:
            print(previous + '\t'+ str(files))
        previous = key
        files = {}
        #sum = 0
    
    files[value] = files.get(value,0)+1
    #sum = sum + int(value) # añadir si no esta
print(previous + '\t'+ str(files))
