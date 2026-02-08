#1

def my_function():
    print("Hello, Yerassyl!")

my_function()
print("------------------------------------")

#2

def my_func(name):
    return f"Welcome to the KBTU, {name}!"

print(my_func("Yerassyl"))
print(my_func("Erko"))
print(my_func("Asyl"))

print("------------------------------------")

#3

def get_greeting():
    return "What's up bruh?"

message = get_greeting()
print(message)

print("------------------------------------")

#4

def check_age(age):
    if age >= 18:
        pass
    else:
        print("Access denied!")

check_age(18)
check_age(15)