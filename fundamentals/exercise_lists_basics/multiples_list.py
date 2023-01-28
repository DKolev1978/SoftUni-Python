number1 = int(input())
number2 = int(input())

result = []

for num in range(1, number2 + 1):
    result.append(num * number1)

print(result)
