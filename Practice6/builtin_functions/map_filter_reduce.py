#1
numbers = [1, 2 ,3, 4, 45]

tripled = list(map(lambda u: u * 3, numbers))
print(*tripled)

even = list(filter(lambda o: o % 2 == 0, numbers))
print(*even)

words = ["apple", "banana", "kiwi", "cherry", "fig"]
le = list(filter(lambda s: len(s) > 5, words))
print(le)

#2

from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda c, d: c * d, numbers)
print(result)

result2 = reduce(lambda e, r: e + r, numbers)
print(result2)


#4
a = 3.14
print(type(a))

x = str(a)
print(type(x))