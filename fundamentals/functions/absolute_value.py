numbers_as_string = input().split()

numbers = []

for num in numbers_as_string:
    numbers.append(abs(float(num)))

print(numbers)

