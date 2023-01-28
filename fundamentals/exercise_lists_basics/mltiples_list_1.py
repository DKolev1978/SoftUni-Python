factor = int(input())
count = int(input())

element = 0
result = []

for _ in range(count):
    element += factor
    result.append(element)
print(result)
