n = int(input())

alice_matrix = []
alice_position = []
coll_tea = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for r in range(n):
    alice_matrix.append(input().split())

    if 'A' in alice_matrix[r]:
        alice_position = [r, alice_matrix[r].index('A')]
        alice_matrix[alice_position[0]][alice_position[1]] = "*"

while coll_tea < 10:
    direction = input()

    row = alice_position[0] + directions[direction][0]
    col = alice_position[1] + directions[direction][1]

    if not (0 <= row < n and 0 <= col < n):
        break

    alice_position = [row, col]
    position = alice_matrix[row][col]
    alice_matrix[row][col] = '*'

    if position == 'R':
        break

    if position.isdigit():
        coll_tea += int(position)

if coll_tea < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

print(*[' '.join(row) for row in alice_matrix], sep='\n')