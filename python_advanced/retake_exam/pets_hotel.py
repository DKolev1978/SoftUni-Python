def accommodate_new_pets(capacity: int, weight: float, *args):
    accommodated_pets = {}
    if not 0 <= capacity <= 50:
        raise SystemExit
    for el in args:
        pet_type, pet_weight = el
        if capacity > 0 and pet_weight <= weight:
            if pet_type not in accommodated_pets:
                accommodated_pets[pet_type] = 1
            else:
                accommodated_pets[pet_type] += 1

            capacity -= 1

    res = f"Accommodated pets:\n"
    for key, val in sorted(accommodated_pets.items()):
        res += f"{key}: {val}\n"
    if len(accommodated_pets) <= capacity:
        return f"All pets are accommodated! Available capacity: {capacity}.\n" + res
    else:
        return f"You did not manage to accommodate all pets!\n" + res
print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))
print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))


from unittest import TestCase, main


class Test(TestCase):
    def test_accommodate_pets(self):
        result = accommodate_new_pets(
            2,
            15.0,
            ("dog", 10.0),
            ("cat", 5.8),
            ("cat", 2.7),

        )

        self.assertEqual(
            result.strip(),
            """You did not manage to accommodate all pets!
Accommodated pets:
cat: 1
dog: 1""")


if __name__ == '__main__':
    main()
