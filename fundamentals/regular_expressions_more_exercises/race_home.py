import re
text = input().split(", ")
regex = r"([A-Za-z]|[0-9])"
names = {name: 0 for name in text}   # Creates dictionary whit key = Name, value = 0.
                                        # Value will be updated afterwords
commands = input()

while commands != "end of race":
    matches = re.findall(regex, commands)
    match_score = 0
    match_name = ""
    for match in matches:
        if match.isdigit():
            match_score += int(match)
        else:
            match_name += match
    if match_name in names.keys():
        names[match_name] += match_score

    commands = input()

names = dict(sorted(names.items(), key=lambda x: x[1], reverse=True))
key_to_delete = max(names, key=lambda k: names[k])
print(f"1st place: {key_to_delete}")
del names[key_to_delete]
key_to_delete = max(names, key=lambda k: names[k])
print(f"2nd place: {key_to_delete}")
del names[key_to_delete]
key_to_delete = max(names, key=lambda k: names[k])
print(f"3rd place: {key_to_delete}")