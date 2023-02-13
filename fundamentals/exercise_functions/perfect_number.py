def is_perfect_number(number):
    list_del = []
    new_num = int(number)
    for num in range(1, new_num):
        if new_num % num == 0:
            list_del.append(num)

    return new_num == sum(list_del)


input_number = input()
if is_perfect_number(input_number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
