control_number = int(input())
control_number_counter = 0
flag = False

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a * b + c * d == control_number and a < b and c > d:
                    control_number_counter += 1
                    print(f"{a}{b}{c}{d}", end=" ")
                    if control_number_counter == 4:
                        flag = True
                        first_num, second_num, third_num, forth_num =a, b, c, d
if flag:
    print(f"\nPassword: {first_num}{second_num}{third_num}{forth_num}")
else:
    print("No!")







