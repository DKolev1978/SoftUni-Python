import unittest


class IntegerListTests(unittest.TestCase):
    def setUp(self) -> None:
        self.list = IntegerList(1, 5, 10, 1000)

    def test_correct_initialization(self):
        self.assertEqual(4, len(IntegerList.get_data(self.list)))

    def test_get_data_correct(self):
        result = self.list.get_data()
        self.assertEqual([1, 5, 10, 1000], result)

    def test_adding_no_integer_expect_Value_Error(self):
        with self.assertRaises(ValueError) as ve:
            self.list.add(6.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_adding_integer_expect_adding_in_the_list(self):
        self.list.add(10000)
        self.assertEqual([1, 5, 10, 1000, 10000], self.list.get_data())

    def test_get_index_with_invalid_index_raises_IndexError(self):
        with self.assertRaises(IndexError) as ie:
            self.list.get(4)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_index_with_valid_index(self):
        result = self.list.get(3)
        self.assertEqual(1000, result)

    def test_insert_with_invalid_index_expect_IndexError(self):
        with self.assertRaises(IndexError) as ie:
            self.list.insert(4, 100)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_with_valid_index_not_integer_expect_ValueError(self):
        with self.assertRaises(ValueError) as ve:
            self.list.insert(3, 100.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_with_valid_index_valid_integer_expect_element_in_list(self):
        self.list.insert(3, 100000)
        self.assertEqual([1, 5, 10, 100000, 1000], self.list.get_data())

    def test_get_biggest(self):
        self.assertEqual(1000, self.list.get_biggest())

    def test_get_index(self):
        self.assertEqual(0, self.list.get_index(1))
        self.assertEqual(1, self.list.get_index(5))
        self.assertEqual(2, self.list.get_index(10))
        self.assertEqual(3, self.list.get_index(1000))


if __name__ == "__main__":
    unittest.main()


class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)
