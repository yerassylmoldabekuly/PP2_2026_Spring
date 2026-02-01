n = int(input())

x = list(map(int, input().split()))

s = set()
l = len(s)

for n in x:
    s.add(n)
    if l != len(s):
        print("YES")
        l = len(s)
    else:
        print("NO")