from collections import deque

monster_armor_values = deque([int(n) for n in input().split(",") if 1 <= int(n) <= 100])
soldier_striking_impact = [int(n) for n in input().split(",") if 1 <= int(n) <= 100]
killed_monsters = 0

while len(monster_armor_values) > 0 or len(soldier_striking_impact) > 0:
    try:
        monster_armor = monster_armor_values.popleft()
        soldier_strike = soldier_striking_impact.pop()
    except IndexError:
        break

    if soldier_strike >= monster_armor:
        soldier_strike -= monster_armor
        killed_monsters += 1
        if soldier_strike == 0:
            continue
        else:
            try:
                soldier_striking_impact[-1] += soldier_strike
            except IndexError:
                break
    if len(soldier_striking_impact) == 0:
        print("The soldier has been defeated.")
        break

    if len(monster_armor_values) == 0:
        print("All monsters have been killed!")

print(f"Total monsters killed: {killed_monsters}")
