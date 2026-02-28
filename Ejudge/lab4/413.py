import json
import sys
import re

TOKEN_RE = re.compile(r"""
    ([A-Za-z_][A-Za-z0-9_]*)   # key
  | \[(\d+)\]                  # [index]
  | \.                         # dot
""", re.VERBOSE)

NOT_FOUND = object()

def parse_query(q: str):
    tokens = []
    pos = 0
    expect_part = True

    while pos < len(q):
        m = TOKEN_RE.match(q, pos)
        if not m:
            return None

        key, idx = m.group(1), m.group(2)
        chunk = m.group(0)

        if chunk == '.':
            if expect_part:
                return None
            expect_part = True
        elif key is not None:
            if not expect_part:
                return None
            tokens.append(("key", key))
            expect_part = False
        else:  # [idx]
            tokens.append(("idx", int(idx)))
            expect_part = False

        pos = m.end()

    if expect_part:
        return None
    return tokens

def resolve(root, tokens):
    cur = root
    for typ, val in tokens:
        if typ == "key":
            if not isinstance(cur, dict) or val not in cur:
                return NOT_FOUND
            cur = cur[val]
        else:
            if not isinstance(cur, list) or val >= len(cur):
                return NOT_FOUND
            cur = cur[val]
    return cur  # может быть None, это нормально

def dump_compact(x):
    return json.dumps(x, separators=(',', ':'), sort_keys=True)

def main():
    data_line = sys.stdin.readline().strip()
    q_line = sys.stdin.readline().strip()

    J = json.loads(data_line) if data_line else None
    q = int(q_line) if q_line else 0

    for _ in range(q):
        query = sys.stdin.readline().strip()
        tokens = parse_query(query)
        if tokens is None:
            print("NOT_FOUND")
            continue

        value = resolve(J, tokens)
        if value is NOT_FOUND:
            print("NOT_FOUND")
        else:
            print(dump_compact(value))

if __name__ == "__main__":
    main()