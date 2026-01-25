#1

txt = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."

if "industry" in txt:
    print("Yes, 'industry' is present")
else:
    print("No, it is not")

print("----------------------------")
#2

txt = "Welcome to PP2"
x = txt[3:7]

print("WEL" + x)

print("----------------------------")

#3

txt = " Hello, World! "
print(txt.strip())
print(txt.replace("W", "L"))
print(txt.upper())
print(txt.lower())
print(txt.split())

print("----------------------------")

#4

age = 18
print(f"My name is Yerassyl, and I am {age}")
print(f"for the number: {age}, float number will be as follows: {age:.2f}")

print("----------------------------")

#5

txt = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."

if "lorem" not in txt:
    print(1)
else:
    print(2)