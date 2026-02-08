"""
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.
"""

#1

x = lambda a : a * 5
print(x(10))

print("--------------------------------")

#2

x = lambda a, b, c : a + b + c
print(x(10, 5, 4))

print("--------------------------------")

#3

def my_func(num):
    return lambda a : a * num

mydoubler = my_func(2)
print(mydoubler(10))

print("--------------------------------")

#4

def power(num):
    return lambda a : a ** num

number = power(3)
print(number(2))


