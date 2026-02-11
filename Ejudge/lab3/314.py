n = int(input())
l = list(map(int, input().split()))
x = int(input())

i = 0
while i < x:
    data = input().split()
    a = data[0]

    if a == "abs":
        l = list(map(lambda a: abs(a), l))
        i += 1
    else:
        b = int(data[1])
        if a == "add":
            l = list(map(lambda a: a + b, l))
            i += 1
        elif a == "multiply":
            l = list(map(lambda a: a * b, l))
            i += 1
        elif a == "power":
            l = list(map(lambda a: a ** b, l))
            i += 1

print(*l)




