N = int(input("Введіть межу: "))

primes = [i for i in range(2, N + 1) if all(i % j != 0 for j in range(2, i))]

print(primes)
