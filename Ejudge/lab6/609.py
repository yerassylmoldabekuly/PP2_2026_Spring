n = int(input())
keys = list(map(str, input().split()))
values = list(map(str, input().split()))


q = input()
b = False

for k, v in zip(keys, values):
    if k == q:
        print(v)
        b = True
        break

if b == False:
    print("Not found")