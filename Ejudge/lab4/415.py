import sys
from datetime import date

def is_leap(y: int) -> bool:
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

def parse_line(s: str):
    d_str, tz_str = s.strip().split()
    y, m, d = map(int, d_str.split('-'))

    sign = 1 if tz_str[3] == '+' else -1
    hh, mm = map(int, tz_str[4:].split(':'))
    offset_seconds = sign * (hh * 3600 + mm * 60)

    return y, m, d, offset_seconds

def utc_seconds_at_local_midnight(y: int, m: int, d: int, offset_seconds: int) -> int:
    days = date(y, m, d).toordinal()
    return days * 86400 - offset_seconds

def birthday_day_in_year(bm: int, bd: int, y: int) -> date:
    if bm == 2 and bd == 29 and not is_leap(y):
        return date(y, 2, 28)
    return date(y, bm, bd)

def main():
    birth_line = sys.stdin.readline().strip()
    now_line = sys.stdin.readline().strip()

    by, bm, bd, birth_offset = parse_line(birth_line)
    ny, nm, nd, now_offset = parse_line(now_line)


    now_utc = utc_seconds_at_local_midnight(ny, nm, nd, now_offset)

    bday_date_this = birthday_day_in_year(bm, bd, ny)
    bday_utc_this = utc_seconds_at_local_midnight(
        bday_date_this.year, bday_date_this.month, bday_date_this.day, birth_offset
    )

    if bday_utc_this < now_utc:
        bday_date_next = birthday_day_in_year(bm, bd, ny + 1)
        bday_utc = utc_seconds_at_local_midnight(
            bday_date_next.year, bday_date_next.month, bday_date_next.day, birth_offset
        )
    else:
        bday_utc = bday_utc_this

    diff = bday_utc - now_utc  # >= 0

    if diff == 0:
        print(0)
    else:
        print((diff + 86399) // 86400)

if __name__ == "__main__":
    main()