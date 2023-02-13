text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
new_text = [ch for ch in text if ch.lower() not in vowels]
print("".join(new_text))


