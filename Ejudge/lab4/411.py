import json
import sys

def apply_patch(source, patch):
    # source и patch — dict
    for key, pval in patch.items():
        # Rule: if patch value is null -> remove from source
        if pval is None:
            if key in source:
                del source[key]
            continue

        # Rule: if key missing in source -> add
        if key not in source:
            source[key] = pval
            continue

        sval = source[key]

        # Rule: if both values are JSON objects -> recurse
        if isinstance(sval, dict) and isinstance(pval, dict):
            apply_patch(sval, pval)
        else:
            # Rule: otherwise replace
            source[key] = pval

def main():
    # read two lines: source, patch
    src_line = sys.stdin.readline().strip()
    patch_line = sys.stdin.readline().strip()

    source = json.loads(src_line) if src_line else {}
    patch = json.loads(patch_line) if patch_line else {}

    apply_patch(source, patch)

    # compact + sorted keys
    print(json.dumps(source, sort_keys=True, separators=(',', ':')))

if __name__ == "__main__":
    main()