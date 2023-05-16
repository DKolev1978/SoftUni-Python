n = int(input())

matrix = []
position = None

for _ in range(n):
    sub_matrix = list(input())
    matrix.append(sub_matrix)

symbol_needed = input()

for row_index in range(n):
    if position:
        break
    for col_index in range(n):
        if matrix[row_index][col_index] == symbol_needed:
            position = (row_index, col_index)
            break

if position:
    print(position)
else:
    print(f"{symbol_needed} does not occur in the matrix")