import math

width_spaceship = float(input())
length_spaceship = float(input())
height_spaceship = float(input())
height_astronafts = float(input())

astronaft_room = 2 * 2 * (height_astronafts + 0.40)
total_spaceship_space = width_spaceship * length_spaceship * height_spaceship

total_people = math.floor(total_spaceship_space / astronaft_room)
if total_people < 3:
    print("The spacecraft is too small.")
elif total_people > 10:
    print("The spacecraft is too big.")
else:
    print(f"The spacecraft holds {total_people:.0f} astronauts." )
