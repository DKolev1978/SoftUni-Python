first_str = ord(input())
second_str = ord(input())

random_str = input()

sum_str = 0
for letter in random_str:
    current = ord(letter)
    if first_str < current < second_str:
        sum_str += current

print(sum_str)