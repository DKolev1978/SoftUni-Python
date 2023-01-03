number_locations = int(input())
flag = False

while number_locations > 0:
    expected_gold_digg = float(input())
    number_of_days_for_digg = int(input())
    sum_digg_gold = 0
    days_counter = number_of_days_for_digg
    while True:
        gold_digg_day = float(input())
        sum_digg_gold = sum_digg_gold + gold_digg_day
        days_counter -= 1

        if days_counter == 0:
            flag = True
            break
    average_gold_dig = sum_digg_gold / number_of_days_for_digg
    number_locations -= 1
    if average_gold_dig >= expected_gold_digg:
        print(f"Good job! Average gold per day: {average_gold_dig:.2f}.")
    else:
        print(f"You need {expected_gold_digg - average_gold_dig:.2f} gold.")







