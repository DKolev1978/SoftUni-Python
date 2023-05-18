def find_player_position():
    for row in range(rows):
        if "P" in matrix[row]:
            return matrix[row].index("P")


def check_valid_index(row, col, player=False):
    global win
    
    if 0 <= row < rows and 0 <= col < cols:
        return True
    if player:
        win = True


win = False
directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),

}
rows, cols = [int(x) for x in input().split()]

matrix = [list(input()) for _ in range(rows)]

commands = input()

player_row, player_col = find_player_position()
matrix[player_row][player_col] = "."

for command in commands:
    player_movement_row, player_movement_col =  player_row + directions[command][0], player_col + directions[command][1]




