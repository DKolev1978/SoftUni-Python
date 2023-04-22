import re
n = int(input())
message_regex = r"^([$%])([A-Z][a-z]{2,})\1: \[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$"
for index in range(n):
    new_message = ""
    message = input()
    message_matches = re.findall(message_regex, message)
    if not message_matches:
        print("Valid message not found!")
    else:
        for match in message_matches:
            for m in match:
                if m.isdigit():
                    m = int(m)
                    letter = chr(m)
                    new_message += letter
            print(f"{match[1]}: {new_message}")



