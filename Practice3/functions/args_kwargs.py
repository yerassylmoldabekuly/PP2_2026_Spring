#1
#The *args parameter allows a function to accept any number of positional arguments.
#Inside the function, args becomes a tuple containing all the passed arguments:


def max_n(*args):
    max_num = args[0]
    for num in args:
        if num > max_num:
            max_num = num
    return max_num

print(max_n(1, 2, 3, 4, 5, 6, 7))

print("------------------------------------")

#2

def my_func(greeting, *args):
    for name in args:
        print(greeting, name)

my_func("Hello", "Yerassyl", "Bekarys", "Darkhan")

print("------------------------------------")

#3

def my_func(*args):
    total = 0
    if len(args) == 0:
        print("None")
    for num in args:
        total += num
    return total

print(my_func(1, 2, 3))
print(my_func(10, 20, 30, 40))
print(my_func(5))

print("------------------------------------")

#4
"""
The **kwargs parameter allows a function to accept any number of keyword arguments.
Inside the function, kwargs becomes a dictionary containing all the keyword arguments:
"""

def my_func(**kwargs):
    print("Name:", kwargs["name"])
    print(kwargs["name"] + "'s age is", kwargs["age"])
    print("He lives in", kwargs["city"])
    print("All data:", kwargs)


my_func(name = "Yerassyl", age = "18", city = "Almaty")

print("------------------------------------")

#5

def my_func(username, **kwargs):
    print("Title:", username)
    print("Additional details:")
    for key, values in kwargs.items():
        print(" ", key + ":", values)


my_func("isa@gmail.com", name = "Islam", age = "20" , hobby = "Football")
