last_sector = input()
a_sector_rows = int(input())
odd_places_count = int(input())
sector_num = ord(last_sector)
sector_A = ord("A")
seat_first = ord("a")
num_of_even_seats = odd_places_count + 2
total_seats = 0
for sector in range(sector_A, sector_num + 1):
    current_sector = sector
    sector_offset = a_sector_rows + (current_sector - sector_A)
    for row in range(1, sector_offset + 1):
        if row % 2 != 0:
            for seat in range(seat_first, seat_first + odd_places_count):
                print(f"{chr(sector)}{row}{chr(seat)}")
                total_seats += 1
        else:
            for seat in range(seat_first, seat_first + num_of_even_seats):
                print(f"{chr(sector)}{row}{chr(seat)}")
                total_seats += 1
print(total_seats)





