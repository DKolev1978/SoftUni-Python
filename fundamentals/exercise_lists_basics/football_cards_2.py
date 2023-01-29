user_input = input().split()

team_count = 11
a_team = []
b_team = []
a_team_red_cards = 0
b_team_red_cards = 0
is_terminated = False

for el in user_input:
    new_el = el.split("-")
    if a_team_red_cards > 4 or b_team_red_cards > 4:
        is_terminated = True
        break

    if new_el in a_team or new_el in b_team:
        continue
    if new_el[0] == "A":
        a_team.append(new_el)
        a_team_red_cards += 1
    else:
        b_team.append(new_el)
        b_team_red_cards += 1


print(f"Team A - {team_count - len(a_team)}; Team B - {team_count - len(b_team)}")
if is_terminated:
    print("Game was terminated")

# A-1 A-5 A-10 B-2
# A-1 A-5 A-10 B-2 A-10 A-7 A-3
# A-1 A-5 A-10 B-2 A-10 A-7 A-3 A-1, B-2
