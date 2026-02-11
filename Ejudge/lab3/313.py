x = list(map(int, input().split()))

primes = list(filter(lambda a: a > 1 and
            all(a % i != 0 for i in range(2, int(a ** 0.5) + 1)), x))

if not primes:
    print("No primes")

else:
    print(*primes)
