# def even_odd(*args):
#     numbers = []
#     even = []
#     odd = []
#     com = ''
#     for arg in args:
#         if not isinstance(arg, int):
#             com = arg
#         else:
#             numbers.append(arg)
#
#     if com == "even":
#         for num in numbers:
#             if num % 2 == 0:
#                 even.append(num)
#         return even
#
#     elif com == "odd":
#         for num in numbers:
#             if num % 2 != 0:
#                 odd.append(num)
#         return odd


def even_odd(*args):
    command = args[-1]

    if command == "even":
        return [arg for arg in args[:-1] if int(arg) % 2 == 0]
    else:
        return [arg for arg in args[:-1] if int(arg) % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
