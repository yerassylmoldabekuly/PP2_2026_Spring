"""
Using Lambda with sorted()
The sorted() function can use a lambda as a key for custom sorting:
"""

#1
students = [("Anna", 18), ("Joe", 15), ("Williams", 19)]

sorted_students = sorted(students, key=lambda a: a[1])
print(sorted_students)

print("--------------------------------")

#2

words = ["apple", "pie", "banana", "cherry"]

by_len = sorted(words, key=lambda a: len(a))
print(by_len)

print("--------------------------------")

#3

nums = [5, 9, 10, 15, 20, 30, 33]

desc = sorted(nums, key=lambda a: a, reverse=True)
print(desc)

print("--------------------------------")

#4

nums = [-10, 5, -3, 2, -8]

x = sorted(nums, key=lambda a: abs(a))
print(x)
