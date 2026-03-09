import os

#1

os.makedirs("project/data/raw", exist_ok=True)
print("Nested directory created")

print("-------------------------------")
#2

items = os.listdir("project")

for item in items:
    print(item)

print("-------------------------------")

items = os.listdir("project/data")

for item in items:
    print(item)