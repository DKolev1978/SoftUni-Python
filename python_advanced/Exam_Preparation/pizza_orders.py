from collections import deque

pizza_orders = deque([int(po) for po in input().split(", ") if 0 < int(po) < 11])
employees_pizza = [int(ep) for ep in input().split(", ")]


def processed_pizzas(pizza_orders, employees_pizza):
    total_pizzas_made = 0
    while pizza_orders and employees_pizza:
        while pizza_orders[0] > employees_pizza[-1]:
            total_pizzas_made += employees_pizza[-1]
            pizza_orders[0] = pizza_orders[0] - employees_pizza[-1]
            employees_pizza.pop()

            if not pizza_orders or not employees_pizza:
                return total_pizzas_made

        total_pizzas_made += pizza_orders.popleft()
        employees_pizza.pop()

    return total_pizzas_made


total_pizzas_made = processed_pizzas(pizza_orders, employees_pizza)

if employees_pizza:
    print(f"All orders are successfully completed!\n"
          f"Total pizzas made: {total_pizzas_made}\n"
          f"Employees: {', '.join([str(ep) for ep in employees_pizza])}")
else:
    print(f"Not all orders are completed.\n"
          f"Orders left: {', '.join([str(po) for po in pizza_orders])}")
