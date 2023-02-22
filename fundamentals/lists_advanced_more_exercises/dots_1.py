def correct_game_field_bounds(row, col):
    if row < 0 or col < 0 or row >= len(game_field) or col >= len(game_field[0]):
        return True


def check_wall_of_game_field(row, col):
    if game_field[row][col] in "-–":
        return True


def check_already_visit(row, col):
    if game_field[row][col] == "v":
        return True


def find_exit(row, col):
    if game_field[row][col] == ".":
        return True


def find_game_field_path(row, col, game_field):
    if correct_game_field_bounds(row, col) or check_wall_of_game_field(row, col) or check_already_visit(row, col):
        return

    path_steps.append(1)

    if find_exit(row, col):
        max_connected_points.append(sum(path_steps))

    game_field[row][col] = "v"
    find_game_field_path(row, col + 1, game_field)  # check right
    find_game_field_path(row, col - 1, game_field)  # check left
    find_game_field_path(row + 1, col, game_field)  # check up
    find_game_field_path(row - 1, col, game_field)  # check down


rows = int(input())
game_field = []
max_connected_points = [0]
for curr_row in range(rows):
    game_field.append(list(input().split()))

range_of_col = len(game_field[0])

for row in range(len(game_field)):
    for col in range(range_of_col):
        path_steps = []
        if not check_wall_of_game_field(row, col):
            find_game_field_path(row, col, game_field)


print(max(max_connected_points))