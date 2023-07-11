text = int(input())

directions = {
    "up": lambda r, c: [(r - 1) % SIZE, c],
    "down": lambda r, c: [(r + 1) % SIZE, c],
    "left": lambda r, c: [r, (c - 1) % SIZE],
    "right": lambda r, c: [r, (c + 1) % SIZE],
}


directions_simple = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
n = int(input())

easter_matrix = []
bunny_position = []
best_path = []

best_direction = None
max_coll_eggs = 0

for r in range(n):
    easter_matrix.append(input().split())

    if 'B' in easter_matrix[r]:
        bunny_pos = [r, easter_matrix[r].index('B')]