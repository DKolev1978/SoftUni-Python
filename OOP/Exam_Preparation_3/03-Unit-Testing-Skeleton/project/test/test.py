from unittest import TestCase, main
from project.robot import Robot


class TestRobot(TestCase):
    def setUp(self) -> None:
        self.test_robot = Robot("Test", "Military", 10, 10.0)
        self.test_robot_other = Robot("Test_Other", "Education", 20, 20.0)

    def test_correct_initialization(self):
        self.assertEqual("Test", self.test_robot.robot_id)
        self.assertEqual("Military", self.test_robot.category)
        self.assertEqual(10, self.test_robot.available_capacity)
        self.assertEqual(10.0, self.test_robot.price)
        self.assertEqual(self.test_robot.hardware_upgrades, [])
        self.assertEqual(self.test_robot.software_updates, [])

    def test_list_append_hardware_upgrades(self):
        self.test_robot.hardware_upgrades.append("Arm")
        self.assertEqual("Arm", self.test_robot.hardware_upgrades[-1])

    def test_list_append_software_updates(self):
        self.test_robot.software_updates.append("Android")
        self.assertEqual("Android", self.test_robot.software_updates[-1])

    def test_category_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test_robot.category = "Student"

        self.assertEqual(f"Category should be one of '{self.test_robot.ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_category_setter_works(self):
        self.test_robot.category = "Military"
        self.assertEqual("Military", self.test_robot.category)

    def test_price_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test_robot.price = -1

        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_price_setter_works(self):
        self.test_robot.price = 1
        self.assertEqual(1, self.test_robot.price)

    def test_upgrade_with_existing_part_returns_error(self):
        self.test_robot.hardware_upgrades.append("arm")
        result = self.test_robot.upgrade("arm", 5.0)
        self.assertEqual(result, f"Robot {self.test_robot.robot_id} was not upgraded.")

    def test_upgrade_works_correctly(self):
        result = self.test_robot.upgrade("arm", 5.0)
        self.assertEqual(f"Robot {self.test_robot.robot_id} was upgraded with arm.", result)

    def test_upgrade_price_works_correctly(self):
        self.test_robot.upgrade("arm", 5.0)
        self.test_robot.price += 5.00 * self.test_robot.PRICE_INCREMENT
        self.assertEqual(25.0, self.test_robot.price)

    def test_update_when_version_criteria_not_meet(self):
        self.test_robot.software_updates.append(7)
        self.test_robot.available_capacity = 5
        result = self.test_robot.update(6, 6)
        self.assertEqual(f"Robot {self.test_robot.robot_id} was not updated.", result)

    def test_update_when_criteria_is_meet(self):
        self.test_robot.software_updates.append(5)
        self.test_robot.available_capacity = 5
        result = self.test_robot.update(7, 2)
        self.assertEqual(f"Robot {self.test_robot.robot_id} was updated to version 7.", result)

    def test_update_when_criteria_is_meet_append_software_updates(self):
        self.test_robot.software_updates.append(5)
        self.test_robot.available_capacity = 5
        self.test_robot.update(7, 2)
        self.assertEqual(7, self.test_robot.software_updates[-1])

    def test_update_when_criteria_is_meet_available_capacity(self):
        self.test_robot.software_updates.append(5)
        self.test_robot.available_capacity = 5
        self.test_robot.update(7, 2)
        self.assertEqual(3, self.test_robot.available_capacity)

    def test_gt_self_price_is_bigger_than_other_price(self):
        self.test_robot.price = 25
        result = self.test_robot.__gt__(self.test_robot_other)
        self.assertEqual(f"Robot with ID {self.test_robot.robot_id} is more expensive than Robot with ID {self.test_robot_other.robot_id}.", result)

    def test_gt_self_price_is_eq_to_other_price(self):
        self.test_robot.price = 20
        result = self.test_robot.__gt__(self.test_robot_other)
        self.assertEqual(f"Robot with ID {self.test_robot.robot_id} costs equal to Robot with ID {self.test_robot_other.robot_id}.", result)

    def test_gt_self_price_is_les_then_other_price(self):
        self.test_robot.price = 10
        result = self.test_robot.__gt__(self.test_robot_other)
        self.assertEqual(f"Robot with ID {self.test_robot.robot_id} is cheaper than Robot with ID {self.test_robot_other.robot_id}.", result)


if __name__ == "__main__":
    main()
