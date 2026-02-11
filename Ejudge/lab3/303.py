s = input().strip()

to_digit = {
    "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
    "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8",
    "NIN": "9", "ZER": "0"
}
to_word = {v: k for k, v in to_digit.items()}

ops = "+-*/"
pos = -1
op = ""

for i, ch in enumerate(s):
    if ch in ops:
        pos = i
        op = ch
        break

left = s[:pos]
right = s[pos+1:]


def parse_num(part: str) -> int:
    digits = []
    for i in range(0, len(part), 3):
        triplet = part[i:i+3]
        digits.append(to_digit[triplet])
    return int("".join(digits))

a = parse_num(left)
b = parse_num(right)


if op == "+":
    res = a + b
elif op == "-":
    res = a - b
elif op == "*":
    res = a * b
else:  # "/"
    res = a // b


if res == 0:
    print("ZER")
else:
    out = []
    for ch in str(res):
        out.append(to_word[ch])
    print("".join(out))