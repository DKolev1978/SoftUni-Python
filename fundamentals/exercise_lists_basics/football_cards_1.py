user_input = input().split()
a_team_red_cards = []
b_team_red_cards = []
a_team = 11
b_team = 11
is_terminated = False
for element in user_input:
    new_element = element.split("-")

    if b_team < 7 or a_team < 7:
        is_terminated = True
        break
    if new_element in a_team_red_cards or new_element in b_team_red_cards:
        continue

    if new_element[0] == "A":
        a_team -= 1
        a_team_red_cards.append(new_element)
    else:
        b_team -= 1
        b_team_red_cards.append(new_element)

print(f"Team A - {a_team}; Team B - {b_team}")
if is_terminated:
    print("Game was terminated")
#   A-1 A-5 A-10 B-2
#   A-1 A-1 A-5 A-5 A-10 B-2 B-2 A-10 A-7 A-3 A-1
