dict = {}
n = int(input())

while n != 0:
    num = input()
    dict[num] = dict.get(num, 0) + 1
    n -= 1

answer = 0

for key, value in dict.items():
    if value == 3:
        answer += 1

print(answer)