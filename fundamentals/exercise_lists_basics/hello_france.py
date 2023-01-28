user_input = input().split("|")
budget = float(input())
budget_total = budget

profit = 0.0
new_price = []
price_profit = []

for item in user_input:
    all_types = item.split("->")
    item_type = all_types[0]
    item_price = float(all_types[1])
    if item_type == "Clothes" and (item_price > 50):
        continue
    if item_type == "Shoes" and (item_price > 35):
        continue
    if item_type == "Accessories" and (item_price > 20.50):
        continue
    if item_price < budget:
        budget -= item_price
        new_price.append(item_price)
for i in range(len(new_price)):
    num = float(new_price[i])
    win = num * 40 / 100 + num
    win1 = num * 40 / 100
    profit = profit + win1
    price_profit.append(f"{win:.2f}")
result = ' '.join(str(i) for i in price_profit)
print(result)
print(f"Profit: {profit:.2f}")
enought_money = budget_total + profit
if enought_money > 150.00:
    print("Hello, France!")
else:
    print("Not enough money.")

