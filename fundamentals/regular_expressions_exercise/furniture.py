import re

regex = "^>>([A-Za-z]+)<<(\d+(\.?\d*))!(\d+)"
bought_furniture = []
total_prise = 0
while True:
    text = input()
    if text == "Purchase":
        break

    matches = re.findall(regex, text)
    for match in matches:
        furniture = match[0]
        bought_furniture.append(furniture)
        price = match[1]
        quantity = match[3]

        total_prise += float(price) * int(quantity)


print("Bought furniture:")
for fur in bought_furniture:
    print(fur)
print(f"Total money spend: {total_prise:.2f}")

