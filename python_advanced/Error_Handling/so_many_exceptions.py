numbers_list = [int(x) for x in input().split(", ")]  # 2. int(input()).split(", ")
result = 1

for i in range(len(numbers_list)):   # 3. range(numbers_list):
    number = numbers_list[i]
    if number <= 5:    # 1. Missing ":"
        result *= number
    elif 5 < number <= 10:
        result /= number

print(result)