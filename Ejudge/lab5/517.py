import re

s = input()

x = re.findall(r"[0-9]{2}/[0-9]{2}/[0-9]{4}", s)
print(len(x))