def last_wagon(people):
    train[-1] += people
    return train


def insert(wagon_index, people):
    train[index] += people
    return train


def leave(wagon_index, people):
    train[index] -= people
    return train


number_of_wagons = int(input())

train = [0] * number_of_wagons
command = input()
while command != "End":
    tokens = command.split()
    key_word = tokens[0]
    if key_word == "add":
        people = int(tokens[1])
        last_wagon(people)
    elif key_word == "insert":
        index = int(tokens[1])
        people = int(tokens[2])
        insert(index, people)
    elif key_word == "leave":
        index = int(tokens[1])
        people = int(tokens[2])
        leave(index, people)

    command = input()

print(train)
