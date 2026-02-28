a, b = map(int, input().split())

def my_func(a1, b1):
    sq = (x*x for x in range(a1, b1 + 1))
    for i in sq:
        yield i

d = my_func(a, b)
for j in d:
    print(j)