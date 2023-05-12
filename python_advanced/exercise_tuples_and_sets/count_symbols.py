# occurrences = {}
#
# for letter in input():
#     occurrences[letter] = occurrences.get(letter, 0) + 1
#
#     # if letter not in occurrences:
#     #     occurrences[letter] = 0
#     #
#     # occurrences[letter] += 1
#
# for letter, times in sorted(occurrences.items()):
#     print(f"{letter}: {times} time/s")

# Second

text = input()

for letter in sorted(set(text)):
    print(f"{letter}: {text.count(letter)} time/s")
