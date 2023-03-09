recourses = {}
input_line = input()

while input_line != "stop":
    resource = input_line
    quantity = int(input())
    if resource in recourses:
        recourses[resource] += quantity
    else:
        recourses[resource] = quantity

    input_line = input()

for input_line, quantity in recourses.items():
    print(f"{input_line} -> {quantity}")


