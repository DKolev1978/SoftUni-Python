def found_palindroms(text, list_of_palindroms):
    if word == "".join(reversed(word)):
        palindromes.append(word)
    return [palindromes]


# some Input

strings = input().split(" ")
searched_palindrome = input()
palindromes = []

for word in strings:
    found_palindroms(word, palindromes)

print(f"{palindromes}")
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")
