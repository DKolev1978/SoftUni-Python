def shopping_list(number: int, **shop_list):
    budget = number
    bay_product = 0
    if budget < 100:
        return "You do not have enough budget."

    for key, val in shop_list.items():
        if bay_product > 5 or not shop_list:
            break
        if 



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

