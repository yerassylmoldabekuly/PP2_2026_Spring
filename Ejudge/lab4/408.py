n = int(input())

gen = (x for x in range(2, n + 1))
for i in gen:
    j = i
    num = 2
    b = True
    while num < j:
        if j % num != 0 and j > 1:
            b = True
            num += 1
        else:
            b = False
            break
    if b:
        print(j, end=" ")
