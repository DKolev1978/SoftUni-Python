string_input = input().split()
first_word = string_input[0]
second_word = string_input[1]

min_len = min(len(first_word), len(second_word))
result = 0
for index in range(min_len):
    first_word_char = first_word[index]
    second_word_char = second_word[index]
    result += ord(first_word_char) * ord(second_word_char)

result += sum([ord(char) for char in first_word[min_len:]])
result += sum([ord(char) for char in second_word[min_len:]])
# for idx in range(min_len, len(first_word)):
#     result += ord(first_word[idx])
# for idx in range(min_len, len(second_word)):
#     result += ord(second_word[idx])

print(result)
