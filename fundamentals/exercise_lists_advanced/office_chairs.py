n = int(input())
free_chairs = 0
game_on = True

for room in range(1, n + 1):
    command = input().split()
    chars = command[0]
    people = int(command[1])

    if people > len(chars):
        needed_chairs = people - len(chars)
        game_on = False
        print(f"{needed_chairs} more chairs needed in room {room}")
    else:
        free_chars_by_row = len(chars) - people
        free_chairs += free_chars_by_row

if game_on:
    print(f"Game On, {free_chairs} free chairs left")


