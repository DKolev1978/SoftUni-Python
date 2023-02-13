def sum_numbers(a,b):
    return a + b


def subtract(a, b):
    return a - b


first = int(input())
second = int(input())
third = int(input())

sum_result = sum_numbers(first, second)
subtract_result = subtract(sum_result, third)

print(subtract_result)


