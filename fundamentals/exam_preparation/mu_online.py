game = input().split('|')
initial_health, initial_bitcoins = 100, 0
max_health = initial_health
is_live = True
for idx in range(len(game)):
    legend = game[idx].split()
    command = legend[0]
    if command == "potion":
        health = int(legend[1])
        if initial_health < max_health:
            if initial_health + health > max_health:
                health_added = max_health - initial_health
                initial_health += health_added
            else:
                health_added = health
                initial_health += health_added
            print(f"You healed for {health_added} hp.")
            print(f"Current health: {initial_health} hp.")
        else:
            continue

    elif command == "chest":
        bit_coins = int(legend[1])
        initial_bitcoins += bit_coins
        print(f"You found {bit_coins} bitcoins.")
    else:
        points = int(legend[1])
        initial_health -= points
        if initial_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {idx + 1}")
            is_live = False
            break

if is_live:
    print(f"You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")