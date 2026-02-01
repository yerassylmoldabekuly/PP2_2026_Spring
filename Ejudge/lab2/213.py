n = int(input())

i = 2
b = True

while i < n:
    if n % i == 0:
        b = False
        break
    i += 1

if b:
    print("Yes")
else:
    print("No")