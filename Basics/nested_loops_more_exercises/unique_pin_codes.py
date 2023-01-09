left_digit = int(input())
middle_digit = int(input())
right_digit = int(input())

for l in range(2, left_digit + 1, 2):
    for m in range(0, middle_digit + 1):
        for r in range(2, right_digit + 1, 2):
            if m == 2 or m == 3 or m == 5 or m == 7:
                curr_num = l * 100 + m * 10 + r
                if 100 < curr_num < 999:
                    print(f"{l} {m} {r}")