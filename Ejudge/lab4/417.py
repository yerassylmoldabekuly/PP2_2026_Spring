import math


def solve():
    try:
        R = float(input())
        x1, y1 = map(float, input().split())
        x2, y2 = map(float, input().split())
    except EOFError:
        return

    dx = x2 - x1
    dy = y2 - y1


    a = dx ** 2 + dy ** 2


    if a == 0:
        print(f"{math.sqrt(x1 ** 2 + y1 ** 2) <= R and 0.0 or 0.0:.10f}")
        return

    b = 2 * (x1 * dx + y1 * dy)
    c = x1 ** 2 + y1 ** 2 - R ** 2

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        print(f"{0.0:.10f}")
    else:

        sqrt_d = math.sqrt(discriminant)
        t1 = (-b - sqrt_d) / (2 * a)
        t2 = (-b + sqrt_d) / (2 * a)


        t_start = max(0, min(t1, t2))
        t_end = min(1, max(t1, t2))

        if t_start < t_end:
            segment_length = (t_end - t_start) * math.sqrt(a)
            print(f"{segment_length:.10f}")
        else:
            print(f"{0.0:.10f}")


solve()