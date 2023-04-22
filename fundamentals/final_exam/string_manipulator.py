text = input()

command = input()
while command != "End":
    command_actions = command.split()
    command_text = command_actions[0]
    if command_text == "Translate":
        char, replacement = command_actions[1], command_actions[2]
        text = text.replace(char, replacement)
        print(text)
    elif command_text == "Includes":
        substring = command_actions[1]
        if substring in text:
            print("True")
        else:
            print("False")
    elif command_text == "Start":
        substring = command_actions[1]
        print(text.startswith(substring))
    elif command_text == "Lowercase":
        text = text.lower()
        print(text)
    elif command_text == "FindIndex":
        char = command_actions[1]
        position = text.rindex(char)
        print(position)
    elif command_text == "Remove":
        startIndex, count = int(command_actions[1]), int(command_actions[2])
        length = text[startIndex:(startIndex + count)]
        text = text.replace(length, "", 1)
        print(text)
    command = input()