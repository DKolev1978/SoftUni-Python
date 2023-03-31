import re
n = int(input())

barcode = r"\@\#+([A-Z][A-Za-z0-9]{4,}[A-Z])\@\#+"

for _ in range(n):
    text = input()
    matches = re.findall(barcode, text)

    if not matches:
        print("Invalid barcode")
    else:
        text = ''.join(text)
        product_group = ''.join([x for x in text if x.isdigit()])
        if not product_group:
            product_group = "00"
        print(f"Product group: {product_group}")



