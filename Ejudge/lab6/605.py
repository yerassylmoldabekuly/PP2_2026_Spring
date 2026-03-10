s = input()

vowel = any(ch in "aeiouAEIOU" for ch in s)

if vowel:
    print("Yes")
else:
    print("No")