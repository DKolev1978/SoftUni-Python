budget = float(input())
ticket_type = input()
count_people = int(input())
budget_transport = 0
ticket_price = 0
if ticket_type == 'VIP':
    ticket_price = 499.99
elif ticket_type == 'Normal':
    ticket_price = 249.99
else:
    print('Invalid ticket type')
if 0 < count_people <= 4:
    budget_transport = budget * 0.75
elif count_people <= 9:
    budget_transport = budget * 0.60
elif count_people <= 24:
    budget_transport = budget * 0.50
elif count_people <= 49:
    budget_transport = budget * 0.40
else:
    budget_transport = budget * 0.25
total_ticket_price = ticket_price * count_people
diff = abs(budget - total_ticket_price - budget_transport)
if budget >= (total_ticket_price + budget_transport):
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")






