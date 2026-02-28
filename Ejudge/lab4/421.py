import sys
import importlib

def main():
    data = sys.stdin.read().splitlines()
    q = int(data[0])
    for i in range(1, q + 1):
        module_path, attr = data[i].split()

        try:
            mod = importlib.import_module(module_path)
        except Exception:
            print("MODULE_NOT_FOUND")
            continue

        if not hasattr(mod, attr):
            print("ATTRIBUTE_NOT_FOUND")
            continue

        obj = getattr(mod, attr)
        print("CALLABLE" if callable(obj) else "VALUE")

if __name__ == "__main__":
    main()