def calculation(first, second, third):
    numbers_mult = first * second * third
    return numbers_mult


num1, num2, num3 = int(input()), int(input()), int(input())

if calculation(num1, num2, num3) > 0:
    print("positive")
elif calculation(num1, num2, num3) < 0:
    print("negative")
elif calculation(num1, num2, num3) == 0:
    print("zero")
