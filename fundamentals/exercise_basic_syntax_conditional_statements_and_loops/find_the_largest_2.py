num = input()

number = int("".join(sorted(str(num), reverse=True)))

print(number)