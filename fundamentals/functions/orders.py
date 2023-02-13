order = input()
count = int(input())


def calculate(type_of_drink, quantity):
    total_price = None
    if type_of_drink == "coffee":
        total_price = count * 1.50
    elif type_of_drink == "coke":
        total_price = count * 1.40
    elif type_of_drink == "water":
        total_price = count * 1.00
    elif type_of_drink == "snacks":
        total_price = count * 2.00
    return total_price


result = calculate(order, count)
print(f"{result:.2f}")
