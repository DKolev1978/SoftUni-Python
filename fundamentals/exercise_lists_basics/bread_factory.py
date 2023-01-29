user_input = input().split("|")
energy = 100
coins = 100
is_day_completed = True
for el in user_input:
    element = el.split("-")
    if "rest" in element:
        new_energy = int(element[1])
        if energy + new_energy >= 100:
            print("You gained 0 energy.")
        else:
            energy += new_energy
            print(f"You gained {new_energy} energy.")
        print(f"Current energy: {energy}.")
    elif "order" in element:
        energy -= 30
        if energy > 0:
            new_coins = int(element[1])
            print(f"You earned {new_coins} coins.")
            coins += new_coins
        else:
            print("You had to rest!")
            energy += 50
    else:
        ingredient = element[0]
        price = int(element[1])

        if coins - price <= 0:
            print(f"Closed! Cannot afford {ingredient}.")
            is_day_completed = False
            break
        else:
            print(f"You bought {ingredient}.")
            coins -= price

if is_day_completed:
    print(f"Day completed!\n"
          f"Coins: {coins}\n"
          f"Energy: {energy}")

# rest-2|order-10|eggs-100|rest-10