import math

tournaments_count = int(input())
initial_points = int(input())
total_points = initial_points
win_tournaments = 0

for i in range(1, tournaments_count + 1):
    etap = input()

    if etap == 'W':
        win_tournaments += 1
        total_points += 2000
    elif etap == 'F':
        total_points += 1200
    elif etap == 'SF':
        total_points += 720

print(f"Final points: {total_points:.0f}")
avg_points = (total_points - initial_points) / tournaments_count
print(f"Average points: {math.floor(avg_points)}")
print(f"{win_tournaments / tournaments_count * 100:.2f}%")