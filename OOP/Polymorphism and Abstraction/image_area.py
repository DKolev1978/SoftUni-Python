class ImageArea:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()


a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 == a2)
print(a1 != a3)

import unittest


class TestsImageArea(unittest.TestCase):
    def setUp(self):
        self.a1 = ImageArea(6, 4)
        self.a2 = ImageArea(2, 12)
        self.a3 = ImageArea(3, 18)

    def test_init(self):
        self.assertEqual(self.a1.width, 6)
        self.assertEqual(self.a1.height, 4)

    def test_get_area(self):
        self.assertEqual(self.a2.get_area(), 24)

    def test_equal_true_and_false(self):
        self.assertTrue(self.a1 == self.a2)
        self.assertFalse(self.a2 == self.a3)

    def test_not_equal_true_and_false(self):
        self.assertFalse(self.a1 != self.a2)
        self.assertTrue(self.a2 != self.a3)

    def test_lt_true_and_false(self):
        self.assertTrue(self.a2 < self.a3)
        self.assertFalse(self.a3 < self.a2)

    def test_le_true_and_false(self):
        self.assertTrue(self.a2 <= self.a1)
        self.assertFalse(self.a3 <= self.a2)

    def test_gt_true_and_false(self):
        self.assertTrue(self.a3 > self.a2)
        self.assertFalse(self.a1 > self.a3)

    def test_ge_true_and_false(self):
        self.assertTrue(self.a1 >= self.a2)
        self.assertFalse(self.a1 >= self.a3)


if __name__ == "__main__":
    unittest.main()
