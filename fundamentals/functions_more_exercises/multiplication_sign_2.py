def calculation(first, second, third):
    count = 0
    if first == 0 or second == 0 or third == 0:
        count = -1
        return count
    if num1 > 0:
        count += 1
    if num2 > 0:
        count += 1
    if num3 > 0:
        count += 1
    return count


num1, num2, num3 = int(input()), int(input()), int(input())
result = calculation(num1, num2, num3)

if result == -1:
    print("zero")
elif result % 2 == 0:
    print("negative")
elif result % 2 != 0:
    print("positive")

