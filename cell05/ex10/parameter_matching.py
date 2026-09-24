#!/usr/bin/env python3
import sys

params = sys.argv[1:]

if len(params) != 1:
    print("none")
else:
    target_param = ""
    for p in params:
        target_param = p

    user_input = input("What was the parameter? ")

    if user_input == target_param:
        print("Good job!")
    else:
        print("Nope, sorry...")