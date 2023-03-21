import re
numbers = []
while True:
    text = input()
    if not text:
        break
    regex = '\\d+'
    matches = re.findall(regex, text)
    numbers.extend(matches)
print(" ".join(numbers))
# for i in numbers:
#     if i:
#         print(f"{i}", end=" ")
