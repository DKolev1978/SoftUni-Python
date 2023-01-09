steps_needed = 10000
actual_steps = int(input())
steps = actual_steps

while steps <= steps_needed:
    actual_steps = input()
    if actual_steps == "Going home":
        actual_steps = int(input())
        steps = steps + actual_steps
        break

    actual_steps = int(actual_steps)
    steps = steps + actual_steps

diff = abs(steps_needed - steps)
if steps >= steps_needed:
    print("Goal reached! Good job!")
    print(f'{diff} steps over the goal!')
else:
    print(f"{diff} more steps to reach goal.")






