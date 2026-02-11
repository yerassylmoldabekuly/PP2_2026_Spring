x = int(input())

def isUsual(num):

    while True:
        if num % 2 == 0:
            num = num // 2
        elif num % 3 == 0:
            num = num // 3
        elif num % 5 == 0:
            num = num // 5
        elif num == 1:
            return "Yes"
        else:
            return "No"

print(isUsual(x))