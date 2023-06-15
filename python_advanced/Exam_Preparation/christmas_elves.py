from collections import deque

elfs = deque([int(x) for x in input().split()])
materials = deque([int(x) for x in input().split()])

total_energy = 0
total_toys = 0
iterations = 0

while elfs and materials:
    elf = elfs.popleft()
    material = materials[-1]

    if elf < 5:
        continue

    iterations += 1
    current_toys_count = 0

    if iterations % 3 == 0:
        material *= 2
        current_toys_count += 1

    if elf >= material:
        total_energy += material
        elf -= material

        if iterations % 5 != 0:
            elf += 1
            current_toys_count += 1
        else:
            current_toys_count = 0

        materials.pop()

    else:
        elf *= 2
        current_toys_count = 0

    total_toys += current_toys_count

    elfs.append(elf)


print(f"Toys: {total_toys}")
print(f"Energy: {total_energy}")

if elfs:
    print(f"Elves left: {', '.join(str(x) for x in elfs)}")

if materials:
    print(f"Boxes left: {', '.join(str(x) for x in materials)}")