input_elements = input().split(" ")

a_team_cards = []
b_team_cards = []
should_terminate = False
for card in input_elements:
    if card in a_team_cards or card in b_team_cards:
        continue

    card_args = card.split("-")
    team_name = card[0]
    player_number = card_args[1]

    if team_name == "A":
        a_team_cards.append(card)
    else:
        b_team_cards.append(card)

    if len(a_team_cards) > 4 or len(b_team_cards) > 4:
        should_terminate = True
        break

initial_player_count = 11

print(f"Team A - {initial_player_count - len(a_team_cards)}; Team B - {initial_player_count - len(b_team_cards)}")
if should_terminate:
    print("Game was terminated")