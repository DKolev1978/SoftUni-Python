from collections import deque

bowls_of_ramen = deque([int(bor) for bor in input().split(", ")])
customers = deque([int(cus) for cus in input().split(", ")])


while bowls_of_ramen and customers:
    current_bowl = bowls_of_ramen.pop()
    current_customer = customers.popleft()

    if current_bowl == current_customer:
        continue

    if current_bowl > current_customer:
        current_bowl -= current_customer
        bowls_of_ramen.append(current_bowl)
        continue

    if current_bowl < current_customer:
        current_customer -= current_bowl
        customers.appendleft(current_customer)
        continue


if not customers and bowls_of_ramen:
    print("Great job! You served all the customers.")
    print(f"Bowls of ramen left: {', '.join([str(bow) for bow in bowls_of_ramen])}")

if not customers and not bowls_of_ramen:
    print("Great job! You served all the customers.")

if not bowls_of_ramen and customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(cus) for cus in customers])}")

