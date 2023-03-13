text = input()
parts = text.split(":")

for line in parts[1:]:
    symbol = line[0]
    print(f":{symbol}")