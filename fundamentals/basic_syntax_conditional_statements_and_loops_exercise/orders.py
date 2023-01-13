n = int(input())
total_price = 0
for _ in range(1, n + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_for_day = int(input())
    if 0.01 <= price_per_capsule <= 100.0 and 1 <= days <= 31 and 1 <= capsules_needed_for_day <= 200:
        order_price = price_per_capsule * capsules_needed_for_day * days
        total_price += order_price
        print(f"The price for the coffee is: ${order_price:.2f}")
print(f"Total: ${total_price:.2f}")

