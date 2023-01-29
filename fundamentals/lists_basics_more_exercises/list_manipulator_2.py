string_input = input().split(' ')
list_input = []
a = 1
for i in string_input:
    list_input.append(int(i))

command = input()

while command != 'end':
    command_list = command.split(' ')
    if command_list[0] == 'exchange':
        index_swap = int(command_list[1])
        if index_swap >= len(list_input) or index_swap < 0:
            print('Invalid index')
        else:
            list_1 = list_input[:index_swap + 1]
            list_2 = list_input[index_swap + 1:]
            list_input.clear()
            list_input = list_2 + list_1
    elif command_list[0] == 'max':
        if command_list[1] == 'even':
            max_even = -1
            for place, number in enumerate(list_input):
                if number % 2 == 0 and number >= max_even:
                    max_even = number
                    index_max_even = place
            if max_even == -1:
                print('No matches')
            else:
                print(index_max_even)
        else:
            max_odd = -1
            for place, number in enumerate(list_input):
                if number % 2 == 1 and number >= max_odd:
                    max_odd = number
                    index_max_odd = place
            if max_odd == -1:
                print('No matches')
            else:
                print(index_max_odd)
    elif command_list[0] == 'min':
        if command_list[1] == 'even':
            min_even = 1001
            for place, number in enumerate(list_input):
                if number % 2 == 0 and number <= min_even:
                    min_even = number
                    index_min_even = place
            if min_even == 1001:
                print('No matches')
            else:
                print(index_min_even)
        else:
            min_odd = 1001
            for place, number in enumerate(list_input):
                if number % 2 == 1 and number <= min_odd:
                    min_odd = number
                    index_min_odd = place
            if min_odd == 1001:
                print('No matches')
            else:
                print(index_min_odd)
    elif command_list[0] == 'first':
        list_output = []
        count = int(command_list[1])
        if count > len(list_input) or count < 0:
            print('Invalid count')
        else:
            if command_list[2] == 'even':
                for i in list_input:
                    if count > 0 and i % 2 == 0:
                        list_output.append(i)
                        count = count - 1
                print(list_output)
            elif command_list[2] == 'odd':
                for i in list_input:
                    if count > 0 and i % 2 == 1:
                        list_output.append(i)
                        count = count - 1
                print(list_output)
    elif command_list[0] == 'last':
        list_output = []
        count = int(command_list[1])
        if count > len(list_input) or count < 0:
            print('Invalid count')
        else:
            if command_list[2] == 'even':
                for i in list_input[::-1]:
                    if count > 0 and i % 2 == 0:
                        list_output.append(i)
                        count = count - 1
                list_output.reverse()
                print(list_output)
            elif command_list[2] == 'odd':
                for i in list_input[::-1]:
                    if count > 0 and i % 2 == 1:
                        list_output.append(i)
                        count = count - 1
                list_output.reverse()
                print(list_output)
    command = input()
else:
    print(list_input)