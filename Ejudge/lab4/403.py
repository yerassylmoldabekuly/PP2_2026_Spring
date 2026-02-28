n = int(input())

def my_func(num):
    d = (x for x in range(0, num + 1))
    for i in d:
        if i % 12 == 0:
            yield i

ctr = my_func(n)
for j in ctr:
    print(j, end=" ")