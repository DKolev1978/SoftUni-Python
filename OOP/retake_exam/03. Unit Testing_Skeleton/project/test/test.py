from unittest import TestCase, main
from project.trip import Trip


class TestTrip(TestCase):
    def setUp(self) -> None:
        self.trip = Trip(1000.00, 2, True)

    def test_trip_init(self):
        self.assertEqual(1000.00, self.trip.budget)
        self.assertEqual(2, self.trip.travelers)
        self.assertEqual(True, self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_travelers_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0
        self.assertEqual(str(ve.exception), "At least one traveler is required!")

    def test_travelers_setter_works(self):
        self.trip.travelers = 3
        self.assertEqual(self.trip.travelers, 3)

    def test_is_family_setter_count_les_than_two(self):
        self.trip.travelers = 1
        self.trip.is_family = True
        self.assertEqual(False, self.trip.is_family)

    def test_is_family_setter_count_more_than_two_not_family(self):
        self.trip.travelers = 3
        self.trip.is_family = False
        self.assertEqual(False, self.trip.is_family)

    def test_is_family_setter_works(self):
        self.trip.travelers = 3
        self.trip.is_family = True
        self.assertEqual(True, self.trip.is_family)

    def test_book_a_trip_destination_not_in_destinations(self):
        result = self.trip.book_a_trip('Romania')
        self.assertEqual(result, "This destination is not in our offers, please choose a new one!")

    def test_book_a_trip_not_enough_money(self):
        destination = self.trip.book_a_trip('Australia')
        with self.assertRaises(KeyError) as ke:
            required_price = self.trip.DESTINATION_PRICES_PER_PERSON[destination] * self.trip.travelers
            required_price *= 0.9
        self.assertEqual(str(ke.exception), "'Your budget is not enough!'")

    def test_book_a_trip_with_enough_money_family(self):
        self.trip = Trip(12_000.00, 2, True)
        destination = self.trip.book_a_trip('Australia')
        self.assertEqual(f"'Successfully booked destination Australia! Your budget left is {self.trip.budget:.2f}'",
                         f"'{destination}'")

    def test_book_a_trip_with_enough_money_not_family(self):
        self.trip = Trip(12_000.00, 1, True)
        destination = self.trip.book_a_trip('Australia')
        self.assertEqual(f"'Successfully booked destination Australia! Your budget left is {self.trip.budget:.2f}'",
                         f"'{destination}'")

    def test_book_a_trip_with_enough_money_family_appends_booked_destinations(self):
        self.trip = Trip(12_000.00, 2, True)
        self.trip.book_a_trip('Australia')
        self.assertEqual({'Australia': 10260.0}, self.trip.booked_destinations_paid_amounts)

    def test_book_a_trip_with_enough_money_not_family_appends_booked_destinations(self):
        self.trip = Trip(12_000.00, 1, True)
        self.trip.book_a_trip('Australia')
        self.assertEqual({'Australia': 5700}, self.trip.booked_destinations_paid_amounts)

    def test_book_a_trip_with_enough_money_family_budget_decrease(self):
        self.trip = Trip(12_000.00, 3, True)
        self.trip.book_a_trip('Bulgaria')
        self.assertEqual(10650.0, self.trip.budget)

    def test_book_a_trip_with_enough_money_not_family_budget_decrease(self):
        self.trip = Trip(12_000.00, 3, False)
        self.trip.book_a_trip('Bulgaria')
        self.assertEqual(10500.0, self.trip.budget)

    def test_booking_status_no_bookings(self):
        self.assertEqual(self.trip.booking_status(), f'No bookings yet. Budget: {self.trip.budget:.2f}')

    def test_booking_status_with_bookings(self):
        self.trip = Trip(100_000.00, 2, True)
        self.trip.book_a_trip('Bulgaria')
        self.trip.book_a_trip('Australia')
        result = self.trip.booking_status()
        self.assertEqual(result,
                         "Booked Destination: Australia\n"
                         "Paid Amount: 10260.00\n"
                         "Booked Destination: Bulgaria\n"
                         "Paid Amount: 900.00\n"
                         "Number of Travelers: 2\n"
                         "Budget Left: 88840.00")


if __name__ == "__main__":
    main()
