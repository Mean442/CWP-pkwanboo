#!/usr/bin/env python3
import sys
import re


params = sys.argv[1:]

if len(params) != 2:
    print("none")
else:
    keyword = params[0]
    text = params[1]
    
    count = 0
    for match in re.finditer(keyword, text):
        count += 1
    
    if count == 0:
        print("none")
    else:
        print(count)