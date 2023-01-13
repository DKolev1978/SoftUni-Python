n = int(input())
total_price = 0
for _ in range(1, n + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_for_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    if capsules_needed_for_day < 1 or capsules_needed_for_day > 2000:
        continue
    order_price = price_per_capsule * capsules_needed_for_day * days
    total_price += order_price
    print(f"The price for the coffee is: ${order_price:.2f}")
print(f"Total: ${total_price:.2f}")

