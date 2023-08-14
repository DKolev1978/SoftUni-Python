from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar("Opel", "Astra", 1000, 1000)

    def test_correct_initialization(self):
        self.assertEqual("Opel", self.car.model)
        self.assertEqual("Astra", self.car.car_type)
        self.assertEqual(1000, self.car.mileage)
        self.assertEqual(1000, self.car.price)

    def test_list_correct_initialization(self):
        self.car.repairs.append("Need repair")
        self.assertEqual("Need repair", self.car.repairs[0])

    def test_price_setter_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1

        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    def test_price_setter_correct(self):
        self.car.price = 2
        self.assertEqual(2, self.car.price)

    def test_mileage_setter_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_mileage_setter_correctly(self):
        self.car.mileage = 101
        self.assertEqual(101, self.car.mileage)