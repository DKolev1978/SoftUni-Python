number_of_commands = int(input())

parking_lot = set()

for _ in range(number_of_commands):
    command, car_plate = input().split(", ")
    if command == "IN":
        parking_lot.add(car_plate)
    elif command == "OUT" and car_plate in parking_lot:
        parking_lot.remove(car_plate)

if parking_lot:
    for car in parking_lot:
        print(car)
else:
    print("Parking Lot is Empty")


