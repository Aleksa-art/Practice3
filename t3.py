limit = int(input()) + 1
sum = 0

for i in range(limit):
    if i == 0:
        continue
    else:
        sum += i
print(sum)
