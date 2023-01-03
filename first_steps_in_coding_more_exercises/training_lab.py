import math

length = float(input()) * 100     # input in meters * 100 to sm
width = float(input()) * 100

rows = int(length / 120)
columns = int((width - 100) / 70)
workplaces = rows * columns - 3

print(f'{workplaces}')
