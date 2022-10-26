#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    file,line = line.split(":",1)
    words = re.sub(r'\W+', ' ', line).split()
    
    for word in words:
        print(word.lower() + "\t" + file)
    ##



