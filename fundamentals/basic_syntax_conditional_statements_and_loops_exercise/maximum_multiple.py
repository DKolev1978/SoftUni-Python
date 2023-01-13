divisor = int(input())
boundary = int(input())
maximum = 0
for num in range(1, boundary + 1):
    if num % divisor == 0:
        maximum = num
print(maximum)
