def is_index_valid(index, seq):
    if 0 <= index < len(seq):
        return True
    return False


elements = input().split()
user_input = input()
moves = 0
win = False
while user_input != "end":
    if not elements:
        win = True
        break
    moves += 1
    user_input = user_input.split()

    index_1 = int(user_input[0])
    index_2 = int(user_input[1])
    if is_index_valid(index_1, elements) and is_index_valid(index_2, elements):
        if elements[index_1] == elements[index_2]:
            element = elements[index_1]
            print(f"Congrats! You have found matching elements - {element}!")
            if index_1 < index_2:
                del elements[index_2]
                del elements[index_1]
            else:
                del elements[index_1]
                del elements[index_2]
        else:
            print("Try again!")
    elif not is_index_valid(index_1, elements) or not is_index_valid(index_2, elements) or index_1 == index_2:
        position = len(elements) // 2
        element = f"-{moves}a"
        elements.insert(position, element)
        elements.insert(position, element)
        print("Invalid input! Adding additional elements to the board")
    user_input = input()

if win:
    print(f"You have won in {moves} turns!")
else:
    print("Sorry you lose :(")
    print(' '.join(elements), end='')

