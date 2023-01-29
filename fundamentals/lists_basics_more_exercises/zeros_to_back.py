numbers = input().split(", ")
sorted_numbers = []
count = 0
for i in range(len(numbers)):
    sorted_numbers.append(int(numbers[i]))
for num in sorted_numbers:
    if num == 0:
        sorted_numbers.remove(num)
        sorted_numbers.append(num)

print(sorted_numbers)
