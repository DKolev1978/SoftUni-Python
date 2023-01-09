budget = float(input())
season = input()
car_price = 0
class_car = ""
type_car = ""
if budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        car_price = budget * 35 / 100
    elif season == "Winter":
        type_car = "Jeep"
        car_price = budget * 65 / 100
elif budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        car_price = budget * 45 / 100
    elif season == "Winter":
        type_car = "Jeep"
        car_price = budget * 80 / 100
elif budget > 500:
    class_car = "Luxury class"
    type_car = "Jeep"
    car_price = budget * 90 / 100

print(f"{class_car}")
print(f"{type_car} - {car_price:.2f}")

