import re

s = input()

x = re.sub(r"\d", lambda a: a.group(0) * 2, s)
print(x)