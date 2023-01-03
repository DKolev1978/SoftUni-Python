game_moves = int(input())

total_score = 0
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0
counter_invalid = 0

for i in range(game_moves):
    number = int(input())
    if 0 <= number <= 9:
        total_score += number * 0.2
        counter_1 += 1
    elif 9 < number <= 19:
        total_score += number * 0.3
        counter_2 += 1
    elif 19 < number <= 29:
        total_score += number * 0.4
        counter_3 += 1
    elif 29 < number <= 39:
        total_score += 50
        counter_4 += 1
    elif 39 < number <= 50:
        total_score += 100
        counter_5 += 1
    else:
        total_score = total_score / 2
        counter_invalid += 1

print(f"{total_score:.2f}")
print(f"From 0 to 9: {counter_1 / game_moves * 100:.2f}%")
print(f"From 10 to 19: {counter_2 / game_moves * 100:.2f}%")
print(f"From 20 to 29: {counter_3 / game_moves * 100:.2f}%")
print(f"From 30 to 39: {counter_4 / game_moves * 100:.2f}%")
print(f"From 40 to 50: {counter_5 / game_moves * 100:.2f}%")
print(f"Invalid numbers: {counter_invalid / game_moves * 100:.2f}%")
