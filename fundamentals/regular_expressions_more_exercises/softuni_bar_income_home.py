import re

text = input()
names_regex = r"%([A-Z][a-z]+)%"
products_regex = r"<(\w+)>"
count_regex = r"\|(\d+)\|"
prices_regex = r"((?:\d+(?:\.\d*)?|\.\d+))\$"
total_income = 0

while text != "end of shift":
    name = re.findall(names_regex, text)
    product = re.findall(products_regex, text)
    count = re.findall(count_regex, text)
    price = re.findall(prices_regex, text)
    if name and product and count and price:
        product_price = float(price[0])
        price = int(count[0]) * product_price
        total_income += price
        print(f"{name[0]}: {product[0]} - {price:.2f}")
    text = input()
print(f"Total income: {total_income:.2f}")