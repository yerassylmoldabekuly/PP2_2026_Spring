#1

def my_func(student):
    return (
        "Name:", student["Name"],
        "He studies at the:", student["uni"],
        "He is", student["Age"], "years old."
    )

my_student = {"Age": 18, "Name": "Yerassyl", "uni": "KBTU"}
print(my_func(my_student))

print("------------------------------------")

#2

def my_func(x, y):
    return x + y

numbers = my_func(10, 3)
print(numbers)

print("------------------------------------")

#3

def check_n(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_n(4))
print(check_n(7))

print("------------------------------------")

#4

def grade(score):
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 75 and score <= 89:
        return "B"
    elif score >= 60 and score <= 74:
        return "C"
    elif score >= 0 and score <= 59:
        return "F"
    else:
        return "Invalid score"

print(grade(95))
print(grade(80))
print(grade(40))
print(grade(150)) #Invalid score

print("------------------------------------")

#5

def login(username, password):
    if len(username) == 0:
        return "Username required"
    elif len(password) < 6:
        return "Password too short"
    elif username == "admin" and password == "123456":
        return "Login successful"
    else:
        return "Invalid password"

print(login("", "123456"))      # Username required
print(login("user", "123"))     # Password too short
print(login("admin", "123456")) # Login successful
print(login("admin", "000000")) # Invalid password