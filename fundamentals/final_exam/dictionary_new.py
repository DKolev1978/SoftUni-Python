word_definition = input().split(" | ")
word_dict = {}

for w in word_definition:
    key, value = w.split(": ")
    if key in word_dict:
        word_dict[key].append(value)
    else:
        word_dict[key] = [value]
        
words = input().split(" | ")
word = input()
if word == "Test":
    for w in words:
        if w in word_dict:
            print(f"{w}:")
            for value in word_dict[w]:
                print(f" -{value}")

elif word == "Hand Over":
    print(" ".join(word_dict.keys()))



