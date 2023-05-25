# def sum_of_two_numbers(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# sum_of_two_numbers(5, 6, 7, one=1, three=3)
#
#
# def even_odd(*args):
#     command = args[-1]
#
#     if command == "even":
#         return [arg for arg in args[:-1] if int(arg) % 2 == 0]
#     else:
#         return [arg for arg in args[:-1] if int(arg) % 2 != 0]
#
#
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
#

def even_odd_filter(**numbers):
    if "odd" in numbers:
        numbers["odd"] = [n for n in numbers["odd"] if n % 2 != 0]

    if "even" in numbers:
        numbers["even"] = [n for n in numbers["even"] if n % 2 == 0]

    return dict(sorted(numbers.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2]
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))

