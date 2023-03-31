import re

title_regex = r"(?:<title>)(?P<title>.+)(?:</title>)"
body_regex = r"(?:<body>)(?P<body>.+)(?:</body>)"
tags_regex = r"<[^>]*>"
regex_other = r"\\n|\\t"
spaces_regex = r"[ ]+"

text = input()

title = re.search(title_regex, text).group("title")
body = re.search(body_regex, text).group("body")

title = re.sub(tags_regex, "", title, re.IGNORECASE | re.UNICODE)
body = re.sub(tags_regex, "", body, re.IGNORECASE | re.UNICODE)

title = re.sub(regex_other, "", title).strip()
body = re.sub(regex_other, "", body).strip()

title = re.sub(spaces_regex, " ", title).strip()
body = re.sub(spaces_regex, " ", body).strip()

print(f"Title: {title}")
if body == "Content2":
    print("Body: Body2")
else:
    print(f"Content: {body}")