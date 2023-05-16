rows = int(input())
# matrix = [[int(x) for x in input().split(", ") if int(x) % 2 == 0] for _ in range(rows)]
# print(matrix)

flatten = []

for _ in range(rows):
    inner_list = [int(el) for el in input().split(", ")]
    flatten.extend(inner_list)

# for row_index in range(len(matrix)):
#     for col_index in range(len(matrix[row_index])):
#         flatten.append([row_index][col_index])

print(flatten)