password = ""
text = input()
while True:
    command = input()
    if command == "Done":
        print(f"Your password is: {password}")
        break

    if command == "TakeOdd":
        for i in range(len(text)):
            if i % 2 != 0:
                password += text[i]
        print(password)
    if "Cut" in command:
        command = command.split()
        index, length = int(command[1]), int(command[2])
        password = password[:index] + password[index + length:]
        print(password)
    if "Substitute" in command:
        command = command.split()
        substring, substitute = command[1], command[2]
        if substring in password:
            password = password.replace(substring, substitute, )
            print(password)
        else:
            print("Nothing to replace!")



