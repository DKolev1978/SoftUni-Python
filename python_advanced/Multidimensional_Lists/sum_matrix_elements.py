##################Fisrt############################
# rows, columns = [int(x) for x in input().split(", ")]
#
# matrix = []
# matrix_sum = 0
#
# for row in range(rows):
#     lines = [int(x) for x in input().split(", ")]
#     matrix_sum += sum(lines)
#     matrix.append(lines)
#
# print(matrix_sum)
# print(matrix)

rows, columns = [int(x) for x in input().split(", ")]

matrix = []
matrix_sum = 0

for _ in range(rows):
    numbers = [int(x) for x in input().split(", ")]
    matrix.append(numbers)

for row_index in range(rows):
    for col_index in range(columns):
        matrix_sum += matrix[row_index][col_index]

print(matrix_sum)
print(matrix)