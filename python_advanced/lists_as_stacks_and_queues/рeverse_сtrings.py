user_input = list(input())
stack_text = list(user_input)

while stack_text:
    removed_element = stack_text.pop()
    print(removed_element, end='')


