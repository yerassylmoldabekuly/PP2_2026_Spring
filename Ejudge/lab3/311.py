class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Pair(self.x + other.x, self.y + other.y)

a1, b1, a2, b2 = map(int, input().split())
p1 = Pair(a1, b1)
p2 = Pair(a2, b2)

result = p1.add(p2)
print(f"Result: {result.x} {result.y}")

