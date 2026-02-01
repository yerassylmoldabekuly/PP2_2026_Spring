serials = {}

n = int(input())

for i in range(n):
    dorama, epis = input().split()
    epis = int(epis)

    serials[dorama] = serials.get(dorama, 0) + epis

for key, value in sorted(serials.items()):
    print(key, value)