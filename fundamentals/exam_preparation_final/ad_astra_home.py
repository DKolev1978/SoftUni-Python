import math
import re

products_pattern = r"(#|\|)(?P<product>[a-zA-Z\s]+)\1(?P<date>\d{2}\/\d{2}\/\d{2})\1(?P<calories>\d{1,5})\1"
text = input()

days = sum(int(x.group('calories')) for x in re.finditer(products_pattern, text)) / 2000
print(f"You have food to last you for: {math.floor(days)} days!")
for match in re.finditer(products_pattern, text):
    print(f"Item: {match.group('product')}, Best before: {match.group('date')}, Nutrition: {match.group('calories')}")

