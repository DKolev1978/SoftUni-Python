import math


def calculate_position(ma, row, col):
    if row < 0:
        row = len(ma) - 1
    if col < 0:
        col = len(ma) - 1

    if row >= len(ma):
        row = 0
    if col >= len(ma):
        col = 0

    return row, col


n = int(input())
coins = 0
matrix = []
player_position = []
player_path = []
is_winner = True
for row_odx in range(n):
    row_data = input().split()
    if "P" in row_data:
        player_position = [row_odx, row_data.index("P")]
    matrix.append(row_data)

player_path.append(player_position)
while coins < 100:
    command = input()
    current_row, current_col = player_position
    if command == 'up':
        row, col = calculate_position(matrix, current_row - 1, current_col)
    if command == 'down':
        row, col = calculate_position(matrix, current_row + 1, current_col)
    if command == "right":
        row, col = calculate_position(matrix, current_row, current_col + 1)
    if command == 'left':
        row, col = calculate_position(matrix, current_row, current_col - 1)

    matrix[current_row][current_col] = '0'
    if matrix[row][col] == "X":
        coins //= 2
        is_winner = False
        player_path.append(player_position)
        print(f"Game over! You've collected {coins} coins.")
        break

    coins += int(matrix[row][col])

    matrix[row][col] = 'P'
    player_position = [row, col]
    player_path.append(player_position)

if is_winner:
    print(f"You won! You've collected {coins} coins.")
print("Your path:")
[print(step) for step in player_path]