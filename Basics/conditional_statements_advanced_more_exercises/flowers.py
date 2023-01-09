chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
seasons = input()
holidays = input()
chrysanthemums_price = 0
roses_price = 0
tulips_price = 0
all_flowers_price = 0
flowers_count = chrysanthemums_count + roses_count + tulips_count

if seasons == 'Spring':
    chrysanthemums_price = chrysanthemums_count * 2
    roses_price = roses_count * 4.10
    tulips_price = tulips_count * 2.50
    all_flowers_price = chrysanthemums_price + roses_price + tulips_price
    if tulips_count >= 7:
        all_flowers_price = all_flowers_price - all_flowers_price * 5 / 100
elif seasons == 'Summer':
    chrysanthemums_price = chrysanthemums_count * 2
    roses_price = roses_count * 4.10
    tulips_price = tulips_count * 2.50
    all_flowers_price = chrysanthemums_price + roses_price + tulips_price
elif seasons == 'Autumn':
    chrysanthemums_price = chrysanthemums_count * 3.75
    roses_price = roses_count * 4.50
    tulips_price = tulips_count * 4.15
    all_flowers_price = chrysanthemums_price + roses_price + tulips_price
elif seasons == 'Winter':
    chrysanthemums_price = chrysanthemums_count * 3.75
    roses_price = roses_count * 4.50
    tulips_price = tulips_count * 4.15
    all_flowers_price = chrysanthemums_price + roses_price + tulips_price
    if roses_count >= 10:
        all_flowers_price = all_flowers_price - all_flowers_price * 10 / 100
if flowers_count >= 20:
    all_flowers_price = all_flowers_price - all_flowers_price * 20 / 100

if holidays == 'Y':
    all_flowers_price = all_flowers_price + all_flowers_price * 15 / 100
all_flowers_price += 2

print(f'{all_flowers_price:.2f}')

