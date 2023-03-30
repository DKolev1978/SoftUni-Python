import re

text = input()
symbols = ['+', '-', '*', '/', '.', 1, 1, 3, 4, 5, 6, 7]
demon_regex = r'([a-zA-z0-9-*/.]+[^, ])'
damage_regex = r'([-+*\/]?[\d+?:\.\d+?]+)'
multiplying = []
deleting = []
demons = {}
demon_names = re.findall(demon_regex, text)


for dm in demon_names:
    damage = 0
    demon_health = 0
    demons[dm] = {}
    demons_damage = re.findall(damage_regex, text)
    for ch in dm:
        if ch.isdigit():
            continue
        elif ch not in symbols:
            demon_health += ord(ch)
        elif ch == "*":
            multiplying.append(ch)
        elif ch == "/":
            deleting.append(ch)
    damage = sum([float(i) for i in demons_damage])
    if len(multiplying) > 0:
        for el in multiplying:
            damage = 2 * damage
    if len(deleting) > 0:
        for el in deleting:
            damage = damage / 2

    demons[dm][demon_health] = damage

for key, index in sorted(demons.items()):
    print(f"{key} -", end="")
    for k, v in index.items():
        print(f" {k} health, {v:.2f} damage")