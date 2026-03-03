import re

#1

pattern = r"ab*"

tests = ["a", "ab", "abbb", "ac", "ba", "b", "aa", "aab", "cabbb"]

for s in tests:
    if re.fullmatch(pattern, s):
        print(s, "-> MATCH")
    else:
        print(s, "-> NO MATCH")

print("-------------------------------------")

#2

pattern = "ab{2,3}"

tests = ["abb", "abbb", "a", "ab", "abbbb", "acb", "zabb", "abbz"]

for t in tests:
    if re.fullmatch(pattern, t):
        print(t, "-> MATCH")
    else:
        print(t, "-> NO MATCH")

print("-------------------------------------")

#3

pattern = r"\b[a-z]+_[a-z]+\b"
text = "a_c asd_cc AA__cc AA-C_"

matches = re.findall(pattern, text)
print("Matches:", matches)

print("-------------------------------------")
#4

pattern2 = f"^[A-Z][a-z]+$"
tests = ["Hello", "H", "HELLO", "Hello123", "hello", "HeLlo"]

for p in tests:
    print(p, "-->", bool(re.findall(pattern2, p)))

print("-------------------------------------")

#5

pattern = r"^a.*b$"

tests = ["ab", "acb", "a123b", "a_b", "aBBBb", "ba", "abc", "a123bc"]
for t in tests:
    if re.fullmatch(pattern, t):
        print(t, "--> MATCH")
    else:
        print(t, "--> NO MATCH")

print("-------------------------------------")
#6

text = " sdfsfrewf 67.,232"

result = re.sub(r"[ ,.]", ":", text)
print(result)

print("-------------------------------------")

#7

text = "_hello_world_how_are_u"

camel = re.sub(r"_([a-zA-Z0-9])", lambda m: m.group(1).upper(), text)
print(camel)

print("-------------------------------------")

#8

text = "HelloWorldUSA"

result = re.split(r"(?<!^)(?=[A-Z])", text)
print(result)

print("-------------------------------------")
#9

s = "HelloWorldUSA"
result = re.sub(r"(?<!^)(?=[A-Z])", " ", s)
print(result)

print("-------------------------------------")

#10

camel = "HelloWorldHowAreU"

snake = re.sub(r"(?<!^)(?=[A-Z])", "_", camel).lower()
print(snake)








