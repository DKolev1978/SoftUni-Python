products_by_price = {}
products_by_quantity = {}

while True:
    line_input = input()
    if line_input == "buy":
        break

    arguments = line_input.split()
    product = arguments[0]
    price = float(arguments[1])
    quantity = int(arguments[2])
    if product in products_by_price:
        products_by_price[product] = price
        products_by_quantity[product] += quantity
    else:
        products_by_price[product] = price
        products_by_quantity[product] = quantity
for product in products_by_price:
    price = products_by_price[product]
    quantity = products_by_quantity[product]
    total_price = price * quantity
    print(f"{product} -> {total_price:.2f}")

