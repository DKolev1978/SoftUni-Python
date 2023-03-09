# # result = {letter: ord(letter) for letter in input().split(", ")}
# print({letter: ord(letter) for letter in input().split(", ")})

# 6. Odd Occurrence


# words = input().lower().split()
# dictionary = {}
#
# for word in words:
#     if word not in dictionary:
#         dictionary[word] = 0
#     dictionary[word] += 1
#
# for key, value in dictionary.items():
#     if value % 2 != 0:
#         print(key, end=" ")

n = int(input())
synonyms = {}

for i in range(n):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")