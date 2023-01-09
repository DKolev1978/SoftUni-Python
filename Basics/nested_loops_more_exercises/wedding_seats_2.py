next_sector = input()
sector_A_size = int(input())
num_of_odd_seats = int(input())

sector_A = ord("A")
last_sector = ord(next_sector)
first_seat = ord("a")

num_of_even_seats = num_of_odd_seats + 2

total_seats = 0

for sector in range(sector_A, last_sector + 1):
    current_sector = sector
    sector_offset = sector_A_size + (current_sector - sector_A)
    for row in range(1, sector_offset + 1):
        if row % 2 != 0:
            for seat in range(first_seat, first_seat + num_of_odd_seats):
                print(f"{chr(sector)}{row}{chr(seat)}")
                total_seats += 1
        else:
            for seat in range(first_seat, first_seat + num_of_even_seats):
                print(f"{chr(sector)}{row}{chr(seat)}")
                total_seats += 1
print(total_seats)