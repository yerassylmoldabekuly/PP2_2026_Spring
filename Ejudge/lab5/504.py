import re

s = input()

d = re.findall(r"[0-9]", s)
if re.sub("[+-.,:;]", "", s):
    print(*d)
else:
    d.sort()
    print(*d)