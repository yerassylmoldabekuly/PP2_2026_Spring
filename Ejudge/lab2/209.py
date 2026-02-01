n = int(input())

x = list(map(int, input().split()))

max_n = 1
min_n = x[0]

for n in x:
    if n > max_n:
        max_n = n
    elif min_n > n:
        min_n = n

for n in x:
    if max_n == n:
        n = min_n
    print(n, end=" ")