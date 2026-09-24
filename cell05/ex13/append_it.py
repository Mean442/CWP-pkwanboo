#!/usr/bin/env python3
import sys


args = sys.argv[1:]

if not args:
    print("none")
    sys.exit()


for arg in args:
    if arg.endswith("ism"):
        continue

    print(arg + "ism")