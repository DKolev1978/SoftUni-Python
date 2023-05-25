# def kwargs_length(**kwargs):
#     return len(kwargs)
#
#
# dictionary = {'name': 'Peter', 'age': 25, 'City': 'Sofia'}
# print(kwargs_length(**dictionary))


def kwargs_length(**kwargs):
    return len(kwargs)


dictionary = {'name': 'Peter', 'age': 25}
print(kwargs_length(**dictionary))