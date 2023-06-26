# def print_row(s, star_c):
#     for row in range(s - star_c):
#         print(" ", end="")
#     for row in range(1, star_c):
#         print("*", end=" ")
#
#     print("*")
#
#
# n = int(input())
#
# for star_count in range(1, n):
#     print_row(n, star_count)
# for star_count in range(n, 0, -1):
#     print_row(n, star_count)

# Without functions

n = int(input())

for count in range(1, n + 1):
    print(' ' * (n - count), end='')
    print(*['*'] * count)

for count in range(n - 1, 0, -1):
    print(' ' * (n - count), end='')
    print(*['*'] * count)
