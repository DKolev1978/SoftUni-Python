n = int(input())
matrix = [list(input()) for _ in range(n)]

# a = [-2, -1, 1, 2]
# positions = [(x, y) for x in a for y in a if abs(x) != abs(y)]
positions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, 1),
    (2, -1),
    (1, 2),
    (1, -2)
)

removed_k = 0

while True:
    max_attacks = 0
    k_with_most_attacks_pos = []

    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "K":
                attacks = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < n and 0 <= pos_col < n:
                        if matrix[pos_row][pos_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    k_with_most_attacks_pos = [row, col]
                    max_attacks = attacks

    if k_with_most_attacks_pos:
        r, c = k_with_most_attacks_pos
        matrix[r][c] = "0"
        removed_k += 1
    else:
        break

print(removed_k)