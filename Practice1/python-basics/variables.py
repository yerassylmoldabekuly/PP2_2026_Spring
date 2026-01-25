#1
x = 5
y = 'Yerassyl'
print(x)
print(y)
print("--------------------------------------------------")

#2 casting
a = int(4)
b = str(4)
c = float(4)
print(a, b, c)
print(type(a))
print(type(b))
print(type(c))
print("--------------------------------------------------")

#3
q, w, e = "Apple", "Banana", "Orange"
print(q + w + e)
print(q, w, e)
print("--------------------------------------------------")

#4 unpacking
fruits = ["Apple", "Banana", "Orange"]
x, y, z = fruits
print(x)
print(y)
print(z)
print("--------------------------------------------------")

#5 global variable
x = 'cool'

def myfunc():
    global x
    x = 'fantastic'

myfunc()
print("KBTU is " + x)