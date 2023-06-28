class Product:
    def __init__(self, name: str, quantity: int) -> None:
        self.name = name
        self.quantity = quantity

    def decrease(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity

    def increase(self, quantity: int):
        self.quantity += quantity

    def __repr__(self) -> str:
        return self.name

