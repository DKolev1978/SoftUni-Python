left_pass_num = int(input())
right_pass_num = int(input())
max_num_of_pswds = int(input())

symbol_A_low, symbol_A_high = 35, 55
symbol_B_low, symbol_B_high = 64, 96

counter_A, counter_B = symbol_A_low, symbol_B_low

for x in range(1, left_pass_num + 1):
    for y in range(1, right_pass_num + 1):

        max_num_of_pswds -= 1

        if max_num_of_pswds < 0:
            break

        print(f"{chr(counter_A)}{chr(counter_B)}{x}{y}{chr(counter_B)}{chr(counter_A)}", end="|")

        counter_A += 1

        if counter_A > symbol_A_high:
            counter_A = symbol_A_low

        counter_B += 1

        if counter_B > symbol_B_high:
            counter_B = symbol_B_low
