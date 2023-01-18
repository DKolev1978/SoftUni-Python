text = input()

for i in range(len(text)):
    word = text[i]
    word_as_int = ord(word)
    if 65 <= word_as_int <= 90:
        print(f"{i}, ", end="")





