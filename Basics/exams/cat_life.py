import math

bread = input()
sex = input()

if bread == 'British Shorthair':
    if sex == 'm':
        months = int(math.floor(13 * 12) / 6)
        print(f"{months} cat months")
    elif sex == 'f':
        months = int(math.floor(14 * 12) / 6)
        print(f"{months} cat months")
elif bread == "Persian":
    if sex == 'm':
        months = int(math.floor(14 * 12) / 6)
        print(f"{months} cat months")
    elif sex == 'f':
        months = int(math.floor(15 * 12) / 6)
        print(f"{months} cat months")
elif bread == "Siamese":
    if sex == 'm':
        months = int(math.floor(15 * 12) / 6)
        print(f"{months} cat months")
    elif sex == 'f':
        months = int(math.floor(16 * 12) / 6)
        print(f"{months} cat months")
elif bread == "Ragdoll":
    if sex == 'm':
        months = int(math.floor(16 * 12) / 6)
        print(f"{months} cat months")
    elif sex == 'f':
        months = int(math.floor(17 * 12) / 6)
        print(f"{months} cat months")
elif bread == "American Shorthair":
    if sex == 'm':
        months = int(math.floor(12 * 12) / 6)
        print(f"{months} cat months")
    elif sex == 'f':
        months = int(math.floor(13 * 12) / 6)
        print(f"{months} cat months")
elif bread == "Siberian":
    if sex == 'm':
        months = int(math.floor(11 * 12) / 6)
        print(f"{months} cat months")
    elif sex == 'f':
        months = int(math.floor(12 * 12) / 6)
        print(f"{months} cat months")
else:
    print(f'{bread} is invalid cat!')

