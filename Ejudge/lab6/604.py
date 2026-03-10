n = int(input())
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

sum = 0
for a,b in zip(arr, arr2):
    sum += a*b

print(sum)