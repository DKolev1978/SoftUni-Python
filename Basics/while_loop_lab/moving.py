width_place = int(input())
length_place = int(input())
height_place = int(input())

available_space = width_place * length_place * height_place
box_count = 0

while box_count <= available_space:
    n = input()
    if n == 'Done':
        break

    n = int(n)
    box_count += n

diff = abs(box_count - available_space)

if available_space >= box_count:
    print(f"{diff} Cubic meters left.")
else:
    print(f"No more free space! You need {diff} Cubic meters more.")




