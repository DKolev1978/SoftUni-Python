from re import findall

class NameTooLong(Exception):
    pass

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
MAX_LENGTH = 10
VALID_DOMAINS = [".com", ".bg", ".org", ".net"]

pattern_name = r'\w+'
pattern_domain = r'\.[a-z]+'

email = input()

while email != "End":
    if email.count("@") > 1:
        raise MoreThanOneAtSymbolError("Email must contain only one @ symbol")
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain at symbol")
    if len(email.split("@")[0]) < MIN_LENGTH:
        raise NameTooShortError("Name must be at least 4 symbols long")
    if len(email.split("@")[0]) > MAX_LENGTH:
        raise NameTooLong("Name must be at most 10 symbols long")
    if findall(pattern_name, email)[0] != email.split("@")[0]:
        raise InvalidNameError("Name can contain only letters, digits and underscores underscores")
    if findall(pattern_domain, email)[-1] not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org,.net")
    print("Email is valid")

    email = input()
