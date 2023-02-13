def removing_the_vowels(text):
    vowels = ['a', 'o', 'u', 'e', 'i']
    return [ch for ch in text if ch.lower() not in vowels]


text = input()
text_to_print = removing_the_vowels(text)
print("".join(text_to_print))
