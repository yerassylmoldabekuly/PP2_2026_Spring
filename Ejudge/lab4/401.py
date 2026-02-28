n = int(input())

def my_func(num):
    for i in range(1, num + 1):
        yield i * i

d = my_func(n)

for x in d:
    print(x)