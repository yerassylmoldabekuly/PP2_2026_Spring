"""
Using Lambda with filter()
The filter() function creates a list of items for which a function returns True:

"""
import math
#1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = list(filter(lambda a : a % 2 != 0, numbers))
print(odd_numbers)

print("--------------------------------")
#2

words = ["c++", "python", "JAVA", "Kbtu", "Home"]
x = list(filter(lambda a:  a.islower(), words))
print(x)

print("--------------------------------")
#3

perfect_square = [100, 121, 144, 169, 200, 201]
x = list(filter(lambda a : math.sqrt(a).is_integer(), perfect_square))

print(x)

print("--------------------------------")

#4

nums = [5, 9, 10, 15, 20, 30, 33]
x = list(filter(lambda a: a % 3 == 0 and a % 5 == 0, nums))

print(x)
print("--------------------------------")

#5

names = ["Alice", "bob", "Charlie", "david", "Eve"]
x = list(filter(lambda a : a[0].isupper(), names))

print(x)
