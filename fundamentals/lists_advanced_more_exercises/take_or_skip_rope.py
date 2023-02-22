def even_nums(seq):
    for num in range(len(seq)):
        if num % 2 == 0:
            take_list.append(seq[num])
        else:
            skip_list.append(seq[num])


user_input = input()
message = ''
numbers_list, non_numbers_list, take_list,  skip_list = [], [], [], []

for element in user_input:
    if element.isdigit():
        numbers_list.append(element)
    else:
        non_numbers_list.append(element)
even_nums(numbers_list)
while non_numbers_list:
    if len(non_numbers_list) <= 0 or len(take_list) <= 0 or len(skip_list) <= 0:
        break
    taken = int(take_list[0])
    for idx in range(taken):
        if len(non_numbers_list) <= 0 or len(take_list) <= 0 or len(skip_list) <= 0:
            break
        message += non_numbers_list[0]
        non_numbers_list.pop(0)
    take_list.pop(0)
    skip = int(skip_list[0])
    for idx in range(skip):
        if len(non_numbers_list) <= 0 or len(take_list) <= 0 or len(skip_list) <= 0:
            break
        non_numbers_list.pop(0)
    skip_list.pop(0)
print(message)



