from unittest import TestCase, main

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.second_nand_car = SecondHandCar("Opel", "Astra", 101, 1000.0)

    def test_correct_initializing(self):
        self.assertEqual("Opel", self.second_nand_car.model)
        self.assertEqual("Astra", self.second_nand_car.car_type)
        self.assertEqual(101, self.second_nand_car.mileage)
        self.assertEqual(1000.0, self.second_nand_car.price)

    def test_price_correctly_setup(self):
        with self.assertRaises(Exception) as ex:
            self.second_nand_car.price = 0.0

        self.assertEqual("Price should be greater than 1.0!", str(ex.exception))

    def test_mileage_correctly_setup(self):
        with self.assertRaises(Exception) as ex:
            self.second_nand_car.mileage = 100

        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ex.exception))

    def test_set_promotional_price_correctly(self):
        new_prise = 500.0
        self.second_nand_car.price = new_prise
        self.assertEqual(500.0, self.second_nand_car.price)


if __name__ == '__main__':
    main()
