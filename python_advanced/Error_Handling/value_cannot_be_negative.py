# class CustomError(Exception):
#     pass
#
#
# raise CustomError("here is my message")

# define Python user-defined exceptions
# class Error(Exception):
#     """Base class for other exceptions"""
#     pass
#
#
# class ValueTooSmallError(Error):
#     """Raised when the input value is too small"""
#
#
# num = int(input())
# if num < 10:
# #     raise ValueTooSmallError
# class ValueCanNotBeNegative(Exception):
#     pass
#
#
# for _ in range(5):
#     try:
#         num = float(input("Enter a valid number: "))
#         if num < 0:
#             raise ValueCanNotBeNegative
#     except ValueError:
#         print("This is not a valid number. Continue to nex one")

# class ValueCannotBeNegative(Exception):
#     """Number is below zero"""
#     pass
#
#
# for i in range(5):
#     number = int(input())
#     if number < 0:
#         raise ValueCannotBeNegative

my_tuple = (1, 2, 3)
print(type(my_tuple))
print(my_tuple[-1])
print(len(my_tuple))

my_set = {1, 2, 3}
my_set.add(4)
print(my_set)
print(type(my_set))

my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)
