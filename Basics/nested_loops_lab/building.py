number_floors = int(input())
number_rooms = int(input())
for f in range(number_floors, 0, -1):
    for r in range(number_rooms):
        if f == number_floors:
            flat_name = f'L{f}{r}'
        elif f % 2 != 0:
            flat_name = f'A{f}{r}'
        elif f % 2 == 0:
            flat_name = f'O{f}{r}'
        print(flat_name, end=' ')
    print()
