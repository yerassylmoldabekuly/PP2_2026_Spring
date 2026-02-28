import sys
from datetime import date

def parse_line(s: str) -> int:
    # s = "YYYY-MM-DD UTC±HH:MM"
    d_str, tz_str = s.strip().split()
    y, m, d = map(int, d_str.split('-'))

    # tz_str = "UTC+03:00" or "UTC-05:30"
    sign = 1 if tz_str[3] == '+' else -1
    hh, mm = map(int, tz_str[4:].split(':'))
    offset_seconds = sign * (hh * 3600 + mm * 60)

    # Convert local midnight to UTC timestamp seconds:
    # local_time = UTC + offset  =>  UTC = local_time - offset
    days = date(y, m, d).toordinal()  # days since 0001-01-01
    utc_seconds = days * 86400 - offset_seconds
    return utc_seconds

def main():
    t1 = parse_line(sys.stdin.readline())
    t2 = parse_line(sys.stdin.readline())
    diff = abs(t1 - t2)
    print(diff // 86400)

if __name__ == "__main__":
    main()