#3

fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits, start=1):
    print(f"{i}: {fruit}")

print("-----------------------------------------")

names = ["Alice", "Bob", "Charlie"]
scores = [95, 80, 72]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

pairs = list(zip(names, scores))
print(pairs)

n, s = zip(*pairs)
print(list(n))
print(list(s))