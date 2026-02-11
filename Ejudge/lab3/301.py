x = int(input())

s = str(x)

def if_valid(num):
    b = True
    l = len(num)
    i = 0

    while i < l:
        if int(num[i]) % 2 == 0:
            i += 1
        else:
            b = False
            return "Not valid"

    if b:
        return "Valid"

print(if_valid(s))
