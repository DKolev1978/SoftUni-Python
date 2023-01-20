n = int(input())
result = 0
for car in range(n):
    char = input()
    result += int(ord(char))
print(f"The sum equals: {result}")