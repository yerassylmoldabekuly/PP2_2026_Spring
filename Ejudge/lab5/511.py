import re

s = input()

x = re.findall("[A-Z]", s)
print(len(x))