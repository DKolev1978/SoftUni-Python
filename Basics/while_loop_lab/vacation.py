needed_money = float(input())
initial_money = float(input())

total_money = initial_money
count_days = 0
count_spend = 0

while total_money < needed_money:
    if count_spend >= 5:
        break
    action = input()
    amount_money = float(input())

    count_days += 1

    if action == "spend":
        count_spend += 1
        total_money = total_money - amount_money
        if total_money <0:
            total_money = 0
    elif action == 'save':
        count_spend = 0
        total_money = total_money + amount_money
if count_spend == 5:
    print("You can't save the money.")
    print(f'{count_days}')
else:
    print(f"You saved the money for {count_days} days.")


