parking_validation = {}

number_of_commands = int(input())

for command_index in range(number_of_commands):
    user_input = input().split()
    command = user_input[0]
    name = user_input[1]
    if command == "register":
        plate = user_input[2]
        if name not in parking_validation:
            parking_validation[name] = plate
            print(f"{name} registered {parking_validation[name]} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_validation[name]}")
    elif command == "unregister":
        if name not in parking_validation:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del parking_validation[name]

for key, value in parking_validation.items():
    print(f"{key} => {value}")

# my_dict = {"name1": "Some Name 1", "name2": "Some Name 2"}
# print(my_dict.keys())
