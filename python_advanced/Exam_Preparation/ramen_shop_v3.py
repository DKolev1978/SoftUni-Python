from collections import deque
bowls_of_ramen = deque(int(n) for n in input().split(", "))
customers = deque(int(n) for n in input().split(", "))

while len(bowls_of_ramen) != 0 and len(customers) != 0:
    bow = bowls_of_ramen.pop()
    customer = customers.popleft()
    if bow == customer:
        continue
    elif bow > customer:
        bow -= customer
        bowls_of_ramen.append(bow)
    else:
        customer -= bow
        customers.appendleft(customer)


if len(customers) == 0:
    print("Great job! You served all the customers.")
    if len(bowls_of_ramen) > 0:
        print(f"Bowls of ramen left: {', '.join([str(b) for b in bowls_of_ramen])}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(c) for c in customers])}")