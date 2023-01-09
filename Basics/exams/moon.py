from math import ceil
speed = float(input()) # average speed
fuel_liters = float(input()) # needed liters for 100 km

hours = ceil(384400 * 2 / speed + 3)
liters_needed = ((384400 * 2) * fuel_liters) / 100
print(f'{hours}')
print(f'{liters_needed:.0f}')
