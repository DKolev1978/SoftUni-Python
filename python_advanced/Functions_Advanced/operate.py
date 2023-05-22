# # functions = {
# #     "*": lambda i: reduce(lambda a, b: a * b, map(int, expression[:i])),
# #     "/": lambda i: reduce(lambda a, b: a / b, map(int, expression[:i])),
# #     "+": lambda i: reduce(lambda a, b: a + b, map(int, expression[:i])),
# #     "-": lambda i: reduce(lambda a, b: a - b, map(int, expression[:i])),
# # }
# # def is_valid(*args):
# #     for idx in args:
# #         print(idx)
#
#
# def division (*args):
#     idx = 0
#     for num in args:
#         if idx == 0:
#             result = num
#             idx += 1
#         else:
#             result /= num
#             return result
#
#
# def operate(operator, *args):
#     result = 0
#     if operator == "*" or operator == "/":
#         result = 1
#         if operator == "*":
#             for num in args:
#                 result *= num
#         elif operator == "/":
#             division(*args)
#     elif operator == "+":
#         result = sum(args)
#     elif operator == "-":
#         for num in args:
#             result -= num
#
#     return result
#
#
# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4, 2))
# print(operate("/", 8, 4))
# print(operate("-", 8, 4))
#

from functools import reduce


def operate(operator, *args):

    return reduce(lambda a, b: eval(f"{a}{operator}{b}"), args)
    # if operator == "+":
    #     return reduce(lambda a, b: a + b, args)
    # elif operator == "*":
    #     return reduce(lambda a, b: a * b, args)
    # elif operator == "-":
    #     return reduce(lambda a, b: a - b, args)
    # else:
    #     return reduce(lambda a, b: a // b, args)


print(operate("+", 1, 2))
print(operate("*", 3, 4))
print(operate("-", 6, 4))
print(operate("/", 8, 4))
