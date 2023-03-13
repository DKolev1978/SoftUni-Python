from string import ascii_lowercase

strings = input().split()
total_result = 0
for sbs in strings:
    first_letter = sbs[0]
    last_letter = sbs[-1]
    number = int(sbs[1:len(sbs) - 1])
    first_letter_alphabet_position = ascii_lowercase.index(first_letter.lower()) + 1
    if first_letter.isupper():
        number /= first_letter_alphabet_position
    else:
        number *= first_letter_alphabet_position

    last_letter_alphabet_position = ascii_lowercase.index(last_letter.lower()) + 1
    if last_letter.isupper():
        number -= last_letter_alphabet_position
    else:
        number += last_letter_alphabet_position
    total_result += number
print(f"{total_result:.2f}")


