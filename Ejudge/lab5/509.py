import re

s = input()

x = re.findall(r"\b[a-zA-Z]{3}\b", s)
print(len(x))