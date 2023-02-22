rows = int(input())
user_input = []
count = 0

for num in range(rows):
    user_input.append(input().split())
for el in user_input:
    for i in range(len(el)):
        element = el[i]
        if element == "-":
            continue
        else:
            index = i
            if el[i] == el[-1]:
                continue
            if el[index - 1] == "." or el[index + 1] == ".":
                count += 1
            elif index == 0 and el[index + 1] == ".":
                count += 1

print(count)