type_coffee = input()
sugar = input()
count = int(input())
price = 0

if type_coffee == "Espresso":
    if sugar == "Without":
        price = count * 0.90
        price = price - price * 0.35
    elif sugar == "Normal":
        price = count * 1
    elif sugar == "Extra":
        price = count * 1.20
    if count >= 5:
        price = price - price * 0.25
elif type_coffee == "Cappuccino":
    if sugar == "Without":
        price = count * 1
        price = price - price * 0.35
    elif sugar == "Normal":
        price = count * 1.2
    elif sugar == "Extra":
        price = count * 1.60
elif type_coffee == "Tea":
    if sugar == "Without":
        price = count * 0.50
        price = price - price * 0.35
    elif sugar == "Normal":
        price = count * 0.60
    elif sugar == "Extra":
        price = count * 0.70
if price > 15:
    price = price - price * 0.20
print(f"You bought {count} cups of {type_coffee} for {price:.2f} lv.")





