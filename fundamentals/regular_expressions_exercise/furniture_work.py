import re

total_cost = 0
furniture = []

regex = r">>([A-Za-z]+)<<(\d+(\.?\d*))!(\d+)"
while True:
    text = input()
    if text == "Purchase":
        break

    matches = re.findall(regex, text)
    for match in matches:
        furniture_type = match[0]
        furniture.append(furniture_type)
        furniture_price = match[1]
        furniture_count = match[3]
        total_cost += float(furniture_price) * int(furniture_count)

print("Bought furniture:")
for fur in furniture:
    print(fur)
print(f"Total money spend: {total_cost:.2f}")

