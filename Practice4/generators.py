#1

n = int(input())
sq = (x*x for x in range(n + 1))
for i in sq:
    print(i, end=" ")

print("\n")
print("--------------------------")

#2

n = int(input())
even = [x for x in range(n + 1) if x % 2 == 0]

for i in range(len(even)):
    if i == len(even) - 1:
        print(even[i])
    else:
        print(even[i], end=", ")

print("\n")
print("--------------------------")


#3

def my_func(num):
    d = (x for x in range(num + 1))
    for i in d:
        if i % 3 == 0 and i % 4 == 0:
            print(i, end=" ")

n = int(input())
my_func(n)

print("\n")
print("--------------------------")

#4

def fun(num, num2):
    while num <= num2:
        yield num * num
        num += 1

n = int(input())
m = int(input())

ctr = fun(n, m)
for x in ctr:
    print(x, end=" ")

print("\n")
print("--------------------------")

#5

n = int(input())

gen = (x for x in range(n, 0, -1))
for i in gen:
    print(i, end=" ")





