import sys

max_number = -sys.maxsize
sum_numbers = 0
input_n = int(input())

for i in range(1, input_n + 1):
    num = int(input())
    sum_numbers += num
    if num > max_number:
        max_number = num

other_sum_num = sum_numbers - max_number
if max_number == other_sum_num:
    print('Yes')
    print(f'Sum = {other_sum_num}')
else:
    print('No')
    sum_numbers = sum_numbers - max_number
    print(f'Diff = {abs(max_number - other_sum_num)}')

