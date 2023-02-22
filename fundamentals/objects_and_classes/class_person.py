class Person:
    def __init__(self, first_name, last_name, age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


person = Person("Dimitar", "Kolev", 44)
print(person.first_name, person.last_name, person.age)
