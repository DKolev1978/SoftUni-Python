stack_parent = []

text = input()

for index in range(len(text)):
    if text[index] == "(":
        stack_parent.append(index)
    elif text[index] == ")":
        start_position = stack_parent.pop()
        end_position = index
        print(text[start_position:end_position + 1])

