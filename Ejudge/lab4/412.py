import json
import sys

MISSING = object()

def to_json_literal(x):
    # compact JSON literal for any JSON value
    return json.dumps(x, separators=(',', ':'), sort_keys=True)

def deep_diff(a, b, path="", out=None):
    if out is None:
        out = []

    # If both are objects (dict), compare by fields recursively
    if isinstance(a, dict) and isinstance(b, dict):
        keys = set(a.keys()) | set(b.keys())
        for k in keys:
            na = a.get(k, MISSING)
            nb = b.get(k, MISSING)
            new_path = f"{path}.{k}" if path else k

            if na is MISSING:
                out.append((new_path, "<missing>", to_json_literal(nb)))
            elif nb is MISSING:
                out.append((new_path, to_json_literal(na), "<missing>"))
            else:
                deep_diff(na, nb, new_path, out)
        return out

    # Not both dicts: if values differ, record this path
    if a != b:
        left = "<missing>" if a is MISSING else to_json_literal(a)
        right = "<missing>" if b is MISSING else to_json_literal(b)
        out.append((path, left, right))

    return out

def main():
    a_line = sys.stdin.readline().strip()
    b_line = sys.stdin.readline().strip()

    A = json.loads(a_line) if a_line else {}
    B = json.loads(b_line) if b_line else {}

    diffs = deep_diff(A, B)

    # sort by path
    diffs.sort(key=lambda t: t[0])

    if not diffs:
        print("No differences")
    else:
        for p, oldv, newv in diffs:
            print(f"{p} : {oldv} -> {newv}")

if __name__ == "__main__":
    main()