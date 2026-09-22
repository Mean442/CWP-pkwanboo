#!/usr/bin/env python

import sys

if (len(sys.argv) > 1) :
    print("none")
    
# i is row, j is colum
i = 0
while (i <= 10):
    print(f"Table de {i} :", end="")
    
    j = 0
    while (j < 11):
        print(f" {i * j}", end="")
        j += 1
        
    print()
    i += 1