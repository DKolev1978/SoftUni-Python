from collections import deque
people = deque()
quantity = int(input())
name = input()
while name != "Start":
    people.append(name)
    name = input()

command = input()
while command != "End":
    data = command.split()
    if len(data) == 1:
        litters_wanted = int(data[0])

        if quantity >= litters_wanted:
            quantity -= litters_wanted
            person = people.popleft()
            print(f"{person} got water")
        else:
            person = people.popleft()
            print(f"{person} must wait")

    else:
        litters_fill = int(data[1])
        quantity += litters_fill
    command = input()
print(f"{quantity} liters left")




