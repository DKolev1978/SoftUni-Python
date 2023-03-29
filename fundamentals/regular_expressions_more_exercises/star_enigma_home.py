import re
attacked_planets = []
destroyed_plannet = []
magic_letters = ["s","t","a","r"]
n = int(input())
planet_name = r".*@(?P<planet>[A-Z][a-z]+)[^\@\-\!\:\>]*:)"
population_count = r"(\d+)[^\@\-\!\:\>]*\!])"
attack_type = r"(A|D)\![^\@\-\!\:\>]*\->]"
soldier_count = r"(\d+).*"
for i in range(n):
    letter_count = 0
    text = input()
    new_message = ""
    for letter in text:
        if letter.lower() in magic_letters:
            letter_count += 1
    for letter in text:
        new_letter = ord(letter) - letter_count
        new_message += chr(new_letter)
    name = re.findall(planet_name, new_message)
    population = re.findall(population_count, new_message)
    attack = re.findall(attack_type, new_message)
    soldier = re.findall(soldier_count, new_message)
    if not len(name) or not len(population) or not len(attack) or not len(soldier):
        continue
    else:
        if attack[0] == "A":
            attacked_planets.append(name[0])
        elif attack[0] == "D":
            destroyed_plannet.append(name[0])

print(f"Attacked planets: {len(attacked_planets)}")
for planet in sorted(attacked_planets):
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_plannet)}")
for planet in sorted(destroyed_plannet):
    print(f"-> {planet}")


