import re
import json

#1
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

prices = re.findall(r"Стоимость\n([\d ]+,\d{2})", text)

for i in prices:
    print(i)

print("-------------------------------------")

#2

with open("raw.txt", "r", encoding="utf-8") as f:
    lines = [ln.strip() for ln in f if ln.strip()]

product_names = []
for i in range(len(lines) - 1):
    if re.fullmatch(r"\d+\.", lines[i]):
        name_line = lines[i + 1]
        m = re.match(r"^([^0-9,]+)", name_line)
        name = m.group(1).strip() if m else name_line
        product_names.append(name)
        print(name)

print("-------------------------------------")

#3

total = 0.0

for s in prices:
    x = float(s.replace(" ", "").replace(",", "."))
    total += x

print(total)

print("-------------------------------------")

#4

m = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})", text)
date_time = None
date = None
time = None
if m:
    date = m.group(1)
    time = m.group(2)
    date_time = f"{date} {time}"
    print("Дата:", date)
    print("Время:", time)
else:
    print("Not found")


print("-------------------------------------")

#5

m = re.search(r"(Банковская карта|Наличные|Карта|Cash|Card)\s*:", text)
payment_method = m.group(1)
print(payment_method)
print("-------------------------------------")

#6

result = {
    "prices_after_cost": prices,
    "product_names": product_names,
    "total amount": total,
    "date": date,
    "time": time,
    "payment_method": payment_method

}
print(json.dumps(result, ensure_ascii=False, indent=2))

