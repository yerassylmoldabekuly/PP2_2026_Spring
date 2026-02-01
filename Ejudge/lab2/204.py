n = int(input())

x = map(int, input().split())

positive = 0

for n in x:
    if n > 0:
        positive += 1

print(positive)