from unittest import TestCase, main
from project.plantation import Plantation


class TestPlantation(TestCase):
    def setUp(self) -> None:
        self.test_plantation = Plantation(10)

    def test_correct_initialization(self):
        self.test_plantation = Plantation(20)
        self.assertEqual(20, self.test_plantation.size)
        self.assertEqual(self.test_plantation.plants, {})
        self.assertEqual(self.test_plantation.workers, [])

    def test_size_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test_plantation = Plantation(-1)
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_size_setter_works_as_expected(self):
        self.test_plantation = Plantation(1)
        self.assertEqual(1, self.test_plantation.size)

    def test_hire_worker_if_name_exist(self):
        self.test_plantation.workers.append("Test")
        with self.assertRaises(ValueError) as ve:
            self.test_plantation.hire_worker("Test")
        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_works_as_expected(self):
        self.test_plantation.hire_worker("Test")
        self.assertEqual("Test", self.test_plantation.workers[-1])

    def test_hire_worker_works_as_expected_returns_correct_message(self):
        self.assertEqual("Test successfully hired.", self.test_plantation.hire_worker("Test"))

    def test_len_works_as_expected(self):
        count_of_plants = 0
        self.assertEqual(count_of_plants, len(self.test_plantation.plants.items()))

    def test_planting_with_not_hired_worker_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test_plantation.planting("Test1", "Bannana")

        self.assertEqual("Worker with name Test1 is not hired!", str(ve.exception))

    def test_planting_withe_len_raise_value_error(self):
        self.test_plantation.size = 0
        self.test_plantation.workers.append("Test1")
        with self.assertRaises(ValueError) as ve:
            self.test_plantation.planting("Test1", "Bannana")
        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_with_worker_in_workers(self):
        self.test_plantation.hire_worker("Test1")
        self.test_plantation.plants["Test1"] = ["Kiwi"]
        result = self.test_plantation.planting("Test1", "Bannana")
        self.assertEqual("Test1 planted Bannana.", result)

    def test_planting_with_worker_in_workers_first_plant(self):
        self.test_plantation.hire_worker("Test1")
        result = self.test_plantation.planting("Test1", "Bannana")
        self.assertEqual("Test1 planted it's first Bannana.", result)

    def test_correct_str(self):
        self.test_plantation.hire_worker("Test1")
        self.test_plantation.planting("Test1", "Bannana")
        self.assertEqual(
            "Plantation size: 10\n"
            "Test1\n"
            "Test1 planted: Bannana", str(self.test_plantation)
        )

    def test_correct_repr(self):
        self.test_plantation.hire_worker("Test1")
        self.test_plantation.hire_worker("Test2")

        self.test_plantation.planting("Test1", "Bannana")
        self.test_plantation.planting("Test2", "Bannana")
        self.assertEqual(
            "Size: 10\n"
            "Workers: Test1, Test2", self.test_plantation.__repr__()
        )


if __name__ == "__main__0":
    main()