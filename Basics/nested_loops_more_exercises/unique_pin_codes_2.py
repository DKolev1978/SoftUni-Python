left_digit = int(input())
middle_digit = int(input())
right_digit = int(input())

for i in range(2, left_digit + 1, 2):
    for j in range(0, middle_digit + 1, 1):
        for l in range(2, right_digit + 1, 2):
            if j == 2 or j ==3 or j == 5 or j == 7:
                curr_num = i * 100 + j * 10 + l
                if 100 < curr_num < 999:
                    print(f"{i} {j} {l}")