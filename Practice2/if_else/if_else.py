#1

a = 99
b = 1

if b > a:
    print("b is greater than b")
elif b == a:
    print("b and a are equal")
else:
    print("b is less than a")

print("------------------------------")

#2

a = 200
b = 100

if b > a:
    print("b is greater than b")
else:
    print("a is greater than b")

print("------------------------------")

#3

num = 9

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

print("------------------------------")

#4

temperature = 15

if temperature > 30:
    print("It's hot outside, do not go out!")
elif temperature > 20:
    print("It's warm outside :)")
elif temperature > 10:
    print("It's cool outside")
else:
    print("It's cold outside, wear warm clothes!")

print("------------------------------")

#5

username = "Yerassyl"

if len(username) > 0:
    print(f"U are welcome: {username}")
else:
    print("Error: Username cannot be empty")