input_str = input().split()

while True:
    new_string = ""
    command = input()
    if command == "3:1":
        break

    current_input = command.split()
    action = current_input[0]
    first = int(current_input[1])
    last = int(current_input[2])

    if action == "merge":
        if first < 0:
            number_start = 0
        if last >= len(input_str):
            last = len(input_str) - 1
        for i in range(first, last + 1):
            new_string += input_str[i]
        del input_str[first: last + 1]
        input_str.insert(first, new_string)
    elif action == "divide":
        temp_list1 = [[] for i in range(last)]
        list_2 = []
        if (len(input_str[first]) / last) % 2 == 0:
            a = 0
            b = 2
            for i in range(last):
                temp_list1[i].append(input_str[first][a:b])
                a += 2
                b += 2
            input_str.pop(first)
            for i in range(len(temp_list1) - 1, -1, -1):
                input_str.insert(first, temp_list1[i][0])
        else:
            char = len(input_str[first]) // last
            diff = len(input_str[first]) - (char * last)
            for i in range(char * last):
                if i < diff:
                    list_2.append(input_str[first][i:char + i])
                else:
                    list_2.append(input_str[first][i:])
            input_str.pop(first)
            for i in range(len(list_2) - 1, -1, -1):
                input_str.insert(first, list_2[i])

print(' '.join(input_str))