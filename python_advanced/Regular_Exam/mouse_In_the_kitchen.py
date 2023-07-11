rows, columns = [int(x) for x in input().split(",")]

matrix = []
mouse_position = []
cheese = 0
no_cheese = []


def is_index_valid(r, c):
    if 0 <= r < rows and 0 <= c < columns:
        return True

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

while True:
    commands = input()
    if commands == "danger":
        print("Mouse will come back later!")
        print_matrix()
        break

    row = mouse_position[0] + directions[commands][0]
    col = mouse_position[1] + directions[commands][1]

    if is_index_valid(row, col):
        curren_position = [row, col]
        position = matrix[row][col]
        if position == "@":
            continue

        if position == "*":
            matrix[mouse_position[0]][mouse_position[1]] = '*'
            matrix[curren_position[0]][curren_position[1]] = "M"
            mouse_position = curren_position
            continue
        elif position == "C":
            matrix[mouse_position[0]][mouse_position[1]] = '*'
            matrix[curren_position[0]][curren_position[1]] = "M"
            mouse_position = curren_position
            cheese -= 1
            if cheese == 0:
                print("Happy mouse! All the cheese is eaten, good night!")
                print_matrix()
                raise SystemExit
        elif position == "T":
            matrix[mouse_position[0]][mouse_position[1]] = '*'
            matrix[curren_position[0]][curren_position[1]] = "M"
            mouse_position = curren_position
            print("Mouse is trapped!")
            print_matrix()
            break

    else:
        print("No more cheese for tonight!")
        print_matrix()
        break


