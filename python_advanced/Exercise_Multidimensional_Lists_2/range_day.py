matrix = []
position = []
targets_position = []
targets_hit_positions = []
targets_hit = 0
targets = 0

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
        targets += matrix[r].count('x')

commands_count = int(input())

for _ in range(commands_count):
    com = input().split()

    if "shoot" in com:
        direction = com[1]

        r = position[0] + directions[direction][0]
        c = position[1] + directions[direction][1]

        while 0 <= r < 5 and 0 <= c < 5:
            if matrix[r][c] == 'x':
                matrix[r][c] = '.'
                target_down_pos = [r, c]
            r += directions[direction][0]
            c += directions[direction][1]

        if target_down_pos:
            targets_hit_positions.append(target_down_pos)
            targets_hit += 1

        if targets_hit == targets:
            print(f'Training completed! All {targets} targets hit.')
            break

if targets_hit < targets:
    print(f'Training not completed! {targets - targets_hit} targets left.')  # принтираме неуспешно завършено обучение

print(*targets_hit_positions, sep="\n")
