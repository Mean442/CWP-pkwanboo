#!/usr/bin/env python3

import sys


x = sys.argv[1:]

if len(sys.argv) == 0 :
    print("none")
else :
    for i in x:
        print(i.upper())
        break