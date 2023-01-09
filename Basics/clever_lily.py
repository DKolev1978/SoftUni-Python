age = int(input())
price_washing_machine = float(input())
toy_price = int(input())
toy_count = 0
saved_money = 0
total_sum = 0
brother_count = 0
for i in range(1, age + 1):
    if i % 2 != 0:
        toy_count += 1
    else:
        brother_count += 1
        saved_money += 10
        total_sum += saved_money

total_money = (total_sum + (toy_count * toy_price)) - brother_count

diff = abs(price_washing_machine - total_money)

if total_money >= price_washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")

