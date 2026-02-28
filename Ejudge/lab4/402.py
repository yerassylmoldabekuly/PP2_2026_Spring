n = int(input())

even = (x for x in range(0, n + 1))
first = True
for i in even:
    if i % 2 == 0:
        if not first:
            print(",", end="")
        print(i, end="")
        first = False
