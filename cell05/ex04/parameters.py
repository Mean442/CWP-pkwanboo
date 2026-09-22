#!/usr/bin/env python3
import sys

count = 0

for i in sys.argv[1:]:
    count += 1

print(f"Number of parameters: {count}.")