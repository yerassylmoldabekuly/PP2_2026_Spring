import re

s = input()
substr = input()

result = re.search(substr, s)

if result:
    print("Yes")
else:
    print("No")