from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.second_hand_car = SecondHandCar("Opel", "Astra", 1000, 1000)

    def test_correct_initialization(self):
        self.assertEqual("Opel", self.second_hand_car.model)
        self.assertEqual("Astra", self.second_hand_car.car_type)
        self.assertEqual(1000, self.second_hand_car.mileage)
        self.assertEqual(1000, self.second_hand_car.price)

    def test_self_repairs(self):
        self.second_hand_car.repairs.append("Test")
        self.assertEqual("Test", self.second_hand_car.repairs[0])

    def test_price_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.price = 1

        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    def test_price_setter_works_correctly(self):
        self.second_hand_car.price = 1500
        self.assertEqual(1500, self.second_hand_car.price)

    def test_mileage_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.mileage = 100

        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))

    def test_mileage_setter_works_correctly(self):
        self.second_hand_car.mileage = 1500
        self.assertEqual(1500, self.second_hand_car.mileage)

    def test_set_promotional_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.set_promotional_price(1500)

        self.assertEqual("You are supposed to decrease the price!", str(ve.exception))

    def test_set_promotional_price_works_correctly(self):
        second_hand_car_price = self.second_hand_car.set_promotional_price(900)
        self.assertEqual(second_hand_car_price, 'The promotional price has been successfully set.')

    def test_need_repair_if_price_more_than_half_car_price(self):
        result = self.second_hand_car.need_repair(600, "Engine")
        self.assertEqual("Repair is impossible!", result)

    def test_need_repair_increases_price(self):
        result = self.second_hand_car.need_repair(200, "Engine")
        self.assertEqual(1200, self.second_hand_car.price)
        self.assertEqual('Price has been increased due to repair charges.', result)

    def test_need_repair_appends_repair_description(self):
        self.second_hand_car.need_repair(200, "Engine")
        self.assertEqual("Engine", self.second_hand_car.repairs[-1])

    def test_gt_if_different_self_other(self):
        other_second_hand_car = SecondHandCar("Opel", "Moka", 500, 500)
        result = self.second_hand_car.__gt__(other_second_hand_car)
        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

    def test_gt_if_same_self_other(self):
        other_second_hand_car = SecondHandCar("Opel", "Astra", 500, 500)
        result = self.second_hand_car.__gt__(other_second_hand_car)
        self.assertEqual(True, result)

    def test_correct_str(self):
        self.assertEqual(
            "Model Opel | Type Astra | Milage 1000km\n"
            "Current price: 1000.00 | Number of Repairs: 0"
            , str(self.second_hand_car))


if __name__ == "__main__":
    main()
