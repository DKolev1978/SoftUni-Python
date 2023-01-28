n = int(input())

numbers_list = []
filtered_list = []

for _ in range(n):
    number = int(input())
    numbers_list.append(number)

command = input()
if command == "even":
    for num in numbers_list:
        if num % 2 == 0:
            filtered_list.append(num)

if command == "odd":
    for num in numbers_list:
        if num % 2 != 0:
            filtered_list.append(num)

if command == "negative":
    for num in numbers_list:
        if num < 0:
            filtered_list.append(num)

if command == "positive":
    for num in numbers_list:
        if num >= 0:
            filtered_list.append(num)

print(filtered_list)