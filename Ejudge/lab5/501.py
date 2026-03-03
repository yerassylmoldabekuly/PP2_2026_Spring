import re
s = input()

result = re.match("Hello", s)

if result:
    print("Yes")
else:
    print("No")