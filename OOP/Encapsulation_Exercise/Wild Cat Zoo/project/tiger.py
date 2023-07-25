from project.animal import Animal


class Tiger(Animal):
    def __init__(self, name: str, gender: str, age: int, money_for_care: int) -> None:
        super().__init__(name, gender, age, money_for_care)
        self.money_for_care = 45
