text = input()
for x in text:
    if (x.isupper()):
        print(x.lower(), end="")
    else :
        print(x.upper(), end="")
