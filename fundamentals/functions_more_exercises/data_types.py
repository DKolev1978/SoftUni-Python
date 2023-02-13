def calculate(what, second_what):
    if what == "int":
        number = int(second_what)
        number = number * 2
    elif what == "real":
        number = float(second_what)
        number = f"{number * 1.5:.2f}"
    elif what == "string":
        number = '$' + second_what + '$'

    return number


word = input()
action = input()
print(calculate(word, action))