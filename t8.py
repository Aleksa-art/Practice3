M = int(input("Введіть кількість рядків: "))
N = int(input("Введіть кількість символів у рядку: "))

for i in range(M):
    for j in range(N):
        print("*", end="")
    print()
