number_of_guests = int(input())

reservation_list = set()

for _ in range(number_of_guests):
    reservation_num = input()
    reservation_list.add(reservation_num)

guest_reservation_num = input()
while guest_reservation_num != "END":
    if guest_reservation_num in reservation_list:
        reservation_list.remove(guest_reservation_num)
    guest_reservation_num = input()

print(len(reservation_list))
for num in sorted(reservation_list):
    print(num)
