interval_start = int(input())
interval_end = int(input())
magic_number = int(input())

combination_counter = 0
flag = False

for num1 in range(interval_start, interval_end + 1):
    for num2 in range(interval_start, interval_end + 1):
        combination_counter += 1
        if num1 + num2 == magic_number:
            print(f"Combination N:{combination_counter} ({num1} + {num2} = {magic_number})")
            flag = True
            break
        else:
            continue
    if flag:
        break
if flag:
    print()
else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")

