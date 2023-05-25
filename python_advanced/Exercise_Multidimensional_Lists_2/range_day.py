matrix = []
position = []
targets_position = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for r in range(5):
    matrix.append(input().split())

    if 'A' in matrix[r]:
        position = [r, matrix[r].index('A')]

    if 'x' in matrix[r]:
        targets_position = [r, matrix[r].index('x')]


commands_count = int(input())

for _ in range(commands_count):
    com = input().split()

    if "shoot" in com:
        direction = com[1]

        for direction, positions in directions.items():
            row, col = [
                bunny_pos[0] + positions[0],
                bunny_pos[1] + positions[1]
            ]
            path = []
            collected_eggs = 0



print(*matrix, sep="\n")
