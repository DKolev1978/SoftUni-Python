from math import ceil
people_count = int(input())
entrance_price = float(input())
sun_bed_price = float(input())
umbrella_price = float(input())

entrance_price_total = people_count * entrance_price
sun_bed_price_total = ceil((people_count * 0.75)) * sun_bed_price
umbrella_price_total = ceil(people_count / 2) * umbrella_price

total_expenses = entrance_price_total + sun_bed_price_total + umbrella_price_total

print(f"{total_expenses:.2f} lv.")

