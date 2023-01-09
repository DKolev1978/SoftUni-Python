width = int(input())
height = int(input())
cake_count = 0
total_cake = width * height

while total_cake >= cake_count:
    cake_pieces = input()
    if cake_pieces == 'STOP':
        break

    cake_pieces = int(cake_pieces)
    cake_count += cake_pieces

diff = abs(cake_count - total_cake)
if total_cake >= cake_count:
    print(f"{diff} pieces are left.")
else:
    print(f"No more cake left! You need {diff} pieces more.")
