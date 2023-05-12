# First solution
# number = int(input())
#
# names = set()
#
# for _ in range(number):
#     names.add(input())
#
# print(*names, sep="\n")

# Second solution
print(*{input()for _ in range(int(input()))}, sep="\n")

