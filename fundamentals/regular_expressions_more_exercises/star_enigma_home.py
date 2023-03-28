import re
planet = {}
magic_letters = ["s","t","a","r"]
n = int(input())
planet_name = r"@([A-Za-z]+)"
population_count = r":(\d+)"
attack_type = r""
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
    print(*name)
    print(*population)
    print(new_message)
    print(letter_count)