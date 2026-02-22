#1

from datetime import date, timedelta

today = date.today()
result = today - timedelta(days=5)

print(today)
print(result)

print("\n")
print("--------------------------")

#2

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print(yesterday.day, today.day, tomorrow.day)

print("\n")
print("--------------------------")

#3

from datetime import datetime

dt = datetime.now()
dt_without_micro = dt.replace(microsecond=0)

print(dt)
print(dt_without_micro)

print("\n")
print("--------------------------")

#4

# Example 2026-02-22 14:30:00
# and     2026-02-22 10:12:00

d1 = input().strip()
d2 = input().strip()

fmt = "%Y-%m-%d %H:%M:%S"
dt1 = datetime.strptime(d1, fmt)
dt2 = datetime.strptime(d2, fmt)

diff_seconds = abs((dt2 - dt1).total_seconds())
print(int(diff_seconds))
