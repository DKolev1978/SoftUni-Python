def multiply(times):
    def decorator(function):
        def wrapper(*args, **kwargs):
            return times * function(*args, **kwargs)

        return wrapper

    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))

# test zero second
import unittest


class MultiplyTests(unittest.TestCase):
    def test_zero_second(self):
        @multiply(5)
        def add_ten(number):
            return number + 10

        self.assertEqual(add_ten(6), 80)


if __name__ == "__main__":
    unittest.main()
