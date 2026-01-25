#1

x = 1
y = 1.25
z = 1j    #complex number

print(type(x))
print(type(y))
print(type(z))

print("----------------------------")

#2

y = 1.11
x = 3

f = float(x)
i = int(y)

print(f)
print(i)

print("----------------------------")

#3

t = 4

c = complex(t)
print(c)

print("----------------------------")

#4 scientific number

c = 4e67
print(type(c))
print(c)

print("----------------------------")

#5

import random

print(random.randrange(1, 100))