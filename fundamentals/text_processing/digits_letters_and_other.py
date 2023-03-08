text = input()

letters = ""
digits = ""
symbols = ""

for ch in text:
    if ch.isalpha():
        letters += ch
    elif ch.isdigit():
        digits += ch
    else:
        symbols += ch

print(digits)
print(letters)
print(symbols)