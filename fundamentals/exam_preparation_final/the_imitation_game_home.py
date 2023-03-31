decrypted_message = ""
while True:
    text = input()
    if text == "Decode":
        break
    if "|" not in text:
        decrypted_message = text
    command = text.split("|")
    if command[0] == "Move":
        number_of_letters = int(command[1])
        decrypted_message = decrypted_message[number_of_letters:] + decrypted_message[:number_of_letters]
    elif command[0] == "Insert":
        index, value = int(command[1]), command[2]
        decrypted_message = decrypted_message[:index] + value + decrypted_message[index:]

    elif command[0] == "ChangeAll":
        substring, replacement = command[1], command[2]
        decrypted_message = decrypted_message.replace(substring, replacement, )

print(f"The decrypted message is: {decrypted_message}")

