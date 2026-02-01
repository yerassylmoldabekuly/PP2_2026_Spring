n = int(input())

x = map(int, input().split())

max_n = -10**9

for n in x:
    if n > max_n:
        max_n = n

print(max_n)