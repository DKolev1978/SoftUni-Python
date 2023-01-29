number = input()

new_list = []
highest = 0
lowest = 1000
no_matches = 0
m_index = 0
for i in number.split(" "):
    new_list.append(int(i))

commands = input()

while commands != "end":
    if "exchange" in commands:
        exchange_list = commands.split(" ")
        exchange_list[-1] = int(exchange_list[-1])
        left_number = len(new_list) - (exchange_list[1] + 1)
        a = exchange_list[-1]
        if left_number < 0 or a < 0:
            print("Invalid index")
        else:
            new_list[:exchange_list[1] + 1], new_list[-left_number:] = new_list[-left_number:], new_list[
                                                                                                :exchange_list[1] + 1]
    elif "max" in commands:
        if commands == "max even":
            for i in new_list:
                if i % 2 == 0 and i > highest:
                    highest = i
                    no_matches += 1
            for i in range(len(new_list) - 1, -1, -1):
                if new_list[i] == highest:
                    m_index = i
                    break
            if no_matches != 0:
                # max_index = new_list.index(highest)
                print(m_index)
        elif commands == "max odd":
            for i in new_list:
                if i % 2 != 0 and i > highest:
                    highest = i
                    no_matches += 1
            for i in range(len(new_list) - 1, -1, -1):
                if new_list[i] == highest:
                    m_index = i
                    break
            if no_matches != 0:
                print(m_index)
        if no_matches == 0:
            print("No matches")

    elif "min" in commands:
        if commands == "min even":
            for i in new_list:
                if i % 2 == 0 and i < lowest:
                    lowest = i
                    no_matches += 1
            for i in range(len(new_list) - 1, -1, -1):
                if new_list[i] == lowest:
                    m_index = i
                    break
            if no_matches != 0:
                print(m_index)
        elif commands == "min odd":
            for i in new_list:
                if i % 2 != 0 and i < lowest:
                    lowest = i
                    no_matches += 1
            for i in range(len(new_list) - 1, -1, -1):
                if new_list[i] == lowest:
                    m_index = i
                    break
            if no_matches != 0:
                print(m_index)
        if no_matches == 0:
            print("No matches")
    elif "first" in commands:
        count = commands.split(" ")
        count[1] = int(count[1])
        counter_list = []
        if count[1] > len(new_list):
            print("Invalid count")
            a = False
        elif count[2] == "even":
            for i in range(len(new_list)):
                if new_list[i] % 2 == 0:
                    counter_list.append(new_list[i])
                    if len(counter_list) == count[1]:
                        break
        else:
            for i in range(len(new_list)):
                if new_list[i] % 2 != 0:
                    counter_list.append(new_list[i])
                    if len(counter_list) == count[1]:
                        break
        if a:
            print(counter_list)
    elif "last" in commands:
        count = commands.split(" ")
        count[1] = int(count[1])
        counter_list = []
        if count[1] > len(new_list):
            print("Invalid count")
            pass
        if count[2] == "even":
            for i in range(len(new_list) - 1, -1, -1):
                if new_list[i] % 2 == 0:
                    counter_list.append(new_list[i])
                    if len(counter_list) == count[1]:
                        break
        elif count[2] == "odd":
            for i in range(len(new_list) - 1, -1, -1):
                if new_list[i] % 2 != 0:
                    counter_list.append(new_list[i])
                    if len(counter_list) == count[1]:
                        break
        elif len(counter_list) != 0:

            counter_list[0], counter_list[1] = counter_list[1], counter_list[0]
        print(counter_list)

    highest = 0
    lowest = 1000
    no_matches = 0
    commands = input()

print(new_list)