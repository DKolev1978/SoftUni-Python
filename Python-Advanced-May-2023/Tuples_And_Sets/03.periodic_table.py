table = set()

for _ in range(int(input())):  # 4
    for el in input().split():  # ["O", "H"...]
        table.add(el)

print(*table, sep="\n")
