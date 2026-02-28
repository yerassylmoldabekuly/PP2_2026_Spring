import sys


def solve():
    try:
        line1 = sys.stdin.readline().split()
        if not line1: return
        x1, y1 = map(float, line1)

        line2 = sys.stdin.readline().split()
        if not line2: return
        x2, y2 = map(float, line2)
    except ValueError:
        return

    total_y = abs(y1) + abs(y2)

    if total_y == 0:
        res_x = x1
    else:
        res_x = x1 + (x2 - x1) * (abs(y1) / total_y)

    print(f"{res_x:.10f} {0.0:.10f}")


if __name__ == "__main__":
    solve()