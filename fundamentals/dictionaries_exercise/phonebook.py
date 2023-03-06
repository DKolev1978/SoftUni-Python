phonebook = {}
n = 0
while True:
    line_input = input()
    parts = line_input.split("-")
    if len(parts) == 1:
        n = int(line_input)
        break

    name = parts[0]
    number = parts[1]

    phonebook[name] = number

for _ in range(n):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")









