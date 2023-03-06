recources = {}

while True:
    resource = input()
    if resource == "stop":
        break

    quantity = int(input())
    if resource in recources:
        recources[resource] += quantity
    else:
        recources[resource] = quantity

for input_line, quantity in recources.items():
    print(f"{input_line} -> {quantity}")

