number_of_wagons = int(input())

train = [0] * number_of_wagons
command = input()
while command != "End":
    tokens = command.split()
    key_word = tokens[0]
    if key_word == "add":
        people = int(tokens[1])
        train[-1] += people
    elif key_word == "insert":
        index = int(tokens[1])
        people = int(tokens[2])
        train[index] += people
    elif key_word == "leave":
        index = int(tokens[1])
        people = int(tokens[2])
        train[index] -= people

    command = input()

print(train)