given_key = [int(i) for i in input().split()]
text = input()


while text != "find":
    counter = 0
    message = ""
    for letter in text:
        letter_as_digit = ord(letter)
        new_letter = letter_as_digit - given_key[counter]
        message += chr(new_letter)
        counter += 1
        if counter == len(given_key):
            counter = 0

    start = message.find("&") + 1
    end = message.find("&", start)
    type_treasure = message[start:end]
    start_cor = message.find("<") + 1
    end_cor = message.find(">")
    coordinates = message[start_cor:end_cor]
    print(f"Found {type_treasure} at {coordinates}")
    text = input()




