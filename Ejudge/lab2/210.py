n = int(input())

x = list(map(int, input().split()))

x.sort(reverse = True)

i = 0
while i < len(x):
    print(x[i], end=" ")
    i += 1

