import re

s = input()

pattern = re.compile(r"\w+")

print(len(re.findall(pattern, s)))