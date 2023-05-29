rows = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []

for r in range(rows):
    temp_matrix = [int(x) for x in input().split(", ")]
    matrix.append(temp_matrix)
    primary_diagonal.append(matrix[r][r])
    secondary_diagonal.append(matrix[r][rows - r - 1])

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
