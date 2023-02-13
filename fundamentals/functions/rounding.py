numbers_to_round = input().split()
rounded_numbers = []


def rounds(a):
    for num in numbers_to_round:
        new_num = round(float(num))
        rounded_numbers.append(new_num)
    return rounded_numbers


print(rounds(numbers_to_round))
