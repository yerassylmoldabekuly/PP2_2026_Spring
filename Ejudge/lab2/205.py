import math
n = int(input())
sqrt = math.sqrt(n)

i = 1

b = True

while i < n:
    if 2 ** i == sqrt:
        b = True
        break
    elif 2 ** i == n:
        b = True
        break
    elif 2 ** i > n:
        b = False
        break
    i += 1

if b:
    print("YES")
else:
    print("NO")
