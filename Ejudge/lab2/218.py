n = int(input())

shows = {}
pos = 1

while n != 0:
    x = input()
    shows[x] = shows.get(x, pos)
    pos += 1
    n -= 1

for key, value in sorted(shows.items()):
    print(key, value)