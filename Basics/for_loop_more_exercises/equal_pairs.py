import sys

size = int(input())
single_pair_sum = 0
all_pairs_sum = 0
previous_pair_sum = 0
max_diff = -sys.maxsize
iteration_flag = False

for pairs in range(size):
    first_value = int(input())
    second_value = int(input())
    single_pair_sum = first_value + second_value
    if iteration_flag:
        max_diff = abs(single_pair_sum - previous_pair_sum)

    all_pairs_sum += single_pair_sum
    previous_pair_sum = single_pair_sum
    iteration_flag = True

if all_pairs_sum == size * single_pair_sum:
    print(f"Yes, value={single_pair_sum}")
else:
    print(f"No, maxdiff={max_diff}")