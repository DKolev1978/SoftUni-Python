numbers_comp = tuple(float(x) for x in input().split())

nums_and_occurrences = {}

for el in numbers_comp:
    if el not in nums_and_occurrences:
        nums_and_occurrences[el] = 0

    nums_and_occurrences[el] += 1

[print(f"{key} - {value} times") for key, value in
 nums_and_occurrences.items()]
