import math


def solve_path():
    R = float(input())
    x1, y1 = map(float, input().split())
    x2, y2 = map(float, input().split())


    d1 = math.hypot(x1, y1)
    d2 = math.hypot(x2, y2)


    dx, dy = x2 - x1, y2 - y1
    dist_ab = math.hypot(dx, dy)

    area = abs(x1 * y2 - x2 * y1)
    h = area / dist_ab if dist_ab > 0 else 0

    dot1 = (x2 - x1) * (-x1) + (y2 - y1) * (-y1)
    dot2 = (x1 - x2) * (-x2) + (y1 - y2) * (-y2)

    if h >= R or dot1 <= 0 or dot2 <= 0:
        print(f"{dist_ab:.10f}")
    else:
        L1 = math.sqrt(max(0, d1 ** 2 - R ** 2))
        L2 = math.sqrt(max(0, d2 ** 2 - R ** 2))

        total_angle = math.acos(max(-1, min(1, (x1 * x2 + y1 * y2) / (d1 * d2))))
        alpha1 = math.acos(R / d1)
        alpha2 = math.acos(R / d2)

        arc_len = R * (total_angle - alpha1 - alpha2)
        print(f"{L1 + L2 + arc_len:.10f}")


solve_path()