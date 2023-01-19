text = input()
list_a = []
for i in range(len(text)):
    letter = text[i]
    letter_as_int = ord(letter)
    if 65 <= letter_as_int <= 90:
        list_a.append(int(i))
print(list_a)





