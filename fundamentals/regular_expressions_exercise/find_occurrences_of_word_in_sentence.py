import re

text = input().lower()
word = input().lower()

matches = re.findall(fr"\b{word}\b", text)
print(len(matches))
