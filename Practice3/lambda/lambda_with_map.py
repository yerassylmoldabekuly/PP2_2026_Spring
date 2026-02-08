#1
"""
Using Lambda with map()
The map() function applies a function to every item in an iterable:
"""
import math

numbers = [2, 3, 4, 5, 6, 7]
x = list(map(lambda a : a * 2, numbers))
print(x)

print("--------------------------------")

#2

numbers = [100, 81, 64, 49, 36]
x = list(map(lambda a : math.sqrt(a), numbers))
print(x)

print("--------------------------------")

#3

numbers = [10, 11, 12, 13, 14, 15]
x = list(map(lambda a: a ** 2, numbers))
print(x)

print("--------------------------------")

#4

words = ["c++", "python", "java"]
x = list(map(lambda a : a.upper(), words))
print(x)

print("--------------------------------")

#5

a = [1, 2, 3]
b = [3, 5, 6]

add = list(map(lambda x, y : x + y, a, b))
print(add)
