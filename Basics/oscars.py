actor = input()
academy_points = float(input())
count_jury = int(input())
total_points = academy_points

for i in range(1, count_jury + 1):
    name = input()
    points = float(input())

    current_points = (len(name) * points) / 2
    total_points = total_points + current_points

    if total_points >= 1250.5:
        break

if total_points >= 1250.5:
    print(f"Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {actor} you need {1250.5 - total_points:.1f} more!")