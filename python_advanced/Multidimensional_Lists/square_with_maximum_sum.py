rows, cols = [int(el) for el in input().split(", ")]
matrix = []
max_sum = float('-inf')
sub_matrix = []

for _ in range(rows):
    inner_list = [int(el) for el in input().split(", ")]
    matrix.append(inner_list)


for row_index in range(rows - 1):

    for col_index in range(cols - 1):
        current_el = matrix[row_index][col_index]
        element_below = matrix[row_index+1][col_index]
        next_element = matrix[row_index][col_index+1]
        diagonal = matrix[row_index+1][col_index+1]
        cur_sum = current_el + element_below + next_element + diagonal

        if max_sum < cur_sum:
            max_sum = cur_sum
            sub_matrix = [[current_el, next_element], [element_below, diagonal]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)