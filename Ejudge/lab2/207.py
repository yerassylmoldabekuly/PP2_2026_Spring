n = int(input())

x = list(map(int, input().split()))

pos = 1
max_n = -10**9


for n in x:
    if n > max_n:
        max_n = n

for n in x:
    if n == max_n:
        print(pos)
        break
    pos += 1
