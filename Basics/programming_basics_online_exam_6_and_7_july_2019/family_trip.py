budget = float(input())
nights = int(input())
price_for_night = float(input())
additional_expenses = float(input())
total_additional_expenses = budget * additional_expenses / 100
total_price = nights * price_for_night
total_expenses = 0
if nights > 7:
    total_price -= 0.05 * total_price
total_expenses = total_price + total_additional_expenses

if budget >= total_expenses:
    print(f"Ivanovi will be left with {budget - total_expenses:.2f} leva after vacation.")
else:
    print(f"{total_expenses - budget:.2f} leva needed.")


