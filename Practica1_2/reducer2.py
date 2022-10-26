#!/usr/bin/python

from audioop import add
from email.policy import default
import sys

previous = None
#sum = 0
files = {}
#List of files empty
#hash para buscar cuantas veces aparece cada palabra.
#Mirar diccionarios en py
#grep zones 
#  key, value = line.strip().split('\t')
    
#     if key != previous:
#         if previous is not None:
#             print(previous + '\t'+ str(files))
#         previous = key
#         files = {}
#         #sum = 0
    
#     files[value] = files.get(value,0)+1
for line in sys.stdin:
    key = line.strip()
    if key != previous: # si la clave no es null ( la primera )
    
        if previous is not None: # no es none
            print(previous+ '\t'+ str(files))
        previous = key
        files = {}
           
    files[key] = files.get(key,0)+1
print(str(files))
