def shopping_list(number: int, **shop_list):
    budget = number
    bay_product = 0
    if budget < 100:
        return "You do not have enough budget."

    for key, val in shop_list.items():
        for v in val:
            if budget < 0:
                break
            if bay_product > 5 or not shop_list:
                break
            price, quantity = val
            if price * quantity > budget:
                continue

            price_per_product = price * quantity
            budget -= price_per_product
            return f"You bought {key} for {price_per_product} leva."




print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

