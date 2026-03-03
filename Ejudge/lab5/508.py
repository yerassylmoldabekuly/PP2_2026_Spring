import re

s = input()
s2 = input()

x = re.split(s2, s)
print(*x, sep=",")
