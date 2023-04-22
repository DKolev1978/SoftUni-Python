word_definition = input().split(" | ")
word_definition_dict = {}
for el in word_definition:
    element = el.split(": ")
    key = element[1]
    value = element[0]
    word_definition_dict[key] = value

words = input().split(" | ")
word = input()
if word == "Test":
    for word in words:
        if word in word_definition_dict.values():
            print(f"{word}:")
            for key, value in word_definition_dict.items():
                if value == word:
                    print(f" -{key}")

elif word == "Hand Over":
    for key in word_definition_dict.values():
        print(key, end=" ")


