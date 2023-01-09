n = int(input())
total = 0
for i in range(1, n + 1):
    num = int(input())
    total += num
average = total / n
print(f"{average:.2f}")
