n = int(input())
numbers = list(map(int, input().split()))

check = all(x >= 0 for x in numbers)

if check:
    print("Yes")
else:
    print("No")