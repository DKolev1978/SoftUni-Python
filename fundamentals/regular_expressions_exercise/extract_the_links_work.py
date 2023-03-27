import re

text = input()
regex = r"(www.([A-Za-z0-9]+)(-|.)([A-Za-z0-9]+).[a-z]+.[a-z]+)"
urls = []

while text:
    matches = re.findall(regex, text)
    for match in matches:
        urls.append(match[0])

    text = input()

for url in urls:
    print(url)


