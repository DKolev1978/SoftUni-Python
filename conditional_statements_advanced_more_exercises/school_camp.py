season = input()
group_kind = input()
students_count = int(input())
sleep_count = int(input())
sport = ""
price = 0

if season == "Winter":
    if group_kind == "girls":
        sport = "Gymnastics"
    elif group_kind == "boys":
        sport = "Judo"
    elif group_kind == "mixed":
        sport = "Ski"
elif season == "Spring":
    if group_kind == "girls":
        sport = "Athletics"
    elif group_kind == "boys":
        sport = "Tennis"
    elif group_kind == "mixed":
        sport = "Cycling"
elif season == "Summer":
    if group_kind == "girls":
        sport = "Volleyball"
    elif group_kind == "boys":
        sport = "Football"
    elif group_kind == "mixed":
        sport = "Swimming"
if season == "Winter":
    if group_kind == "mixed":
        price = 10 * students_count
    else:
        price = 9.60 * students_count
elif season == "Spring":
    if group_kind == "mixed":
        price = 9.50 * students_count
    else:
        price = 7.20 * students_count
elif season == "Summer":
    if group_kind == "mixed":
        price = 20 * students_count
    else:
        price = 15 * students_count

if students_count < 10:
    price = price
elif students_count < 20:
    price = price - price * 0.05
elif students_count < 50:
    price = price - price * 0.15
elif students_count >= 50:
    price = price - price * 0.50

total_price = price * sleep_count
print(f"{sport} {total_price:.2f} lv.")