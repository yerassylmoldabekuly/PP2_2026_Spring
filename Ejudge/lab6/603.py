n = int(input())
words = list(map(str, input().split()))

for i, word in enumerate(words):
    print(f"{i}:{word}", end=" ")