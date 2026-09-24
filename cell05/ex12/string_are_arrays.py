#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
    sys.exit()

text = sys.argv[1]
result = ""


for c in text:
    if c == 'z':
        result += 'z'


if result:
    print(result)
else:
    print("none")