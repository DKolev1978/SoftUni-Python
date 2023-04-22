words_def = input().split(" | ")
words_dict = {}

for el in words_def:
    word, definition = el.split(": ")
    if word in words_dict:
        words_dict[word].append(definition)
    else:
        words_dict[word] = [definition]

words_of_teacher = input().split(" | ")
command = input()

if command == "Test":
    for word in words_of_teacher:
        if word in words_dict:
            print(f"{word}:")
            for definition in words_dict[word]:
                print(f" -{definition}")
elif command == "Hand Over":
    print(" ".join(words_dict.keys()))