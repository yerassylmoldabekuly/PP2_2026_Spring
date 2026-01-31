#1

a = 20
b = 10

if a > b: print("a is greater than b")

print("-------------------------------------")

#2

a = 200
b = 11

print("b is greater than a") if b > a else print("a is greater than b")

print("------------------------------")

#3

a = 10
b = 30

bigger = a if a > b else b
print("Bigger is:", bigger)
print("------------------------------")

#4

x = 101
y = 100

max_value = y if y > x else x
print(f"Maximum value: {max_value}")
print("------------------------------")

#5

username = ""

display_name = username if username else "Guest"
print("Welcome", display_name)