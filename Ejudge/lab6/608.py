n = int(input())
numbers = list(map(int, input().split()))

s = set()

for x in numbers:
    s.add(x)

print(*sorted(s))