text = input()
encrypted_text = ""
for char in text:
    new_ascii_value = ord(char) + 3
    encrypted_text += chr(new_ascii_value)

print(encrypted_text)