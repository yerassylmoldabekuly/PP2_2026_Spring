import re

s = input()
pattern = input()

count = 0

for i in re.finditer(re.escape(pattern), s):
    count += 1

print(count)
