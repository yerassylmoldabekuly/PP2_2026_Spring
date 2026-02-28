def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

n = int(input())
count = 0
c = True

for number in fibonacci():
    if count >= n:
        break
    if not c:
        print(",", end="")
    print(number, end="")
    c = False
    count += 1