#1

f = open("input.txt")
print(f.read())

print("------------------------------")

#2

with open("input.txt") as f:
    print(f.read())

print("------------------------------")

#3

with open("input.txt") as f:
    print(f.readline())

