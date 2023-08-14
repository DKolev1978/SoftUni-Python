def is_index_valid(r, c):
    if 0 <= r < rows and 0 <= c < cols:
        return True

    return False

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

rows, cols = [int(n) for n in input().split()]
matrix = []
pizza_boy_position_starting = []
pizza_rest_position = []
address_position = []

for row_index in range(rows):
    row_data = [c for c in input()]
    if "B" in row_data:
        pizza_boy_position_starting = [row_index, row_data.index("B")]
    elif "P" in row_data:
        pizza_rest_position = [row_index, row_data.index("P")]
    elif "A" in row_data:
        address_position = [row_index, row_data.index("A")]

    matrix.append(row_data)
pizza_boy_position = pizza_boy_position_starting
while True:
    commands = input()
    row, col = pizza_boy_position_starting
    matrix[row][col] = " "
    row = pizza_boy_position[0] + directions[commands][0]
    col = pizza_boy_position[1] + directions[commands][1]

    if is_index_valid(row, col):
        curren_position = [row, col]
        position = matrix[row][col]
        if matrix[row][col] == "*":
            continue
        elif matrix[row][col] == "P":
            matrix[row][col] = "R"
            print("Pizza is collected. 10 minutes for delivery.")
            pizza_boy_position = curren_position

        elif matrix[row][col] == "A":
            matrix[row][col] = "P"
            print("Pizza is delivered on time! Next order...")
            row, col = pizza_boy_position_starting
            matrix[row][col] = "B"
            break
        else:
            matrix[row][col] = "."
            pizza_boy_position = curren_position
    else:
        print("The delivery is late. Order is canceled.")
        break

for row in matrix:
    print(''.join(map(str, row)))
