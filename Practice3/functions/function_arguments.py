#1

def my_func(fname, sname):
    print(fname + " " + sname)

my_func("Yerassyl", "Moldabekuly") #The order matters with positional arguments

print("------------------------------------")

#2

def my_func(name = "friend"):
    print("Hello, " + name + "!")

my_func("Yerassyl")
my_func()
my_func("Nurassyl")

print("------------------------------------")

#3

def my_func(animal, name):
    print("I have a " + animal)
    print("My animal's name is " + name)
    print("I love my", name ,"among all of the", animal ,"'s")

my_func(name = "Buddy", animal = "cat") #This way, with keyword arguments, the order of the arguments does not matter.
print("------------------------------------")

#4

def my_func(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ["apple", "banana", "strawberry"]
my_func(my_fruits)

print("------------------------------------")

#5

def my_func(x, y):
    return x * y

coordinates = my_func(5, 4)
print(coordinates)



