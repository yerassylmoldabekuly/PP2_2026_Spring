count = {}

n = int(input())
x = list(map(int, input().split()))

max_count = 0
answer = 0

for n in x:
    count[n] = count.get(n, 0) + 1

for key, value in count.items():
    if max_count < value:
        max_count = value
        answer = key
    elif max_count == value and key < answer:
        answer = key

print(answer)