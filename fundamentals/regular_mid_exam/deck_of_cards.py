def is_index_valid(index, seq):
    if 0 <= index < len(seq):
        return True
    return False


list_of_cards = input().split(", ")
number_commands = int(input())

for idx in range(1, number_commands + 1):
    user_input = input().split(", ")
    command = user_input[0]
    if command == "Add":
        card = user_input[1]
        if card not in list_of_cards:
            list_of_cards.append(card)
            print("Card successfully added")
        else:
            print("Card is already in the deck")
    elif command == "Remove":
        card = user_input[1]
        if card in list_of_cards:
            list_of_cards.remove(card)
            print("Card successfully removed")
        else:
            print("Card not found")
    elif command == "Remove At":
        idx = int(user_input[1])
        if not is_index_valid(idx, list_of_cards):
            print("Index out of range")
        else:
            list_of_cards.pop(idx)
            print("Card successfully removed")
    elif command == "Insert":
        idx = int(user_input[1])
        card_name = user_input[2]
        if not is_index_valid(idx, list_of_cards):
            print("Index out of range")
        else:
            if card_name in list_of_cards:
                print("Card is already added")
            else:
                list_of_cards.insert(idx, card_name)
                print("Card successfully added")


print(*list_of_cards, sep=", ")



