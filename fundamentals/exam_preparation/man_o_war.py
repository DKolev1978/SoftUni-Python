def is_valid(index, seq):
    return 0 <= index < len(seq)


pirate_ship = [int(x) for x in input().split(">")]
war_ship = [int(x) for x in input().split(">")]
max_health = int(input())
is_running = True
while is_running:
    line = input()
    if line == "Retire":
        break

    command_args = line.split()
    command = command_args[0]

    if command == "Fire":
        idx = int(command_args[1])
        damage = int(command_args[2])
        if not is_valid(idx, war_ship):
            continue
        war_ship[idx] -= damage
        if war_ship[idx] <= 0:
            print("You won! The enemy ship has sunken.")
            is_running = False
    elif command == "Defend":
        start_idx = int(command_args[1])
        end_idx = int(command_args[2])
        damage = int(command_args[3])
        if not is_valid(start_idx, pirate_ship) or not is_valid(end_idx, pirate_ship):
            continue
        for idx in range(start_idx, end_idx + 1):
            pirate_ship[idx] -= damage
            if pirate_ship[idx] <= 0:
                print("You lost! The pirate ship has sunken.")
                is_running = False
                break

    elif command == "Repair":
        idx = int(command_args[1])
        health = int(command_args[2])
        if not is_valid(idx, pirate_ship):
            continue
        pirate_ship[idx] = min(max_health, pirate_ship[idx] + health)

    elif command == "Status":
        threshold = max_health * 0.2
        counter = 0
        for section in pirate_ship:
            if section < threshold:
                counter += 1
        print(f"{counter} sections need repair.")
if is_running:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")
