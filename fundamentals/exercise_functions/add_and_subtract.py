num_1: int = int(input())
num_2 = int(input())
num_3 = int(input())


def sum_numbers(a, b):
    result = num_1 + num_2
    return result


def subtract(a, b):
    result_1 = num_1 + num_2 - num_3
    return result_1


def add_and_subtract(a, b, c):
    subtract(a, b)
    sum_numbers(a, b)


print(subtract(num_1, num_2))

