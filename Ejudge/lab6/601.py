n = int(input())
numbers = list(map(int, input().split()))

square = list(map(lambda a: a ** 2, numbers))
print(sum(square))