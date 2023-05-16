rows, columns = [int(x) for x in input().split(", ")]

matrix = []

for row in range(rows):
    lines = [int(x) for x in input().split()]
    matrix.append(lines)

for col_index in range(columns):
    sum_cols_el = 0
    for row_index in range(rows):
        sum_cols_el += matrix[row_index][col_index]
    print(sum_cols_el)
