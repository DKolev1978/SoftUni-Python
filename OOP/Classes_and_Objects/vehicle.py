# class Laptop:
#     def __init__(self, name, model) -> str:
#         self.name = name
#         self.model = model
#
#
# my_laptop: Laptop = Laptop("Inspiron 15", "Dell")
# print(my_laptop.name)  # Inspiron 15
# print(my_laptop.model)  # Dell


class Vehicle:
    def __init__(self, mileage, max_speed=150):
        self.max_speed = max_speed
        self.mileage = mileage
        self.gadgets = []


car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)

