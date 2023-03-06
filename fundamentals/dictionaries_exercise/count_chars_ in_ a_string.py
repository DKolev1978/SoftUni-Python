words = input().split()

count_letters = {}

for word in words:
    for letter in word:
        if letter in count_letters:
            count_letters[letter] += 1
        else:
            count_letters[letter] = 1

for letter, count in count_letters.items():
    print(f"{letter} -> {count}")