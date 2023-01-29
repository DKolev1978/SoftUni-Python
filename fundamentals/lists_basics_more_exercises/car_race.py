race = [int(i) for i in input().split(' ')]
finish = len(race) // 2
left_car = race[0:finish]
right_car = race[-1:finish:-1]

time_left_car = 0
time_right_car = 0

for time in left_car:
    time_left_car += time
    if time == 0:
        time_left_car *= 0.8

for time in right_car:
    time_right_car += time
    if time == 0:
        time_right_car *= 0.8

if time_left_car > time_right_car:
    print(f"The winner is right with total time: {time_right_car:.1f}")
else:
    print(f"The winner is left with total time: {time_left_car:.1f}")