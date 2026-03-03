import re

s = input()

x = re.search("dog|cat", s)

if x:
    print("Yes")
else:
    print("No")