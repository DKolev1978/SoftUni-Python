first_letter = input()
last_letter = input()
dummy_letter = input()

valid_combinations = 0
first_letter_ascii = ord(first_letter)
last_letter_ascii = ord(last_letter)
dummy_letter_ascii = ord(dummy_letter)
for i in range(first_letter_ascii, last_letter_ascii + 1):
    for j in range(first_letter_ascii, last_letter_ascii + 1):
        for k in range(first_letter_ascii, last_letter_ascii + 1):
            if i != dummy_letter_ascii and j != dummy_letter_ascii and k != dummy_letter_ascii:
                print(f"{chr(i)}{chr(j)}{chr(k)}", end=" ")
                valid_combinations += 1
print(valid_combinations)