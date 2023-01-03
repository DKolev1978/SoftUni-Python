start = int(input())
end = int(input())
magic_number = int(input())

comb_count = 0
magic_number_condition = False

for x1 in range(start, end + 1):
    for x2 in range(start, end + 1):
        comb_count += 1
        if x1 + x2 == magic_number:
            print(f"Combination N:{comb_count} ({x1} + {x2} = {magic_number})")
            magic_number_condition = True
            break
    if magic_number_condition:
        break

if not magic_number_condition:
    print(f"{comb_count} combinations - neither equals {magic_number}")







