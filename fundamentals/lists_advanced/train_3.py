train_length = int(input())
train = [0] * train_length
command = input()
while command != "End":
    tokens = command.split(" ")
    key_word = tokens[0]
    if key_word == "add":
        people = int(tokens[1])
        train[-1] += people
    elif key_word == "insert":
        people = int(tokens[2])
        index = int(tokens[1])
        train[index] += people
    elif key_word == "leave":
        people = int(tokens[2])
        index = int(tokens[1])
        train[index] -= people
    command = input()
print(train)
