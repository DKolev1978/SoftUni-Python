from string import ascii_letters, digits
usernames = input().split(", ")
allowed_chars = ascii_letters + digits + "-" + "_"
valid_usernames = ""
for username in usernames:
    if len(username) < 3 or len(username) > 16:
        continue

    # forbidden_letter = False
    # for letter in username:
    #     if letter not in allowed_chars:
    #         forbidden_letter = True
    #         break
    temp = [letter in allowed_chars for letter in username]
    forbidden_letter = all(temp)
    if not forbidden_letter:
        continue

    print(username)





