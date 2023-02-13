num_1: int = int(input())
num_2 = int(input())
num_3 = int(input())


def smallest_of_three_numbers(a, b, c):
    if num_1 < num_2 and num_1 < num_3:
        smallest_num = num_1
    elif num_1 > num_2 and num_2 < num_3:
        smallest_num = num_2
    else:
        smallest_num = num_3
    return smallest_num


result = smallest_of_three_numbers(num_3, num_2, num_3)

print(result)
