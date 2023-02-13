first_letter = input()
second_letter = input()

first_char_ascii = ord(first_letter)
second_char_ascii = ord(second_letter)
letters = []
for i in range(first_char_ascii + 1, second_char_ascii):
    letters.append(chr(i))
print(" ".join(letters), end="")

