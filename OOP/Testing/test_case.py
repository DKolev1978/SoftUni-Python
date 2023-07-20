import unittest


from OOP.Testing.sum_numbers import sum_numbers, multiply_numbers, divide_numbers


class SimpleTest(unittest.TestCase):
    def test_sum_numbers(self):
        result = sum_numbers(5, 6)
        expected_result = 11
        self.assertEqual(result, expected_result)

    def test_multiply_numbers(self):
        result = multiply_numbers(5, 6)
        expected_result = 30
        self.assertEqual(result, expected_result)

    def test_divide_numbers(self):
        result = divide_numbers(5, 0)
        expected_result = "You can not divide with 0"
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
