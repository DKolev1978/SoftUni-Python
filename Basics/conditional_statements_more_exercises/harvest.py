from math import floor, ceil

x = int(input())    # square meters vineyard
y = float(input())  # grape for one square meter
z = int(input())    # vine needed
count_workers = int(input())

total_grape = x * y
total_grape_vine = total_grape * 0.40 / 2.5
vine_workers = (total_grape_vine - z) / count_workers
diff = abs(total_grape_vine - z)

if total_grape_vine >= z:
    print(f'Good harvest this year! Total wine: {floor(total_grape_vine)} liters.')
    print(f'{ceil(diff)} liters left -> {ceil(vine_workers)} liters per person.')
else:
    print(f'It will be a tough winter! More {floor(diff)} liters wine needed.')



