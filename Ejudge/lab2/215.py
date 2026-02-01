n = int(input())
s = set()

while n != 0:
    surname = input()
    s.add(surname)
    n -= 1

print(len(s))