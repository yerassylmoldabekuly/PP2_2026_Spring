import re

s = input()

pattern1 = r"Name:\s*([a-zA-Z']+\s*[a-zA-Z]*)"
pattern2 = r"Age:\s*(\d+)"

x = re.findall(pattern1, s)
y = re.findall(pattern2, s)

print(*x, *y)