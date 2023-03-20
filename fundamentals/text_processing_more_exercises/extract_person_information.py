n = int(input())

for _ in range(n):
    text = input()
    first_letter = text.find("@") + 1
    second_letter = text.find("|", first_letter)
    name = text[first_letter:second_letter]
    age1 = text.find("#") + 1
    age2 = text.find("*", age1)
    age = text[age1:age2]
    print(f"{name} is {age} years old.")

