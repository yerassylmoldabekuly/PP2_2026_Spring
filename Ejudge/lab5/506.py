import re

s = input()

x = re.search(r"[a-zA-Z-09,.:;]+@[a-zA-Z0-9]+[.][a-zA-Z0-9]+", s)

if x:
    print(x.group())
else:
    print("No email")