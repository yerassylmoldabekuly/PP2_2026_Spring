import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    m = int(data[0])

    g = 0
    n = 0
    l = 0

    idx = 1
    for _ in range(m):
        scope = data[idx]; idx += 1
        x = int(data[idx]); idx += 1

        if scope == "global":
            g += x
        elif scope == "nonlocal":
            n += x
        elif scope == "local":
            l += x

    print(g, n)

if __name__ == "__main__":
    main()