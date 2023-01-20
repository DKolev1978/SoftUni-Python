fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
helmet_counter = 0
sword_counter = 0
shield_counter = 0
armor_counter = 0
expenses = 0
for lost in range(1 , fights_count + 1):
    if lost % 2 == 0:
        helmet_counter += 1
    if lost % 3 == 0:
        sword_counter += 1
    if lost % 6 == 0:
        shield_counter += 1
    if lost % 12 == 0:
        armor_counter += 1
    expenses = helmet_price * helmet_counter + sword_price * sword_counter + shield_price * shield_counter + armor_price * armor_counter

print(f"Gladiator expenses: {expenses:.2f} aureus")