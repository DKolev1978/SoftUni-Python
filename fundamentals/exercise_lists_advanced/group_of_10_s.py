from math import ceil

numbers = [int(num) for num in input().split(", ")]
groups_count = ceil((max(numbers)) / 10)
low_boundary = 1
high_boundary = 10

for idx in range(1, groups_count + 1):
    filtered_numbers = [x for x in numbers if low_boundary <= x <= high_boundary]
    print(f"Group of {10 * idx}'s:  {filtered_numbers}")
    low_boundary += 10
    high_boundary += 10


