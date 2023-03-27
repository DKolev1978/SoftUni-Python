n = int(input())
magic_letters = ["s","t","a","r"]
letter_count = 0

for i in range(n):
    text = input()
    new_message = ""
    for letter in text:
        if letter.lower() in magic_letters:
            letter_count += 1
    for letter in text:
        new_letter = ord(letter) - letter_count
        new_message += chr(new_letter)


    print(new_message)
    print(letter_count)