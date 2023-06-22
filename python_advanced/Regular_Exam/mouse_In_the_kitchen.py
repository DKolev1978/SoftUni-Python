rows, columns = [int(x) for x in input().split(",")]

matrix = []
mouse_position = []
cheese = 0
no_cheese = []


def is_index_valid(r, c):
    if 0 <= r < rows and 0 <= c < columns:
        return True
    else:
        return False


def print_matrix():
    for row in matrix:
        print(''.join(map(str, row)))


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(rows):
    r = [c for c in input()]
    matrix.append(r)
    for el in r:
        count = 0
        if el == "C":
            count += 1
        cheese += count
    if "M" in matrix[row]:
        mouse_position = [row, matrix[row].index('M')]
        matrix[mouse_position[0]][mouse_position[1]] = "*"

commands = input()

while True:
    commands = input()
    if commands == "danger" and cheese > 0:
        print("Mouse will come back later!")
        matrix[current_mouse_position[0]][current_mouse_position[1]] = "M"
        print_matrix()
        break

    current_mouse_position = mouse_position
    row = current_mouse_position[0] + directions[commands][0]
    col = current_mouse_position[1] + directions[commands][1]

    if not is_index_valid(row, col):
        print("No more cheese for tonight!")
        matrix[mouse_position[0]][mouse_position[1]] = "M"
        print_matrix()
        raise SystemExit
    current_mouse_position = [row, col]
    position = matrix[row][col]
    if "@" in position:
        continue
    if "T" in position:
        matrix[current_mouse_position[0]][current_mouse_position[1]] = "M"
        print("Mouse is trapped!")
        print_matrix()
        break
    if "C" in position:
        cheese -= 1
    matrix[current_mouse_position[0]][current_mouse_position[1]] = "*"
    mouse_position = current_mouse_position
    if cheese == 0:
        print("Happy mouse! All the cheese is eaten, good night!")
        matrix[current_mouse_position[0]][current_mouse_position[1]] = "M"
        print_matrix()
        break
