from string import punctuation

with open("files/text.txt") as line_numbers_file:
    text = line_numbers_file.readlines()

output_file = open("files/output.txt", "w")
for i in range(len(text)):
    letters, marks = 0, 0

    for symbol in text[i]:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1
    output_file.write(f"Line {i+1}: {''.join(text[i][:-1])} ({letters})({marks})\n")

output_file.close()
