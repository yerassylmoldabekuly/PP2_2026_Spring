n, l, r = map(int, input().split())

x = list(map(int, input().split()))

x[l-1:r] = reversed(x[l-1:r])

for n in x:
    print(n, end=" ")