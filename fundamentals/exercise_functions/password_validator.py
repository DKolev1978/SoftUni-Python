while True:
    text = input()
    digits = False
    count = False
    letters = False
    is_valid = False
    digit_count = 0
    password_list = text

    words = []

    for idx in range(len(password_list)):
        words.append(password_list[idx])
    if len(password_list) < 6 or len(password_list) > 10:
        print("Password must be between 6 and 10 characters")

    is_valid = text.isalnum()

    for idx in range(len(words)):
        ascii_new = ord(words[idx])
        if 48 < ascii_new > 57:
            digit_count += 1

        if (ascii_new < 48 or ascii_new > 57) or (ascii_new < 65 or ascii_new > 90) or (ascii_new < 97 or ascii_new > 122):
            letters = True

    if letters:
        print("Password must consist only of letters and digits")
    if digits < 2:
        print("Password must have at least 2 digits")

    if is_valid and not letters:
        print("Password is valid")
        break









