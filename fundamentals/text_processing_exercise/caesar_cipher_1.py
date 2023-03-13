text = input()
encrypted_test = ''.join([chr(ord(ch) + 3) for ch in text])
print(encrypted_test)