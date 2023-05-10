from collections import deque


food = int(input())
orders = deque(int(x) for x in input().split())

print(max(orders))

while orders:
    if food >= orders[0]:
        food -= orders[0]
        orders.popleft()
    else:
        print(f"Orders left: {' '.join([str(x) for x in orders])}")
        break
else:
    print("Orders complete")
