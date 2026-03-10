n = int(input())
words = list(map(str, input().split()))

m = max(words, key=len)
print(m)