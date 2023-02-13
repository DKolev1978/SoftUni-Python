first = input()
second = input()

for char in range(ord(first) + 1, ord(second)):
    chars = chr(char)
    print(chars, end=" ")