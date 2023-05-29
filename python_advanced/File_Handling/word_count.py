import os
import re
from collections import defaultdict


def read_content(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File does not exist, program is ending...")
        exit(0)


root_dir = os.path.dirname(os.path.abspath(__file__))
words_file_name = "words.txt"
words_file_path = os.path.join(root_dir, words_file_name)
input_file_name = "input.txt"
input_file_path = os.path.join(root_dir, input_file_name)

words = read_content(words_file_path).lower().split()
input_content = read_content(input_file_path).lower()
input_content = re.sub(r"[^\w+\s]", '', input_content)
text_content_lines = input_content.split("\n")
words_count = defaultdict(lambda: 0)
for word in words:
    for text_line in text_content_lines:
        if word in text_line:
            words_count[word] += 1

    # words_count[word] = input_content.count(word)

with open("output.txt", "w") as file:
    for key, value in sorted(words_count.items(), key=lambda kvp: kvp[1], reverse=True):
        file.write(f"{key} - {value}\n")