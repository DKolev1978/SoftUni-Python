def is_valid(r,c, matr):
    if 0 <= r < len(matr) and 0 <= c < len(matr):
        return True
    else:
        return False


n = int(input())

matrix = list([int(x) for x in input().split()] for _ in range(n))

command_line = input()
while "END" not in command_line:
    command, row, col, operand = command_line.split()
    if is_valid(int(row), int(col), matrix):
        if command == "Add":
            matrix[int(row)][int(col)] += int(operand)
        elif command == "Subtract":
            matrix[int(row)][int(col)] -= int(operand)
    else:
        print("Invalid coordinates")

    command_line = input()

[print(*row) for row in matrix]
# for el in matrix:
#     print(*el, sep=" ")
