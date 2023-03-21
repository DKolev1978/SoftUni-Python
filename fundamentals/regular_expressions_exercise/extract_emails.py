import re

text = input()

regex = "\\s([A-Za-z0-9][\w\-.]*[A-Za-z0-9]@[A-Za-z][A-Za-z\-]*[A-Za-z](\.[A-Za-z][A-Za-z\-]*[A-Za-z])+)"
match = re.findall(regex, text)

print("\n".join([groups[0] for groups in match]))
