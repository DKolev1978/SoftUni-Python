leva_1_count = int(input())
leva_2_count = int(input())
leva_5_count = int(input())
total_amount = int(input())


for leva_1 in range(0, leva_1_count + 1):
    for leva_2 in range(0, leva_2_count + 1):
        for leva_5 in range(0, leva_5_count + 1):
            if (leva_1 * 1 + leva_2 * 2 + leva_5 * 5) == total_amount:
                print(f"{leva_1} * 1 lv. + {leva_2} * 2 lv. + {leva_5} * 5 lv. = {total_amount} lv.")