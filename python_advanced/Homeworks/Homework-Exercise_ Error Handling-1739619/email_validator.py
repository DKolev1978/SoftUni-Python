from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


MIN_LENGTH = 4
VALID_DOMAINS = [".com", ".bg", ".net", ".org"]

pattern_name = r'\w+'
pattern_domain = r'\.[a-z]+'

email = input()

while email != "End":

    if email.count("@") > 1:
        raise MoreThanOneAtSymbolError("Email should not have more than one @ symbol!")
    if len(email.split("@")[0]) < MIN_LENGTH:
        raise NameTooShortError("Name should contain more than 4 characters!")
    if "@" not in email:
        raise MustContainAtSymbolError("Email should contain one @ symbol!")
    if findall(pattern_name, email)[0] != email.split("@")[0]:
        raise InvalidNameError("Invalid name! Name should contain only letters, digits and underscores!")
    if findall(pattern_domain, email)[-1] not in VALID_DOMAINS:
        raise InvalidDomainError("Invalid domain! Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    email = input()
