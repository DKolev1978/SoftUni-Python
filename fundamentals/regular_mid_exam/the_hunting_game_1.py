days_adventure = int(input())
number_players = int(input())
energy = float(input())
water_per_day_one_person = float(input())
food_per_day_one_person = float(input())

total_water = number_players * water_per_day_one_person * days_adventure
total_food = number_players * food_per_day_one_person * days_adventure
is_finish = True
for day in range(1, days_adventure + 1):
    energy_lost = float(input())
    energy -= energy_lost
    if energy <= 0:
        is_finish = False
        break
    if day % 2 == 0:
        energy += energy * 0.05
        total_water = total_water - total_water * 0.30
    if day % 3 == 0:
        energy += energy * 0.10
        total_food = total_food - (total_food / number_players)

if is_finish:
    print(f"You are ready for the quest. You will be left with - {energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")