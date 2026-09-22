#!/usr/bin/env python3
import sys

i = sys.argv[1:]


if len(i) < 2:
    print("none")
else:
    i.reverse()
    for item in i:
        print(item)