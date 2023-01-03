expected_money = int(input())
collected_money = 0
payment_counter = 0
cash, card = 0, 0
cash_counter, card_counter = 0, 0
flag = False
while True:
    user_input = input()
    if user_input == "End":
        break
    else:
        payment_counter += 1
        product_price = int(user_input)
    if payment_counter % 2 == 0:
        if product_price < 10:
            print("Error in transaction!")
        else:
            card_counter += 1
            card += product_price
            print("Product sold!")
    else:
        if product_price > 100:
            print("Error in transaction!")
        else:
            cash_counter += 1
            cash += product_price
            print("Product sold!")
    collected_money = cash + card

    if collected_money >= expected_money:
        flag = True
        break
if flag:
    print(f"Average CS: {(cash / cash_counter):.2f}")
    print(f"Average CC: {(card / card_counter):.2f}")
else:
    print("Failed to collect required money for charity.")



