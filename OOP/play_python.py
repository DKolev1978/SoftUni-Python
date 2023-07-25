from typing import List
from unittest import TestCase, main


# class Phone:
#     def __init__(self, color, size):
#         self.color = color
#         self.size = size
#
#     def turn_on(self):
#         return 'The phone is turned on'
#
#
# phone = Phone("red", 10)
# print(phone.turn_on())

# class Book:
#     def __init__(self, name: str, author: str, pages: int) -> None:
#         self.name = name
#         self.author = author
#         self.pages = pages
#
#
# book = Book("My Book", "Me", 200)
# print(book.name)
# print(book.author)
# print(book.pages)

# class Car:
#     def __init__(self, name: str, model: str, engine: str) -> None:
#         self.name = name
#         self.model = model
#         self.engine = engine
#
#     def get_info(self):
#         return f'This is {self.name} {self.model} with engine {self.engine}'
#
#
# car = Car("Kia", "Rio", "1.3L B3 I4")
# print(car.get_info())

# First_Steps_in_OOP_Exercise-Shop

# class Shop:
#     def __init__(self, name: str, items: List[str]) -> None:
#         self.name = name
#         self.items = items
#
#     def get_items_count(self):
#         return len(self.items)
#
#
# class TestShop(TestCase):
#     def setUp(self) -> None:
#         self.shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
#
#     def test_initialization(self):
#         self.assertEqual("My Shop", self.shop.name)
#         self.assertEqual(["Apples", "Bananas", "Cucumbers"], self.shop.items)
#
#     def test_get_items_count_correctly(self):
#         self.assertEqual(3, len(self.shop.items))
#
#
# if __name__ == "__main__":
#     main()

# shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
# print(shop.get_items_count())

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_info(self):
#         return f'{self.name} is {self.age} years old.'
#
#
# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id
#
#     def get_id(self):
#         return self.student_id
#
#
# person = Person("John", 25)
# print(person.get_info())
#
# student = Student("Leo", 20, 10035464)
# print(student.get_info())
# print(student.get_id())

class Father:
    def __init__(self):
        self.father_name = 'Taylor Evans'

    def father_name(self):
        return self.father_name


class Mother:
    def __init__(self):
        self.mother_name = 'Bet Williams'


class Daughter(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)

    def get_parent_info(self):
        return f'Father: {self.father_name}, Mother: {self.mother_name}'


child = Daughter()
print(child.get_parent_info())
