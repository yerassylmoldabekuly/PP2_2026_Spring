n = int(input())

po = (2**x for x in range(0, n + 1))
for i in po:
    print(i, end=" ")