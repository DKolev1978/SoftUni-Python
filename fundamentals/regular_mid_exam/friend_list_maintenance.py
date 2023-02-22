def is_index_valid(index, seq):
    if 0 <= index < len(seq):
        return True
    return False


friends = input().split(", ")

blacklisted_count = 0
lost_count = 0
while True:
    user_input = input()
    if user_input == "Report":
        break
    commands = user_input.split()
    command = commands[0]
    if command == "Blacklist":
        user = commands[1]
        if user in friends:
            idx = friends.index(user)
            friends.pop(idx)
            friends.insert(idx, "Blacklisted")
            blacklisted_count += 1
            print(f"{user} was blacklisted.")
        else:
            print(f"{user} was not found.")
    elif command == "Error":
        idx = int(commands[1])
        if is_index_valid(idx, friends):
            if friends[idx] != "Blacklisted" and friends[idx] != "Lost":
                user = friends[idx]
                friends.pop(idx)
                friends.insert(idx, "Lost")
                lost_count += 1
                print(f"{user} was lost due to an error.")
        else:
            continue
    elif command == "Change":
        idx = int(commands[1])
        new_name = commands[2]
        if is_index_valid(idx, friends):
            current_name = friends[idx]
            friends.pop(idx)
            friends.insert(idx, new_name)
            print(f"{current_name} changed his username to {new_name}.")
        else:
            continue
print(f"Blacklisted names: {blacklisted_count}")
print(f"Lost names: {lost_count}")
print(' '.join(friends), end='')