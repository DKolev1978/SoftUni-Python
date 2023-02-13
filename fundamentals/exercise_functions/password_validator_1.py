def validate(password):
    errors = []
    if not is_valid_lenght(password):
        errors.append("Password must be between 6 and 10 characters")

    if not contain_alpha_num(password):
        errors.append("Password must consist only of letters and digits")

    if not contains_at_least_two_digits(password):
        errors.append("Password must have at least 2 digits")

    return errors


def is_valid_lenght(password):
    return 6 <= len(password) <= 10


def contain_alpha_num(password):
    return password.isalnum()


def contains_at_least_two_digits(password):
    digits_counter = 0
    for ch in password:
        if ch.isdigit():
            digits_counter += 1

    return digits_counter >= 2


input_password = input()
errors = validate(input_password)

if len(errors):
    for error in errors:
        print(error)
else:
    print("Password is valid")
