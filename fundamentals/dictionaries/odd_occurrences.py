word_keys = [el.lower() for el in input().split()]
default = 0
occurrences = dict.fromkeys(word_keys, default)

for word in word_keys:
    # occurrences[word] = word_keys.count(word)
    occurrences[word] += 1

for word, count in occurrences.items():
    if count % 2 != 0:
        print(word, end=" ")


