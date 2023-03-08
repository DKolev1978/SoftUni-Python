resources = {}

while True:
    resource = input()
    if resource == "stop":
        break

    quantity = int(input())
    if resource in resources:
        resources[resource] += quantity
    else:
        resources[resource] = quantity

for input_line, quantity in resources.items():
    print(f"{input_line} -> {quantity}")

