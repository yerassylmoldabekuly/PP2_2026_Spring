import re

s = input()

pattern = re.compile(r"\b[0-9]+\b")

if re.search(pattern, s):
    print("Match")
else:
    print("No match")