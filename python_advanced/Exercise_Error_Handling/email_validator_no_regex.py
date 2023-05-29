import string  # Used to obtain valid symbols in name


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolErrorException(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


# Global
MIN_LENGTH = 4
VALID_DOMAINS = ["com", "bg", "net", "org"]
ALLOWED = string.ascii_letters + string.digits + '_' + '.'  # Name can contain only letters, numbers, dots and underscores


# email input
email = input()

while email != "End":

    if email.count("@") > 1:
        raise MoreThanOneAtSymbolError("Email should contain only one @ symbol!")
    if len(email.split("@")[0]) < MIN_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")
    if "@" not in email:
        raise MoreThanOneAtSymbolError("Email must contain @!")
    emails = email.split("@")
    name = emails[0]
    for letter in name:
        if letter not in ALLOWED:
            raise InvalidNameError("Name can contain only letters, digits, dots and underscores!")
    domain = emails[1].split(".")
    if domain[1] not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    email = input()
