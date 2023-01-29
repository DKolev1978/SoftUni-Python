gift_list = input().split()

while True:
    command_input = input()
    command_args = command_input.split()
    command = command_args[0]
    gift = command_args[1]

    if command_input == "No Money":
        break

    if "OutOfStock" in command_input:
        for idx in range(len(gift_list)):
            if gift_list[idx] == gift:
                gift_list[idx] = "None"
    elif "Required" in command_input:
        idx = int(command_args[2])
        if 0 <= idx < len(gift_list):
            gift_list[idx] = gift
    elif command == "JustInCase":
        gift_list[-1] = gift

for gift in gift_list:
    if gift == "None":
        continue
    else:
        print(gift, end=" ")

