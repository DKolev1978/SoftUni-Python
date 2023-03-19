import re

pattern = "(\+359-2-[0-9]{3}-[0-9]{4}|\+359 2 [0-9]{3} [0-9]{4})\\b"
phone_numbers = input()
matches = re.findall(pattern, phone_numbers)
print(", ".join(matches))
