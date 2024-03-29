class Account:
    def __init__(self, id: int, name: str, balance: int = 0):
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, amount: int) -> int:
        self.balance += amount
        return self.balance

    def debit(self, amount: int) -> int or str:
        if amount > self.balance:
            return "Amount exceeded balance"

        self.balance -= amount
        return self.balance

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"


account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())

# account = Account(5411256, "Peter")
# print(account.debit(500))
# print(account.credit(1000))
# print(account.debit(500))
# print(account.info())

import unittest


class Tests(unittest.TestCase):
    def test_init_with_balance(self):
        a = Account(1, "A", 10)
        self.assertEqual(a.id, 1)
        self.assertEqual(a.name, "A")
        self.assertEqual(a.balance, 10)

    def test_init_without_balance(self):
        a = Account(1, "A")
        self.assertEqual(a.id, 1)
        self.assertEqual(a.name, "A")
        self.assertEqual(a.balance, 0)

    def test_credit(self):
        a = Account(123, "B", 10)
        res = a.credit(10)
        self.assertEqual(res, 20)
        self.assertEqual(a.balance, 20)

    def test_debit_successfull(self):
        a = Account(333444, "X", 1000)
        res = a.debit(999)
        self.assertEqual(res, 1)
        self.assertEqual(a.balance, 1)

    def test_debit_unsuccessfull(self):
        a = Account(5555, "N", 500)
        res = a.debit(1000)
        self.assertEqual(res, "Amount exceeded balance")
        self.assertEqual(a.balance, 500)

    def test_info(self):
        a = Account(4321, "ABC", 400)
        res = a.info()
        self.assertEqual(res, "User ABC with account 4321 has 400 balance")


if __name__ == "__main__":
    unittest.main()
