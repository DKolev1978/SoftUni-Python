########Zero Matrix################
# matrix = []
#
# for row in range(3):
#     matrix.append([])
#     for col in range(3):
#         matrix[row].append(0)
#
# print(matrix)
rows = int(input())
matrix = [[int(x) for x in input().split(", ") if int(x) % 2 == 0] for _ in range(rows)]
print(matrix)