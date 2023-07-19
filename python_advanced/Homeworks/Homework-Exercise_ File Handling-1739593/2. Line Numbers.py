from string import punctuation

with open("./text_line_numbers.txt", "r") as file:
    text = file.readlines()

output_file = open("./output_line_numbers.txt", "w")

for i in range(len(text)):
    letters, marks = 0, 0

    for symbol in text[i]:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output_file.write(f"Line {i+1}: {''.join(text[i][:-1])} ({letters})({marks})\n")

output_file.close()