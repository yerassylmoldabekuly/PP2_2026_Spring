import sys
from datetime import date

def parse_moment(line: str) -> int:
    # "YYYY-MM-DD HH:MM:SS UTC±HH:MM"
    d_str, t_str, tz_str = line.strip().split()

    y, m, d = map(int, d_str.split('-'))
    hh, mm, ss = map(int, t_str.split(':'))

    sign = 1 if tz_str[3] == '+' else -1
    off_h, off_m = map(int, tz_str[4:].split(':'))
    offset = sign * (off_h * 3600 + off_m * 60)

    # local seconds from some fixed origin:
    days = date(y, m, d).toordinal()
    local_seconds = days * 86400 + hh * 3600 + mm * 60 + ss

    # UTC = local - offset
    return local_seconds - offset

def main():
    start_line = sys.stdin.readline().strip()
    end_line = sys.stdin.readline().strip()

    start_utc = parse_moment(start_line)
    end_utc = parse_moment(end_line)

    print(end_utc - start_utc)

if __name__ == "__main__":
    main()