days_plundering = int(input())
daily_plundering = int(input())
expected_plunder = float(input())

total_plunder = 0

for day in range(1, days_plundering + 1):
    total_plunder += daily_plundering
    if day % 3 == 0:
        total_plunder += daily_plundering * 0.50
    if day % 5 == 0:
        total_plunder = total_plunder - total_plunder * 0.30

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {(total_plunder / expected_plunder) * 100:.2f}% of the plunder.")

