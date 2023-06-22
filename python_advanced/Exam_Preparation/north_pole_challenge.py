size = [int(x) for x in input().split(", ")]
rows, columns = size[0], size[1]

matrix = []
santa_position = []

directions = {
    "up": lambda r, c: [(r - 1) % rows, c],
    "down": lambda r, c: [(r + 1) % rows, c],
    "left": lambda r, c: [r, (c - 1) % rows],
    "right": lambda r, c: [r, (c + 1) % rows],
}

for row in range(rows):
    matrix.append(input().split())

    if "Y" in matrix[row]:
        santa_position = [row, matrix[row].index("Y")]
        matrix[santa_position[0]][santa_position[1]] = "x"

commands = input().split("-")
while commands:
    command = commands[0]
    if command == "End":
        break

    steps = int(commands[1])

    print(command, steps)
    commands = input().split("-")

print(*matrix, sep="\n")
