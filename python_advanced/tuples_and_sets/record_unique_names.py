count = int(input())

unique_name = set()

for _ in range(count):
    name = input()
    unique_name.add(name)

print(*unique_name, sep="\n")
