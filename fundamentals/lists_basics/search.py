n = int(input())
word = input()

sentences = []
filtered_sentence = []

for i in range(n):
    user_line = input()
    sentences.append(user_line)
    if word in user_line:
        filtered_sentence.append(user_line)

print(sentences)
print(filtered_sentence)
