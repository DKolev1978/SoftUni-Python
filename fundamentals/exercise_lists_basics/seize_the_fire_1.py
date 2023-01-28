fire_type = input().split("#")
litters = int(input())

processed_cells = []
total_effort = 0
total_fire = 0
for idx in fire_type:
    type_fire = idx.split(" = ")
    test = type_fire[0]
    water = int(type_fire[1])

    if test == "High" and (water < 81 or water > 125):
        continue

    if test == "Medium" and (water < 51 or water > 80):
        continue

    if test == "Low" and (water < 1 or water > 50):
        continue

    if water > litters:
        continue
    litters -= water
    total_effort += water * 0.25
    total_fire += water
    processed_cells.append(water)

print("Cells:")
for cell in processed_cells:
    print(f" - {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")

