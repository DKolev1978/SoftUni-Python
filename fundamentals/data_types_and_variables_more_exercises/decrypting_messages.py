key: int = int(input())
number_of_lines = int(input())

for _ in range(number_of_lines):
    char = input()
    char_new = ord(char) + key
    print(chr(char_new), end="")

