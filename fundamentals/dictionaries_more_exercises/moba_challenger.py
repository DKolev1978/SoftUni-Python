player_by_position_and_skill = {}

input_line = input()

while input_line != "Season end":
    if " -> " in input_line:
        player, position, skill = input_line.split(" -> ")
        skill = int(skill)
        if player not in player_by_position_and_skill:
            player_by_position_and_skill[player] = {}
        if position not in player_by_position_and_skill:
            player_by_position_and_skill[player][position] = skill
        elif skill > player_by_position_and_skill[player][position]:
            player_by_position_and_skill[player][position] = skill
    elif " vs " in input_line:
        player1, player2 = input_line.split(" vs ")

    input_line = input()
print(player_by_position_and_skill)
