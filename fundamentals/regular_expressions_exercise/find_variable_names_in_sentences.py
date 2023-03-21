import re
regex = "\\b_([A-Za-z\d]+)\\b"
text = input()
matches = re.findall(regex, text)
print(','.join(matches))
