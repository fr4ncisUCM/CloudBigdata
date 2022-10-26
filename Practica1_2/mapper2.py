#!/usr/bin/python

from gettext import find
import sys
import re

for line in sys.stdin:
    
    if (line.find("HEAD") != -1 or line.find("POST") != -1 or line.find("GET") != -1):
        if line.find("GET ") != -1:
            file,line = line.split("GET ")
            line,trash = line.split(" ",1)
            trash2,trash3 = trash.split(" ",1)
            line = line+ " "+trash2[:-1]
            
            
            
            print(line)
        
        if line.find("HEAD ") != -1:
            file,line = line.split("HEAD ")
            line,trash = line.split(" ",1)
            trash2,trash3 = trash.split(" ",1)
            line = line+ " "+trash2[:-1]
            
            print(line)
                 
        if line.find("POST ") != -1:
            file,line = line.split("POST ")
            line,trash = line.split(" ",1)
            trash2,trash3 = trash.split(" ",1)
            line = line+ " "+trash2[:-1]
            
            print(line)
        
        
        


